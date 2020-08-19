import bpy
import os
from mathutils import Vector, Quaternion
import numpy as np
import bmesh
from math import radians
import pickle

class Plant_Processor:

    def __init__(self):
        # USER INPUT: Set active flags for different operations:
        self.number_of_objects = 500 #total number of plant objects to process
        self.terrain = True
        self.capture_partial_cloud = True
        self.save_seperated_objects = True
        self.file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'project', 'deepLeaveSegmentation', 'synth_data', 'original_plant_obj')
        self.save_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'project', 'deepLeaveSegmentation', 'synth_data')
        self.resolutionX = 480
        self.resolutionY = 480
        self.camera_shots = [(0,0),(20,45),(40,-45)] # A list of camera shots to take of all plants, given as view angle and rotation in degrees
        self.output_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'project', 'deepLeaveSegmentation', 'synth_data', 'partial_cloud_pickles')

        # More setup operations
        bpy.context.scene.render.resolution_x = self.resolutionX
        bpy.context.scene.render.resolution_y = self.resolutionY
        self.outclouds = None
        self.outlabels = None

    def init_cleanup(self):
        '''Initial clean up of the default scene'''
        bpy.ops.object.select_all(action='DESELECT') # deselect all objects
        if bpy.data.objects.get("Cube") is not None:
            bpy.data.objects['Cube'].select_set(True) # Select the default cube object
            bpy.ops.object.delete() # remove the cube
        bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(0, 0, 0))
        bpy.data.objects['Camera'].parent = bpy.data.objects['Empty']

    def open_and_split(self):
        '''open each generated full plant mesh one by one and split into organs, perform other operations within the loop'''
        for i in range(1,self.number_of_objects+1):
            file_string = 'tomato%s.obj' %i
            file = os.path.join(self.file_path, file_string)
            try:
                imported_object = bpy.ops.import_scene.obj(filepath=file)
                obj_object = bpy.context.selected_objects[0] ####<--Fix the selected object
            except:
                break
            # center the plant:
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
            obj_object.location[0] = 0
            obj_object.location[1] = 0

            bpy.ops.mesh.separate(type='MATERIAL') # split the tomato by its different materials (leaves, trunk, stems)
            self.rename_components()

            ''' do operations on the split meshes here '''
            if self.terrain == True:
                self.add_terrain(i)

            if self.capture_partial_cloud == True:
                for shot in self.camera_shots:
                    self.setupCamera(shot[0], shot[1]) # Here the view is adjusted
                    bpy.context.view_layer.update() # Update the view layer once all objects are in place
                    pc_out, labels_out = self.get_partial_pc(i)
                    self.format_clouds(pc_out, labels_out)
                    #self.show_point_cloud(pc_out)
                    pc_out = None
                    labels_out = None

            if self.save_seperated_objects == True:
                self.save_meshes(i) # saves the split meshes and also deletes them up from the scene

            self.cleanup() # clear the scene

            if i%50 == 0:
                # every now and then export and free up memory
                self.export_clouds(i/50)

    def rename_components(self):
        for obj in list(bpy.data.objects):
            if 'tomato' in obj.name:
                obj.name = obj.active_material.name
                obj.name = obj.name.split('.')[0]

    def export_clouds(self, id):
        # Save the collected point clouds in batches
        cloud_string = '%s_partial_clouds.pickle' %id
        label_string = '%s_labels.pickle' %id
        cloud_file = os.path.join(self.output_path, cloud_string)
        label_file = os.path.join(self.output_path, label_string)
        with open(cloud_file, 'wb') as f:
            pickle.dump(self.outclouds,f)
        with open(label_file, 'wb') as f:
            pickle.dump(self.outlabels,f)

        # Free up memory and get the next batch
        self.outclouds = None
        self.outlabels = None

    def format_clouds(self, cloud, labels):
        cloud = cloud.reshape(1,cloud.shape[0]*cloud.shape[1],3)
        labels = labels.reshape(1,labels.shape[0]*labels.shape[1],1)

        if self.outclouds is None and self.outlabels is None:
            self.outclouds = cloud
            self.outlabels = labels
        else:
            self.outclouds = np.concatenate((self.outclouds,cloud),axis = 0)
            self.outlabels = np.concatenate((self.outlabels,labels),axis = 0)

    def add_terrain(self, i):
        bpy.ops.mesh.landscape_add(refresh=True)
        bpy.context.object.ant_landscape.subdivision_x = 64
        bpy.context.object.ant_landscape.subdivision_y = 64
        bpy.context.object.ant_landscape.mesh_size_x = 3
        bpy.context.object.ant_landscape.mesh_size_y = 3
        bpy.context.object.ant_landscape.random_seed = i
        bpy.context.object.ant_landscape.height_offset = 0
        bpy.context.object.ant_landscape.height = 0.05
        bpy.context.object.ant_landscape.lacunarity = 2
        bpy.context.object.ant_landscape.noise_size = 0.5
        bpy.context.object.name = "Landscape"
        bpy.ops.mesh.ant_landscape_regenerate()
        bpy.ops.mesh.ant_landscape_refresh()

    def setupCamera(self, view_angle, rotation):
        # Maybe add some noise to the location and orientation of the camera view? Right now view locations are constant
        bpy.data.objects['Camera'].location[0] = 0
        bpy.data.objects['Camera'].location[1] = 0 + (view_angle / 500)
        bpy.data.objects['Camera'].location[2] = 1
        bpy.data.objects['Camera'].rotation_euler[0] = 0
        bpy.data.objects['Camera'].rotation_euler[1] = 0
        bpy.data.objects['Camera'].rotation_euler[2] = 0
        bpy.data.objects['Empty'].rotation_euler[0] = radians(view_angle)
        bpy.data.objects['Empty'].rotation_euler[2] = radians(rotation)

    def cleanup(self):
        all_objects = list(bpy.data.objects)
        for obj in all_objects:
            if not 'Camera' in obj.name and not 'Light' in obj.name and not 'Empty' in obj.name:
                obj.select_set(True)
                bpy.ops.object.delete()

    def get_depthmap(self):
        '''Sets up the blender nodes needed to capture a depth map from the camera position'''
        # Code adapted from https://devtalk.blender.org/t/adjust-z-pass-range-automatically-to-get-depth-image/9909
        # Set up rendering of depth map:
        bpy.context.scene.use_nodes = True
        tree = bpy.context.scene.node_tree
        links = tree.links

        # clear default nodes
        for n in tree.nodes:
            tree.nodes.remove(n)

        # create input render layer node
        rl = tree.nodes.new('CompositorNodeRLayers')

        # The viewer can come in handy for inspecting the results in the GUI
        depthViewer = tree.nodes.new(type="CompositorNodeViewer")
        links.new(rl.outputs[2], depthViewer.inputs[0])
        # Use alpha from input.
        links.new(rl.outputs[1], depthViewer.inputs[1])

        # create a file output node and set the path
        #fileOutput = tree.nodes.new(type="CompositorNodeOutputFile")
        #fileOutput.base_path = os.path.join(os.path.expanduser('~'), 'Desktop',)
        #links.new(invert.outputs[0], fileOutput.inputs[0])

        #Get the final depth map:
        bpy.ops.render.render()
        img=bpy.data.images['Viewer Node']
        pixels = img.pixels

    def get_partial_pc(self,i):

        ''' Capture a partial point cloud (simulated depth camera) using ray casting:
        Adapted from https://blender.stackexchange.com/questions/115285/how-to-do-a-ray-cast-from-camera-originposition-to-object-in-scene-in-such-a-w'''
        # camera object which defines ray source
        cam = bpy.data.objects['Camera']
        container = bpy.data.objects['Empty']
        # save current view mode
        # mode = bpy.context.area.type
        # set view mode to 3D to have all needed variables available
        #bpy.context.area.type = "VIEW_3D"
        # get vectors which define view frustum of camera
        frame = cam.data.view_frame(scene=bpy.context.scene)
        topRight = frame[0]
        bottomRight = frame[2]
        bottomLeft = frame[2]
        topLeft = frame[3]

        label_dict = {'Landscape':0, 'leaves':1, 'stems_1':2, 'trunk':3}

        # setup vectors to match pixels
        xRange = np.linspace(topLeft[0], topRight[0], self.resolutionX)
        yRange = np.linspace(topLeft[1], bottomLeft[1], self.resolutionY)

        # array to store hit information
        values = np.empty((xRange.size, yRange.size, 3), dtype=object)
        labels = np.empty((xRange.size, yRange.size), dtype=object)

        # indices for array mapping
        indexX = 0
        indexY = 0
        # iterate over all X/Y coordinates
        for x in xRange:
            for y in yRange:
                # get current pixel vector from camera center to pixel
                pixelVector = Vector((x, y, topLeft[2]))
                # rotate that vector according to camera rotation
                pixelVector.rotate(cam.matrix_world.to_quaternion())
                #pixelVector.rotate(container.matrix_world.to_quaternion())
                #destination = matrixWorldInverted @ (pixelVector + cam.matrix_world.translation)
                #direction = (destination - origin).normalized()
                origin = cam.matrix_world.to_translation()

                # perform the actual ray casting
                hit, location, norm, face, hit_object, matrix = bpy.context.scene.ray_cast(bpy.context.view_layer,origin,pixelVector)

                if hit:
                    values[indexX,indexY] = np.array(location)
                    labels[indexX,indexY] = label_dict[hit_object.name.split('.')[0]]

                # update indices
                indexY += 1

            indexX += 1
            indexY = 0

        return values, labels

    def show_point_cloud(self, values):
        '''Visualises the captured point cloud in the Blender GUI, Primarily for debugging purposes'''
        mesh = bpy.data.meshes.new(name='created mesh')
        bm = bmesh.new()

        vls = values.reshape(values.shape[0]*values.shape[1],3)

        # iterate over all possible hits
        for index, location in enumerate(vls):
            # no hit at this position
            if location[0] is not None:
                # add new vertex
                bm.verts.new((location[0], location[1], location[2]))

        # make the bmesh the object's mesh
        bm.to_mesh(mesh)
        bm.free()  # always do this when finished

        # We're done setting up the mesh values, update mesh object and
        # let Blender do some checks on it
        mesh.update()
        mesh.validate()

        # Create Object whose Object Data is our new mesh
        obj = bpy.data.objects.new('created object', mesh)

        # Add *Object* to the scene, not the mesh
        scene = bpy.context.scene
        scene.collection.objects.link(obj)

        # Select the new object and make it active
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        # reset view mode
        #bpy.context.area.type = mode

    def save_meshes(self,i):
        '''select the resulting tomato meshes and save them seperately
        meshes are also cleaned from the scene during the saving procedure'''
        for split_object in bpy.data.objects: # Check for given object names
            bpy.ops.object.select_all(action='DESELECT') # deselect all objects

            if not 'Camera' in split_object.name and not 'Light' in split_object.name and not 'Empty' in split_object.name:
                split_object.select_set(True) #only select one at a time
                dae_save_string = '%s_%s.dae' %(i,split_object.name.split('.')[0])
                obj_save_string = '%s_%s.obj' %(i,split_object.name.split('.')[0])
                dae_save_location = os.path.join(self.save_path, 'split_by_organ_dae', dae_save_string)
                obj_save_location = os.path.join(self.save_path, 'split_by_organ_obj', obj_save_string)

                bpy.ops.export_scene.obj(filepath=obj_save_location,
                                            use_selection=True,
                                            use_normals=True,
                                            use_materials=True)
                bpy.ops.wm.collada_export(filepath=dae_save_location,
                                            check_existing=False,
                                            filter_blender=False,
                                            filter_image=False,
                                            filter_movie=False,
                                            filter_python=False,
                                            filter_font=False,
                                            filter_sound=False,
                                            filter_text=False,
                                            filter_btx=False,
                                            filter_collada=True,
                                            filter_folder=True,
                                            selected=True,
                                            sort_by_name=True,
                                            filemode=8,
                                            use_texture_copies=True,
                                            include_children=True)
                bpy.ops.object.delete() # remove the exported object from the scene

if __name__ == "__main__":
    pproc = Plant_Processor()
    pproc.init_cleanup() #First clean the scene
    pproc.open_and_split() #Load plant objects in a loop and perform operations on them
    print("Data processing completed")

import bpy
import os
from mathutils import Vector, Quaternion
import numpy as np
import bmesh

class Plant_Processor:

    def __init__(self):
        # USER INPUT: Set active flags for different operations:
        self.number_of_objects = 1 #total number of plant objects to process
        self.terrain = True
        self.capture_partial_cloud = True
        self.save_seperated_objects = True
        self.file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'project', 'deepLeaveSegmentation', 'synth_data', 'original_plant_obj')
        self.save_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'project', 'deepLeaveSegmentation', 'synth_data')
        self.resolutionX = 1920
        self.resolutionY = 1080

    def init_cleanup(self):
        '''Initial clean up of the default scene'''
        bpy.ops.object.select_all(action='DESELECT') # deselect all objects
        if bpy.data.objects.get("Cube") is not None:
            bpy.data.objects['Cube'].select_set(True) # Select the default cube object
            bpy.ops.object.delete() # remove the cube

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
                self.setupCamera() # Here the view can be changed
                bpy.context.view_layer.update() # Update the view layer once all objects are in place
                pc_out, labels_out = self.get_partial_pc(i)

            if self.save_seperated_objects == True:
                self.save_meshes(i) # saves the split meshes and also deletes them up from the scene

            #self.show_point_cloud(pc_out)

            self.cleanup()

    def rename_components(self):
        for obj in list(bpy.data.objects):
            if 'tomato' in obj.name:
                obj.name = obj.active_material.name

    def export_clouds(self):
        pass

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
        bpy.ops.mesh.ant_landscape_refresh()

    def setupCamera(self):
        # Maybe add some noise to the location and orientation of the camera view
        bpy.data.objects['Camera'].location[0] = 0
        bpy.data.objects['Camera'].location[1] = 0
        bpy.data.objects['Camera'].location[2] = 2
        bpy.data.objects['Camera'].rotation_euler[0] = 0
        bpy.data.objects['Camera'].rotation_euler[1] = 0
        bpy.data.objects['Camera'].rotation_euler[2] = 0


    def cleanup(self):
        all_objects = list(bpy.data.objects)
        for obj in all_objects:
            if not 'Camera' in obj.name and not 'Light' in obj.name:
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
        # save current view mode
        mode = bpy.context.area.type
        # set view mode to 3D to have all needed variables available
        bpy.context.area.type = "VIEW_3D"
        # get vectors which define view frustum of camera
        frame = cam.data.view_frame(scene=bpy.context.scene)
        topRight = frame[0]
        bottomRight = frame[2]
        bottomLeft = frame[2]
        topLeft = frame[3]

        # setup vectors to match pixels
        xRange = np.linspace(topLeft[0], topRight[0], self.resolutionX)
        yRange = np.linspace(topLeft[1], bottomLeft[1], self.resolutionY)

        # array to store hit information
        values = np.empty((xRange.size, yRange.size), dtype=object)
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
                origin = cam.location

                # perform the actual ray casting
                hit, location, norm, face, hit_object, matrix = bpy.context.scene.ray_cast(bpy.context.view_layer,origin,pixelVector)

                if hit:
                    values[indexX,indexY] = location
                    labels[indexX,indexY] = hit_object.name.split('.')[0]

                # update indices
                indexY += 1

            indexX += 1
            indexY = 0
        return values, labels

    def show_point_cloud(self, values):
        '''Visualises the captured point cloud in the Blender GUI, Primarily for debugging purposes'''
        mesh = bpy.data.meshes.new(name='created mesh')
        bm = bmesh.new()

        # iterate over all possible hits
        for index, location in np.ndenumerate(values):
            # no hit at this position
            if location is not None:
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

            if not 'Camera' in split_object.name and not 'Light' in split_object.name:
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

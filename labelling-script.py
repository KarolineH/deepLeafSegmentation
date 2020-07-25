import bpy
import os

#Initial clean up0
bpy.ops.object.select_all(action='DESELECT') # deselect all objects
if bpy.data.objects.get("Cube") is not None:
    bpy.data.objects['Cube'].select_set(True) # Select the default cube object
    bpy.ops.object.delete() # remove the cube

#Open each generated tomato mesh one by one
file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'project', 'deepLeaveSegmentation', 'synth_data', 'original_plant_obj')
save_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'project', 'deepLeaveSegmentation', 'synth_data')
for i in range(1,6001):
    j = 0
    file_string = 'tomato%s.obj' %i
    file = os.path.join(file_path, file_string)
    try:
        imported_object = bpy.ops.import_scene.obj(filepath=file)
        obj_object = bpy.context.selected_objects[0] ####<--Fix the selected object
        bpy.ops.mesh.separate(type='MATERIAL') # split the tomato by its different materials (leaves, trunk, stems)

        #select only the resulting tomato meshes
        for split_object in bpy.data.objects:
            # Check for given object names
            bpy.ops.object.select_all(action='DESELECT') # deselect all objects
            if "tomato" in split_object.name:

                ### Add textures here?

                split_object.select_set(True) #only select one at a time
                j += 1
                dae_save_string = '%s_%s.dae' %(i,j)
                dae_save_location = os.path.join(save_path, 'split_by_organ_dae', dae_save_string)
                obj_save_string = '%s_%s.obj' %(i,j)
                obj_save_location = os.path.join(save_path, 'split_by_organ_obj', obj_save_string)

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

    except:
        break

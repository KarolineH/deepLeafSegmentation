import bpy
from mathutils import Vector, Quaternion
import numpy as np
import bmesh


''' Adapted from https://blender.stackexchange.com/questions/115285/how-to-do-a-ray-cast-from-camera-originposition-to-object-in-scene-in-such-a-w'''

# objects to consider
obj = bpy.data.objects['Cube']
targets = [obj] # list all objects in the scene here

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

# number of pixels in X/Y direction
resolutionX = int(bpy.context.scene.render.resolution_x * (bpy.context.scene.render.resolution_percentage / 100))
resolutionY = int(bpy.context.scene.render.resolution_y * (bpy.context.scene.render.resolution_percentage / 100))

# setup vectors to match pixels
xRange = np.linspace(topLeft[0], topRight[0], resolutionX)
yRange = np.linspace(topLeft[1], bottomLeft[1], resolutionY)

# array to store hit information
values = np.empty((xRange.size, yRange.size), dtype=object)

# indices for array mapping
indexX = 0
indexY = 0

# filling array with None
for x in xRange:
    for y in yRange:
        values[indexX,indexY] = (None, None)
        indexY += 1
    indexX += 1
    indexY = 0

# iterate over all targets
for target in targets:
    # calculate origin
    matrixWorld = target.matrix_world
    matrixWorldInverted = matrixWorld.inverted()
    origin = matrixWorldInverted @ cam.matrix_world.translation

    # reset indices
    indexX = 0
    indexY = 0

    # iterate over all X/Y coordinates
    for x in xRange:
        for y in yRange:
            # get current pixel vector from camera center to pixel
            pixelVector = Vector((x, y, topLeft[2]))

            # rotate that vector according to camera rotation
            pixelVector.rotate(cam.matrix_world.to_quaternion())

            # calculate direction vector
            destination = matrixWorldInverted @ (pixelVector + cam.matrix_world.translation)
            direction = (destination - origin).normalized()

            # perform the actual ray casting
            hit, location, norm, face =  target.ray_cast(origin, direction)

            if hit:
                values[indexX,indexY] = (matrixWorld @ location)

            # update indices
            indexY += 1

        indexX += 1
        indexY = 0

# create new mesh
# source: https://devtalk.blender.org/t/alternative-in-2-80-to-create-meshes-from-python-using-the-tessfaces-api/7445/3
mesh = bpy.data.meshes.new(name='created mesh')
bm = bmesh.new()

# iterate over all possible hits
for index, location in np.ndenumerate(values):
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

print("Done.")

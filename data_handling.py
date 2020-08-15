import tensorflow as tf
from tensorflow import keras
import open3d as o3d

pcd = o3d.io.read_point_cloud("./synth_data/split_clouds/1_1.ply")
#print(np.asarray(pcd.points))
o3d.visualization.draw_geometries([pcd], zoom=0.3412,
                                  front=[0.4257, -0.2125, -0.8795],
                                  lookat=[2.6172, 2.0475, 1.532],
                                  up=[-0.0694, -0.9768, 0.2024])
import pdb; pdb.set_trace()

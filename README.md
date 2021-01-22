# DeepLeafSegmentation
Robotics and Autonomous Systems MSc project

- plant_generator.sh creates 500 original random synthetic plant models using arbaro (deterministic procedure)
- labelling-script.py splits the models into seperate organs and captures annotated 3D point clouds from different viewing angles (run "./blender/blender --background --python labelling-script.py")
- pointnet2_tensorflow2/train_seg_net.py holds the custom PointNet++ implementation and testing procedures

Dependencies: 
python 3.5.2
tensorflow 2.2
Arbaro http://arbaro.sourceforge.net/
Blender www.blender.org/

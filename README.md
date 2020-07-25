# DeepLeaveSegmentation
Robotics and Autonomous Systems MSc project

- plant_generator.sh creates the original synthetic plant models using arbaro (deterministic procedure)
- labelling-script.py splits the models into seperate organs (saves both .dae and .obj) run "./blender/blender --background --python labelling-script.py"
- sample_points.sh samples points from the seperate meshes (.ply format)


Run CloudCompare: from anywhere run "cloudcompare.CloudCompare"
Run Arbaro: navigate to deepLeaveSegmentation/arbaro and run "java -jar arbaro.jar"

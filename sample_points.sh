#!/bin/bash
DENSITYVAR="100000"

for i in {1..2}
do
  cloudcompare.CloudCompare -SILENT -AUTO_SAVE OFF \
   -O synth_data/split_by_organ_obj/${i}_Landscape.obj -SAMPLE_MESH DENSITY $DENSITYVAR -C_EXPORT_FMT PLY -SAVE_CLOUDS FILE "synth_data/split_clouds/${i}_Landscape.ply" -CLEAR_CLOUDS -CLEAR_MESHES \
   -O synth_data/split_by_organ_obj/${i}_leaves.obj -SAMPLE_MESH DENSITY $DENSITYVAR -C_EXPORT_FMT PLY -SAVE_CLOUDS FILE "synth_data/split_clouds/${i}_leaves.ply" -CLEAR_CLOUDS -CLEAR_MESHES \
   -O synth_data/split_by_organ_obj/${i}_stems_1.obj -SAMPLE_MESH DENSITY $DENSITYVAR -C_EXPORT_FMT PLY -SAVE_CLOUDS FILE "synth_data/split_clouds/${i}_stems_1.ply" -CLEAR_CLOUDS -CLEAR_MESHES \
   -O synth_data/split_by_organ_obj/${i}_trunk.obj -SAMPLE_MESH DENSITY $DENSITYVAR -C_EXPORT_FMT PLY -SAVE_CLOUDS FILE "synth_data/split_clouds/${i}_trunk.ply" -CLEAR_CLOUDS -CLEAR_MESHES
done
/

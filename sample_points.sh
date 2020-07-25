#!/bin/bash
DENSITYVAR="10000"

for i in {1..6001}
do
  cloudcompare.CloudCompare -AUTO_SAVE OFF \
   -O synth_data/split_by_organ_obj/${i}_1.obj -SAMPLE_MESH DENSITY $DENSITYVAR -C_EXPORT_FMT PLY -SAVE_CLOUDS FILE "synth_data/split_clouds/${i}_1.ply" -CLEAR_CLOUDS -CLEAR_MESHES \
   -O synth_data/split_by_organ_obj/${i}_2.obj -SAMPLE_MESH DENSITY $DENSITYVAR -C_EXPORT_FMT PLY -SAVE_CLOUDS FILE "synth_data/split_clouds/${i}_2.ply" -CLEAR_CLOUDS -CLEAR_MESHES \
   -O synth_data/split_by_organ_obj/${i}_3.obj -SAMPLE_MESH DENSITY $DENSITYVAR -C_EXPORT_FMT PLY -SAVE_CLOUDS FILE "synth_data/split_clouds/${i}_3.ply" -CLEAR_CLOUDS -CLEAR_MESHES
done
/

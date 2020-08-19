#!/bin/bash
for i in {1..250}
do
  java -jar arbaro/arbaro_cmd.jar --quiet --seed $i --format OBJ --output "synth_data/original_plant_obj/tomato${i}.obj" tomato_medium.xml
done
for i in {251..500}
do
  java -jar arbaro/arbaro_cmd.jar --quiet --seed $i --format OBJ --output "synth_data/original_plant_obj/tomato${i}.obj" tomato_small.xml
done

#!/bin/bash
for i in {1..2}
do
  java -jar arbaro/arbaro_cmd.jar --quiet --seed $i --format OBJ --output "synth_data/original_plant_obj/tomato${i}.obj" tomato_example.xml
done

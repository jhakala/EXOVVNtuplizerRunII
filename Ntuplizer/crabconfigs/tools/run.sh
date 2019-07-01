#!/bin/bash
# declare an array variable
declare -a arr=("B" "C" "D" "E" "F")

## now loop through the above array
for i in "${arr[@]}"
do
   cmsRun VgammaTuplizer/Ntuplizer/config_generic"$i".py >> output.txt
   # or do whatever with individual element of the array
done

# You can access them using echo "${arr[0]}", "${arr[1]}" also


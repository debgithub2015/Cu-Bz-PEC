#! /bin/bash

mkdir adsorption_system/

cd adsorption_system/ 

python ../gen_in-adsorption.py

for i in {00..30}
do
echo $i
awk '!($5="")' adsorption_system_$i.in > tmp.in
sed -i 's/4 4 1 0  0/4 4 1 0 0 0/g' tmp.in ; mv tmp.in adsorption_system_$i.in
awk 'NR>36{$5="0";$7="0";$9="0"};1;NR>62{exit}' adsorption_system_$i.in > tmp.in
awk 'NR>63{print}' adsorption_system_$i.in >> tmp.in ; mv tmp.in adsorption_system_$i.in
done

cd ../

mkdir molecular_overlayer/

cd molecular_overlayer/ 

python ../gen_in-moloverlayer.py

for i in {00..30}
do
echo $i
awk '!($5="")' molecule_overlayer_system_$i.in > tmp.in
sed -i 's/1 1 1 0  0/1 1 1 0 0 0/g' tmp.in ; mv tmp.in molecule_overlayer_system_$i.in
done

cd ../


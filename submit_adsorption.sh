#!/bin/bash

#SBATCH --job-name=Ag-vdw-df
#SBATCH --output="%j.o"
#SBATCH --error="%j.e"
#SBATCH --account="thonhauserGrp"
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=8
#SBATCH --cpus-per-task=1
#SBATCH --time=7-00:00:00
#SBATCH --constraint=rhel7
#SBATCH --mail-user="chakrad@wfu.edu"
#SBATCH --mail-type=FAIL
#SBATCH --partition="medium"
#SBATCH --mem=30Gb

ulimit -s unlimited

module load rhel7/compilers/intel-2018-lp64 rhel7/openmpi/3.1.1-intel-2018

pwdir="/deac/thonhauserGrp/chakrad/quantum-espresso-6.3/qe-6.3-openmpi-3.1.1/bin/pw.x"

adsorption_path="/deac/thonhauserGrp/chakrad/calculations/atomandmolecule-qe6.2.1-i2012-C6modif/coinage_metal_new/Cu-bz-PEC/vdw-df/adsorption_system"

for i in {24..30}; do
mpirun $pwdir < $adsorption_path/adsorption_system_$i.in > $adsorption_path/adsorption_system_$i.out
done


echo "DONE"

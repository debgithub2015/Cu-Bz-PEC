from ase import io
from numpy import *
import sys
import math

def create_in_file(i):
    ref_filename="/deac/thonhauserGrp/chakrad/calculations/atomandmolecule-qe6.2.1-i2012-C6modif/coinage_metal_new/Cu-bz-PEC/vdw-df/input_xsf_files/molecule_overlayer_system_%02d.xsf"%i
    atoms=io.read(ref_filename)
    positions=atoms.get_positions()
    cell=atoms.get_cell()
#    print cell
#    print positions
#    print atoms 

    atoms.write('atoms.xyz')

    Natoms = atoms.get_number_of_atoms()

    types_atoms = set(atoms.get_chemical_symbols())

    Ntyp = len(types_atoms)

    text_control='''&control
calculation='scf'
restart_mode='from_scratch',
pseudo_dir='/deac/thonhauserGrp/chakrad/calculations/atomandmolecule-qe6.2.1-i2012-C6modif/all_pbe_UPF_v1.5'
prefix='benzene_%02d'
disk_io='none'
forc_conv_thr=3d-3
/'''%i

    text_system = '''
&system
ibrav=0
nat = %i
ntyp= %i
occupations     = fixed
ecutwfc         = 50
ecutrho         = 600
nosym           = .true.
input_dft = 'vdw-df'
/'''%(Natoms,Ntyp)

    text_misc='''
&electrons
conv_thr =  1.0d-8
/'''

    text_species='''
ATOMIC_SPECIES
'''
    if 'Cu' in types_atoms:
     text_species += 'Cu  1.0   cu_pbe_v1.2.uspp.F.UPF\n'
    if 'Ag' in types_atoms:
     text_species += 'Ag  1.0  ag_pbe_v1.4.uspp.F.UPF\n'
    if 'Au' in types_atoms:
     text_species += 'Au  1.0  au_pbe_v1.uspp.F.UPF\n'
    if 'C' in types_atoms:
     text_species +=  'C  1.0  c_pbe_v1.2.uspp.F.UPF\n'
    if 'H' in types_atoms:
     text_species +=  'H  1.0  h_pbe_v1.4.uspp.F.UPF\n'
#  text_species += '   k_points automatic\n'
#  text_species += '   3 3 1 0 0 0  '

    input_cell = list(cell[0])+list(cell[1])+list(cell[2])

    text_cell='''
CELL_PARAMETERS angstrom
%5.16f\t %5.16f\t %5.16f
%5.16f\t %5.16f\t %5.16f
%5.16f\t %5.16f\t %5.16f
'''%(tuple(input_cell))

    text_atomic_pos="ATOMIC_POSITIONS angstrom\n"
    file = open('atoms.xyz','r')
    content = file.readlines()
    file.close()

    for line in content[2:]:
         text_atomic_pos +=line

    text_kpoints='''
K_POINTS automatic 
1 1 1 0 0 0  
'''
    full_text = text_control + text_system + text_misc + text_species+ text_cell + text_atomic_pos + text_kpoints

    print full_text

    file = open('molecule_overlayer_system_%02d.in'%i,'w')
    file.write(full_text)
    file.close()


for i in range(31):
    create_in_file(i)

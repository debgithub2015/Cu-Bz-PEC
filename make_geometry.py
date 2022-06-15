from ase import *
from ase import io
from numpy import array
from math import pi

sep_list = [4.00, 3.95, 3.90 , 3.85,  3.80, 3.75,  3.70, 3.65, 3.60 ,3.55, 3.5, 3.45, 3.40, 3.35, 3.30, 3.25, 3.20, 3.15, 3.10, 3.05 , 3.00, 2.95, 2.90 , 2.85,  2.80, 2.75,  2.70, 2.65, 2.60 ,2.55, 2.5]   # Len 35

phi = 30
#phi = 0

#pos = 'fcc'
pos = 'hcp'

# height
#h = 3.0

def create_in_file(i):
	h=sep_list[i]
	molecule = io.read('/deac/thonhauserGrp/chakrad/calculations/atomandmolecule-qe6.2.1-i2012-C6modif/coinage_metal_new/scripts/benzene-vdW-DF-relaxed.xsf')
		
	slab = io.read('/deac/thonhauserGrp/chakrad/calculations/atomandmolecule-qe6.2.1-i2012-C6modif/coinage_metal_new/scripts/Cu111_slab_vdw-df-relaxed.xsf')
	slab.translate([0,0,-7])

	molecule.set_cell(slab.cell)

	edge = slab.positions[-1][2]

	if pos == 'fcc':
	    fcc_pos = slab.positions[-22]
	    new_pos = fcc_pos.copy()
	    new_pos[2] =  h + edge
	    molecule.center(about = new_pos)
	    molecule.euler_rotate(phi = phi, center='COP')

	if pos == 'hcp':
	    hcp_pos = slab.positions[-14]
	    new_pos = hcp_pos.copy()
	    new_pos[2] =  h + edge
	    molecule.center(about = new_pos)
	    molecule.euler_rotate(phi = phi, center='COP')
# Set rotation here.


	atoms = slab + molecule
	atoms.write('adsorption_system_%02d.xsf'%(i))
	molecule.write('molecule_overlayer_system_%02d.xsf'%(i))

for i in range(31):
  create_in_file(i)


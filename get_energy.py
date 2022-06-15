import sys
from numpy import *
import pylab as pl
import scipy.optimize as optimization
import scipy.interpolate as interpolate

Ryd = 13.6057*1000

Eval_ads = zeros(31)
Eval_mol = zeros(31)
Eval_tot = zeros(31)
for i in range(0,31):
  file = open("adsorption_system/adsorption_system_%02d.out"%i)
  content = file.readlines()
  file.close()
  for line in content:
     if '!' in line:
	val=float(line.split()[-2])
	Eval_ads[i] = val

  imin = Eval_ads.argmin()

  file = open("molecular_overlayer/molecule_overlayer_system_%02d.out"%i)
  content = file.readlines()
  file.close()
  for line in content:
     if '!' in line:
	val=float(line.split()[-2])
	Eval_mol[i] = val
   	
  Eval_tot[i]=Eval_ads[i]-Eval_mol[i]   

  sep_list = [4.00, 3.95, 3.90 , 3.85,  3.80, 3.75,  3.70, 3.65, 3.60 ,3.55, 3.5, 3.45, 3.40, 3.35, 3.30, 3.25, 3.20, 3.15, 3.10, 3.05 , 3.00, 2.95, 2.90 , 2.85,  2.80, 2.75,  2.70, 2.65, 2.60 ,2.55, 2.5] 


  print sep_list[i],'\t',Eval_ads[i],'\t', Eval_mol[i],'\t', Eval_tot[i]
   

#  print imin,'\t',Eval_ads[imin]*Ryd,'\t', Eval_mol[imin]*Ryd,'\t', Eval_tot[imin]*Ryd
       
#savetxt('adsorption.txt',Eval_ads )
#savetxt('molecular_ovelayer.txt',Eval_mol )
#savetxt('adsorption+moloverlayer.txt',Eval_tot )

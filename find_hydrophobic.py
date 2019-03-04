#!/usr/bin/env python

import sys
try:
	data = open(sys.argv[1],'r').readlines()
	model = sys.argv[2]

except:
	sys.exit('USAGE: find_hydrophobic.py <contacts list file> <model #>')
chain = []

realdata = False
selcom = []
atomselcom=[]
for i in data[8:]:
	line = i.split()
	if 'C' in line[3] and 'C' in line[7] and line[0] != line[4]:
		selcom.append('#{0}:{1}'.format(model,line[2]))
		atomselcom.append('{0}:{1}@{2}'.format(line[0],line[2],line[3]))
		atomselcom.append('{0}:{1}@{2}'.format(line[4],line[6],line[7]))
print('\nFound {0} residues with hydrophobic interactions'.format(len(selcom)))
if len(selcom) > 0:
	print('\nsel {0}\n'.format(' '.join(selcom)))
	print("Select atoms - only works for original session")
	print('\nsel {0}\n'.format(' '.join(atomselcom)))
#!/usr/bin/env python

import sys
try:
	data = open(sys.argv[1],'r').readlines()
	model = sys.argv[2]
except:
	sys.exit('USAGE: find_saltbridge.py <contacts list file> <model #>')
chain = []

poz = ['NH1','NH2','NE','NZ']
neg = ['OD1','OD2','OE1','OE2']
pozAA = ['ARG','LYS','HIS']
negAA = ['ASP','GLU']
selcom = []
atomselcom = []
for i in data[8:]:
	line = i.split()
	if ((line[3] in poz and line[1] in pozAA)  and (line[7] in neg and line[5] in negAA)) or  ((line[3] in neg and line[1] in negAA)  and (line[7] in poz and line[5] in pozAA))  and line[0] != line[4]:
		selcom.append('#{0}:{1}'.format(model,line[2]))
		atomselcom.append('{0}:{1}@{2}'.format(line[0],line[2],line[3]))
		atomselcom.append('{0}:{1}@{2}'.format(line[4],line[6],line[7]))
print('\nFound {0} residues involved in salt bridges'.format(len(selcom)))
if len(selcom) > 0:
	print('\nsel {0}\n'.format(' '.join(selcom)))
	print("Select atoms - only works for original session")
	print('\nsel {0}\n'.format(' '.join(atomselcom)))
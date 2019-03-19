# crystal_contacts_analysis
Analyse crystal contacts in crystal structures

first make the necessray files in chimera - (will eventually automate this):

0. open the crystal structre pdb file

1. Use menu entry Tools / Higher-Order Structure / Multiscale Models, select multimer type "3x3x3 crystal unit cells" near the bottom of the multiscale dialog and press the "Make models" button.

2. Press the select "with loaded atoms" button at the top of the multiscale dialog to select the original molecule, adjust the contact "Range" near the top of the dialog, then press the "Near" button.

3. Press the other chains "Hide" button to hide the non-contacting chains.

4. Press the style "Show..." button and choose  "Wire" from the menu.

5. use Tools / Surface/BindingAnalysis / Find contacts/clashes

6. Make sure the save file option is selected 

7. Designate the original model for checking - select it on model panel and then click designate

8. Designate all other models for checking against - select them on model panel and then click designate

9. use all other default params for now

10. use Tools / Surface/Binding Analysis / FindHBonds. make sure the save file option is selected for this also.

This is a modified versio of a protocol originally from Tom Goddard.

--> done chimera-ing for now

run the scripts - :

find_hydrophobic.py <contacts list file> <model #>
find_hbonds.py <hbonds list file> <model #>
find_saltbridge.py <contacts list file> <model #>

If you are using the original chimera session the model number will be 0, if you have reopened the file if may have changed.
Each script makes prints out a line that can be pasted into the chimera command line to select the residues involved in those interactions.

Some residues may come up as multiple types of interactions. I like to do them in the order hydrophobic-hbond-saltbridge. 

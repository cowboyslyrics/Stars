# -*- coding: utf-8 -*-
"""
https://www.decodingdevops.com/python-write-to-file-line-by-line/
write to the pokerstars notes.xml
use the above link as a tutorial

"""

playas="losers.txt"

index=1627255667
donors= "<note player=\"Artishell\" label=\"0\" update=\"" + str(index) + "\"></note>\n"
player = "Artishell"

F = open("note.xml","a")

for line in range(5):
    F.writelines(donors)
    index  +=1
    donors= "<note player=\"Artishell\" label=\"0\" update=\"" + str(index) + "\"></note>\n"
    

F.close()
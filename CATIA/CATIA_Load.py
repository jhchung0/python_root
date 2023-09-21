import win32com.client
import math
#import pandas 
CATIA=win32com.client.Dispatch("CATIA.Application")
CATIA.Visible=True
DOCs=CATIA.Documents
PRDDOC=DOCs.add("Part")
PRT1=PRDDOC.Part
HYSH1=PRT1.hybridbodies.add()
HYSH1.Name = "AAA"
HSFAC1=PRT1.HybridShapefactory
for i in range(800):
    PT1=HSFAC1.AddNewPointCoord(300*math.cos(i/20),200*math.sin(i/20),i)
    HYSH1.appendhybridshape(PT1)
PRT1.Update()


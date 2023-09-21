from PIL import Image
import os
import glob

filepath1=""
filepath1 = "C:/WORKING\WEB_on_EVDM\plm\EDU\EDU_SIMULIA_Structural Simulation Essentials/00 - Overview - Structural Simulation Essentials/Overview - Structural Simulation Essentials/"


inputlist1 = glob.glob(filepath1 + "*.jpg")

#print(inputlist1)

for f in inputlist1:
    print(f)
    img = Image.open(f)
    img_resize = img.resize((1600,900))
    print (img_resize.size)
    title,ext = os.path.splitext(f)
    img_resize.save(title + '_resize' + ext)



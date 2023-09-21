from PIL import Image
import os

filepath1=""
filepath1 = "C:/WORKING\WEB_on_EVDM\plm\EDU\EDU_SIMULIA_Structural Simulation Essentials/00 - Overview - Structural Simulation Essentials/Overview - Structural Simulation Essentials/"


img = Image.open(filepath1 + "Overview - Structural Simulation Essentials-page-001.jpg")
img_resize = img.resize((1600,900))



print ( img_resize.size)

img_resize.save(filepath1 +"Overview - Structural Simulation Essentials-page-001_again.jpg")
os.path.isfile(filepath1 +"Overview - Structural Simulation Essentials-page-001_again.jpg")

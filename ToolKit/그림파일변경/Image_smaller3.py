from PIL import Image
from tkinter.filedialog import askdirectory
import os
import glob


filepath1=""
filepath1 = askdirectory( initialdir="D:/DEV")

if not os.path.exists(filepath1):
    print("Path not exist" )
    quit()
else:
    print(filepath1)
inputlist1 = glob.glob(filepath1 + "/*.jpg")

# print(inputlist1)

for f in inputlist1:
    print(f)
    img = Image.open(f)
    img_resize = img.resize((int(413),int(531)))
    os.remove(f)
    print (img_resize.size)
    #title,ext = os.path.splitext(f)
    img_resize.save(f)



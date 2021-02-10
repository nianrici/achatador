import os
import subprocess

achata = "mogrify -geometry 1:1 *.bmp"
recorta = "convert *.bmp -crop x800+0+320 +repage HelpScreens.png"

dirname = "."
deleter = os.listdir(dirname)

subprocess.call(achata, shell=True)
subprocess.call(recorta, shell=True)
# os.remove("*.bmp")

for i in deleter:
    if i.endswith(".bmp"):
        os.remove(i)

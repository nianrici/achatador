import subprocess
import glob
import platform

INPUT_DIR = "."
OUTPUT_FILE = "HelpScreens.png"
IMAGE_PATTERN = "*.bmp"


def process_images_windows():
    for command in [
        f"mogrify -geometry 1:1 {IMAGE_PATTERN}",
        f"convert {IMAGE_PATTERN} -crop x800+0+320 +repage {OUTPUT_FILE}"
    ]:
        subprocess.call(command, shell=True)

    for file in glob.glob(f"{INPUT_DIR}\\{IMAGE_PATTERN}"):
        subprocess.call(["del", file])


def process_images_linux():
    for command in [
        f"mogrify -geometry 1:1 {IMAGE_PATTERN}",
        f"convert {IMAGE_PATTERN} -crop x800+0+320 +repage {OUTPUT_FILE}"
    ]:
        subprocess.call(command, shell=True)

    for file in glob.glob(f"{INPUT_DIR}/{IMAGE_PATTERN}"):
        subprocess.call(["rm", file])


system = platform.system()

if system == "Windows":
    process_images_windows()
elif system == "Linux":
    process_images_linux()
else:
    print("Este script solo es compatible con Windows y Linux.")

import importlib
import subprocess
import sys

import cv2
import matplotlib.pyplot as plt


def reload(module):
    """
    Reloads module with importlib.
    """
    importlib.reload(module)


def install(*package):
    """
    Executes pip install in Jupyter Notebook shell.
    """
    subprocess.run([sys.executable, "-m", "pip", "install"] + list(package))


def imshow(image):
    """
    Displays image with matplotlib.
    """
    plt.figure()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image)
    plt.show()


def imshow_opencv(image):
    """
    Displays image in OpenCV window.
    Press any key to exit.
    """
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

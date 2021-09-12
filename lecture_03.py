import numpy as np
import matplotlib.pylab as plt
import cv2

def showI(img):
    plt.figure(figsize=[20, 10])
    if len(img.shape) < 3:
        plt.imshow(img, 'gray')
    else:
        plt.imshow(img)

fDir = './images'

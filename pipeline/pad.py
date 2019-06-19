import numpy as np
import os
import sys
import imagio

def pad(a, img_res):
	"""Return bottom right padding."""
	zeros = np.full(img_res, 255)
	zeros[:a.shape[0], :a.shape[1], :a.shape[2]] = a
	return zeros

def pad_image(location, res):
    resolution = (res, res, 3)
    img = imageio.imread(location, mode='RGB').astype(np.float)
    if(img.shape[0] <= res and img.shape[1] <= res):
        padded = pad(img, resolution)
        imageio.imsave(location, padded)
    else:
        os.remove(location)
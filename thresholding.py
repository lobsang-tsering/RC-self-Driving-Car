import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def color_thr(s_img, v_img, s_threshold = (0,255), v_threshold = (0,255)):
    s_binary = np.zeros_like(s_img).astype(np.uint8)
    s_binary[(s_img > s_threshold[0]) & (s_img <= s_threshold[1])] = 1
    v_binary = np.zeros_like(s_img).astype(np.uint8)
    v_binary[(v_img > v_threshold[0]) & (v_img <= v_threshold[1])] = 1
    col = ((s_binary == 1) | (v_binary == 1))
    return col


import encoder
import voter
import perform_tensor_decomp as ptd
import compute_rigidity_tensor as crt

import cv2
import matplotlib.pyplot as plt
from skimage.feature import peak_local_max
import copy
import numpy as np


# Name of files
origimage2 = 'IMG_20221104_172457_k0.jpg'
origimage3 = 'IMG_20221104_172457.jpg'



def imshow(img, title=None):
    plt.imshow(img)
    if title is not None:
        plt.title = title
    plt.show()


def threshold(image, low, high, weak):
    output = np.zeros(image.shape)
 
    strong = 255/255
 
    strong_row, strong_col = np.where(image >= high)
    weak_row, weak_col = np.where((image <= high) & (image >= low))
 
    output[strong_row, strong_col] = strong
    output[weak_row, weak_col] = weak
 
    return output
 
 
def hysteresis(image, weak):
    image_row, image_col = image.shape
 
    top_to_bottom = image.copy()
 
    for row in range(1, image_row - 1):
        for col in range(1, image_col - 1):
            if top_to_bottom[row, col] == weak:
                if top_to_bottom[row, col + 1] == 255 or top_to_bottom[row, col - 1] == 255 or top_to_bottom[row - 1, col] == 255 or top_to_bottom[
                    row + 1, col] == 255 or top_to_bottom[
                    row - 1, col - 1] == 255 or top_to_bottom[row + 1, col - 1] == 255 or top_to_bottom[row - 1, col + 1] == 255 or top_to_bottom[
                    row + 1, col + 1] == 255:
                    top_to_bottom[row, col] = 255
                else:
                    top_to_bottom[row, col] = 0
 
    bottom_to_top = image.copy()
 
    for row in range(image_row - 2, 1, -1):
        for col in range(image_col - 2, 1, -1):
            if bottom_to_top[row, col] == weak:
                if bottom_to_top[row, col + 1] == 255 or bottom_to_top[row, col - 1] == 255 or bottom_to_top[row - 1, col] == 255 or bottom_to_top[
                    row + 1, col] == 255 or bottom_to_top[
                    row - 1, col - 1] == 255 or bottom_to_top[row + 1, col - 1] == 255 or bottom_to_top[row - 1, col + 1] == 255 or bottom_to_top[
                    row + 1, col + 1] == 255:
                    bottom_to_top[row, col] = 255
                else:
                    bottom_to_top[row, col] = 0
 
    right_to_left = image.copy()
 
    for row in range(1, image_row-1):
        for col in range(image_col - 2, 1, -1):
            if right_to_left[row, col] == weak:
                if right_to_left[row, col + 1] == 255 or right_to_left[row, col - 1] == 255 or right_to_left[row - 1, col] == 255 or right_to_left[
                    row + 1, col] == 255 or right_to_left[
                    row - 1, col - 1] == 255 or right_to_left[row + 1, col - 1] == 255 or right_to_left[row - 1, col + 1] == 255 or right_to_left[
                    row + 1, col + 1] == 255:
                    right_to_left[row, col] = 255
                else:
                    right_to_left[row, col] = 0
 
    left_to_right = image.copy()
 
    for row in range(image_row - 2, 1, -1):
        for col in range(1, image_col-2):
            if left_to_right[row, col] == weak:
                if left_to_right[row, col + 1] == 255 or left_to_right[row, col - 1] == 255 or left_to_right[row - 1, col] == 255 or left_to_right[
                    row + 1, col] == 255 or left_to_right[
                    row - 1, col - 1] == 255 or left_to_right[row + 1, col - 1] == 255 or left_to_right[row - 1, col + 1] == 255 or left_to_right[
                    row + 1, col + 1] == 255:
                    left_to_right[row, col] = 255
                else:
                    left_to_right[row, col] = 0
 
    final_image = top_to_bottom + bottom_to_top + right_to_left + left_to_right
 
    final_image[final_image > 255] = 255
 
    return final_image


########################### Processing the data #########################
scale = 10
weak = 0.2


img2 = cv2.imread(origimage2, cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread(origimage3, cv2.IMREAD_GRAYSCALE)

blurred_image = cv2.GaussianBlur(img3, (9, 9), 0)
dst = cv2.equalizeHist(blurred_image)

[s2, o2] = encoder.encode(img2, file_name=False)
[saliency2, ballness2, orientaion2] = voter.vote(s2, o2, scale)
#ret2, thresh2 = cv2.threshold(saliency2, 0.17, 1, cv2.THRESH_BINARY)
new_image2 = threshold(saliency2, 0.12, 0.2, weak=weak)
thresh2 = hysteresis(new_image2, weak)

[s4, o4] = encoder.encode(dst, file_name=False)
[saliency4, ballness4, orientaion4] = voter.vote(s4, o4, scale)
#ret4, thresh40 = cv2.threshold(saliency4, 0.17, 1, cv2.THRESH_BINARY)
new_image2 = threshold(saliency4, 0.12, 0.2, weak=weak)
thresh40 = hysteresis(new_image2, weak)


thresh = thresh2 + thresh40
#imshow(thresh, 'thresh')

#ret4, thresh4 = cv2.threshold(thresh, 4, 1, cv2.THRESH_BINARY)
#imshow(thresh4, 'thresh4')
#cv2.imwrite('ortho_all_thre40.jpg', 255*thresh4)


ret5, thresh5 = cv2.threshold(thresh, 1, 1, cv2.THRESH_BINARY)
#imshow(thresh5, 'thresh5')
#cv2.imwrite('ortho_all_thre50.jpg', 255*thresh5)


arr = np.uint8(255 * thresh5)
sk = cv2.ximgproc.thinning(arr, None, 1)


nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(sk, connectivity=8)
areas = stats[1:,cv2.CC_STAT_AREA]


result = np.zeros((labels.shape), np.uint8)

print(nlabels)
for i in range(nlabels - 1):
    if i % 1000 == 0:
	    print(i)
    if areas[i] >= 50:# and (areas[i] / (heig[i] * leng[i])) <= 0.4:   #keep
        result[labels == i + 1] = 255

imshow(result)

cv2.imwrite('results.jpg',result)
		


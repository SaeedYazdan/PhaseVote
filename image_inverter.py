import encoder
import voter
import perform_tensor_decomp as ptd
import compute_rigidity_tensor as crt

import cv2
import matplotlib.pyplot as plt
from skimage.feature import peak_local_max



origimage = 'IMG_20221104_172457_k0.jpg'

#origimage = 'new_img.jpg'


def imshow(img):
    plt.imshow(img)
    plt.show()




img = cv2.imread(origimage, cv2.IMREAD_GRAYSCALE)

imshow(img)
#img2 = copy.copy(img)
#img2[img2 < 80] = 0
#imshow(img2)

inv = 255 - img

imshow(inv)


cv2.imwrite('IMG_20221104_172457_k0_Inv.jpg', inv)

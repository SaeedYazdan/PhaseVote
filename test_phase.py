import cv2
import matplotlib.pyplot as plt



def imshow(img):
    plt.imshow(img)
    plt.show()


img = cv2.imread('IMG_20221104_172457.jpg', 0)#, cv2.IMREAD_GRAYSCALE)
#ret, thresh1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)

blur = cv2.GaussianBlur(img,(9,9),0)
#img = cv2.equalizeHist(img)
#imshow(blur)

#img2 = cv2.Canny(image=img, threshold1=100, threshold2=200) # Canny Edge Detection
#imshow(img2)

#inp = input('Which method to use? (psm, ps, pcs, pc): ')
#img = cv.imread('messi5.jpg',0)

#imshow(img)
#lower_reso = cv2.pyrDown(img)

#imshow(lower_reso)

#lower_reso = cv2.pyrDown(lower_reso)
#imshow(lower_reso)
#img = lower_reso



inp = 'pcm'

if inp == 'psm':
    import phasesymmono as psm
    nscale = 2
    mwl = 1  #3 orig
    mult = 2.1
    so = 0.3 #0.55 orig
    k = 1
    phaseSym, totalEnergy, T = psm.phasesymmono(img, nscale=nscale, minWaveLength=mwl, mult=mult, sigmaOnf=so, k=k, polarity=0, noiseMethod=-1)
    imshow(phaseSym)
    #imshow(totalEnergy)
    cv2.imwrite('IMG_20221104_172457_sym_k2.jpg', 255*phaseSym)

elif inp == 'ps':
    import phasesym as ps
    phaseSym, orientation, totalEnergy, T = phasesym(img, nscale=5, norient=6, minWaveLength=3, mult=2.1, sigmaOnf=0.55, k=2., polarity=0, noiseMethod=-1)
    

elif inp == 'pcm':
    import phasecongmono as pcm
    k = 1
    image = cv2.rotate(img, cv2.ROTATE_180)
    
    M, ori, ft, T = pcm.phasecongmono(image, nscale=5, minWaveLength=3, mult=2.1, sigmaOnf=0.55, k=k, cutOff=0.5, g=10., noiseMethod=-1, deviationGain=1.5)
    imshow(M)
    cv2.imwrite('IMG_20221104_172457_k0.jpg', 255*M)

elif inp == 'pc':
    import phasecong as pc
    M, m, ori, ft, PC, EO, T = phasecong(img, nscale=5, norient=6, minWaveLength=3, mult=2.1, sigmaOnf=0.55, k=2., cutOff=0.5, g=10., noiseMethod=-1)

else:
    raise Exception('Wrong Choice.')



#imshow(ori)
#imshow(ft)





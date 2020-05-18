import numpy as np
import cv2
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QFileDialog, QAction
from PyQt5.QtGui import QIcon, QPixmap

class Image_Comp:

    def __init__(self,imagePath):
        self.img = cv2.imread(imagePath,0)
        #self.img_arr = np.asarray(self.img)
        self.fourier = np.fft.fft2(self.img)
        #self.fourier_shift = np.fft.fftshift(self.fourier)
        self.ft_abs = np.abs(self.fourier)
        self.ft_Mag = np.log10(self.ft_abs)
        self.ft_phase = np.angle(self.fourier)
        self.ft_real = np.real(self.fourier)
        self.ft_imag = np.imag(self.fourier)
        self.ft_uniform_Mag = np.where(self.ft_Mag , 1 , self.ft_Mag)
        self.ft_uniform_phase = np.where(self.ft_phase,0,self.ft_phase)
        

    
     

 
############## for testing ############### 
""" fig = plt.figure()
ax1 = fig.add_subplot(331)
ax2 = fig.add_subplot(332)
ax3 = fig.add_subplot(333)
ax4 = fig.add_subplot(334)
ax5 = fig.add_subplot(335)
ax6 = fig.add_subplot(336)
ax7 = fig.add_subplot(337)

ax1.imshow(img1.img, cmap='gray')
ax2.imshow(img1.ft_Mag, cmap='gray')
ax3.imshow(img1.ft_phase, cmap='gray')
ax4.imshow(img1.ft_real, cmap='gray')
ax5.imshow(img1.ft_imag, cmap='gray')
ax6.imshow(img1.ft_uniform_Mag, cmap='gray')
ax7.imshow(img1.ft_uniform_phase, cmap='gray')
plt.show() """




  
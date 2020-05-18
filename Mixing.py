from image import *
import math
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QFileDialog, QAction
from PyQt5.QtGui import QIcon, QPixmap
import numpy as np

class mixer:
    def __init__(self,imagePath1,imagePath2,slider1_val,slider2_val , curr_img_comp1 , curr_img_comp2):
        self.img_one = Image_Comp(imagePath1)
        self.img_two = Image_Comp(imagePath2)
        self.w1 = slider1_val
        self.w2 =slider2_val
        self.curr_img1 = curr_img_comp1
        self.curr_img2 = curr_img_comp2
        ########case 1 comp 1 from image 1 , comp 2 from image 2#############
        if self.curr_img1 == 0  and  self.curr_img2 == 1:
            self.mix1_f = (self.w1*(self.img_one.ft_abs)+(1-self.w1)*(self.img_two.ft_abs))*np.exp((self.w2*(self.img_two.ft_phase)+(1-self.w2)*(self.img_one.ft_phase))*1j)
            self.mix1_f_inv=np.fft.ifft2(self.mix1_f)
            self.mix1_real = np.real(self.mix1_f_inv)
            self.mix2_f = (self.w1*(self.img_one.ft_real)+(1-self.w1)*(self.img_two.ft_real))+(1j*(self.w2*(self.img_two.ft_imag)+(1-self.w2)*(self.img_one.ft_imag)))
            self.mix2_f_inv=np.fft.ifft2(self.mix2_f)
            self.mix2_real = np.real(self.mix2_f_inv)
            self.mix3_f = (self.w1*(self.img_one.ft_abs)+(1-self.w1)*(self.img_two.ft_abs))*np.exp(1j*(self.w2*(self.img_two.ft_uniform_phase)+(1-self.w2)*(self.img_one.ft_uniform_phase)))
            self.mix3_f_inv=np.fft.ifft2(self.mix3_f)
            self.mix3_real = np.real(self.mix3_f_inv)
            self.mix4_f = (self.w1*(self.img_one.ft_phase)+(1-self.w1)*(self.img_two.ft_phase))*np.exp(1j*(self.w2*(self.img_two.ft_uniform_Mag)+(1-self.w2)*(self.img_one.ft_uniform_Mag)))
            self.mix4_f_inv=np.fft.ifft2(self.mix4_f)
            self.mix4_real = np.real(self.mix4_f_inv)
        elif self.curr_img1 == 1  and  self.curr_img2 == 0:    ################case 2 comp1 from image 2 , comp 2 from image 1###################
            self.mix1_f = (self.w1*(self.img_two.ft_abs)+(1-self.w1)*(self.img_one.ft_abs))*np.exp((self.w2*(self.img_one.ft_phase)+(1-self.w2)*(self.img_two.ft_phase))*1j)
            self.mix1_f_inv=np.fft.ifft2(self.mix1_f)
            self.mix1_real = np.real(self.mix1_f_inv)
            self.mix2_f = (self.w1*(self.img_two.ft_real)+(1-self.w1)*(self.img_one.ft_real))+(1j*(self.w2*(self.img_one.ft_imag)+(1-self.w2)*(self.img_two.ft_imag)))
            self.mix2_f_inv=np.fft.ifft2(self.mix2_f)
            self.mix2_real = np.real(self.mix2_f_inv)
            self.mix3_f = (self.w1*(self.img_two.ft_abs)+(1-self.w1)*(self.img_one.ft_abs))*np.exp(1j*(self.w2*(self.img_one.ft_uniform_phase)+(1-self.w2)*(self.img_two.ft_uniform_phase)))
            self.mix3_f_inv=np.fft.ifft2(self.mix3_f)
            self.mix3_real = np.real(self.mix3_f_inv)
            self.mix4_f = (self.w1*(self.img_two.ft_phase)+(1-self.w1)*(self.img_one.ft_phase))*np.exp(1j*(self.w2*(self.img_one.ft_uniform_Mag)+(1-self.w2)*(self.img_two.ft_uniform_Mag)))
            self.mix4_f_inv=np.fft.ifft2(self.mix4_f)
            self.mix4_real = np.real(self.mix4_f_inv)
        elif self.curr_img1 == 0  and  self.curr_img2 == 0:    ################case 3 comp1 from image 1 , comp 2 from image 1###################
            self.mix1_f = (self.w1*(self.img_one.ft_abs)+(1-self.w1)*(self.img_two.ft_abs))*np.exp((self.w2*(self.img_one.ft_phase)+(1-self.w2)*(self.img_two.ft_phase))*1j)
            self.mix1_f_inv=np.fft.ifft2(self.mix1_f)
            self.mix1_real = np.real(self.mix1_f_inv)
            self.mix2_f = (self.w1*(self.img_one.ft_real)+(1-self.w1)*(self.img_two.ft_real))+(1j*(self.w2*(self.img_one.ft_imag)+(1-self.w2)*(self.img_two.ft_imag)))
            self.mix2_f_inv=np.fft.ifft2(self.mix2_f)
            self.mix2_real = np.real(self.mix2_f_inv)
            self.mix3_f = (self.w1*(self.img_one.ft_abs)+(1-self.w1)*(self.img_two.ft_abs))*np.exp(1j*(self.w2*(self.img_one.ft_uniform_phase)+(1-self.w2)*(self.img_two.ft_uniform_phase)))
            self.mix3_f_inv=np.fft.ifft2(self.mix3_f)
            self.mix3_real = np.real(self.mix3_f_inv)
            self.mix4_f = (self.w1*(self.img_one.ft_phase)+(1-self.w1)*(self.img_two.ft_phase))*np.exp(1j*(self.w2*(self.img_one.ft_uniform_Mag)+(1-self.w2)*(self.img_two.ft_uniform_Mag)))
            self.mix4_f_inv=np.fft.ifft2(self.mix4_f)
            self.mix4_real = np.real(self.mix4_f_inv)
        elif self.curr_img1 == 1  and  self.curr_img2 == 1:     ################case 4 comp1 from image 2 , comp 2 from image 2###################
            self.mix1_f = (self.w1*(self.img_two.ft_abs)+(1-self.w1)*(self.img_one.ft_abs))*np.exp((self.w2*(self.img_two.ft_phase)+(1-self.w2)*(self.img_one.ft_phase))*1j)
            self.mix1_f_inv=np.fft.ifft2(self.mix1_f)
            self.mix1_real = np.real(self.mix1_f_inv)
            self.mix2_f = (self.w1*(self.img_two.ft_real)+(1-self.w1)*(self.img_one.ft_real))+(1j*(self.w2*(self.img_two.ft_imag)+(1-self.w2)*(self.img_one.ft_imag)))
            self.mix2_f_inv=np.fft.ifft2(self.mix2_f)
            self.mix2_real = np.real(self.mix2_f_inv)
            self.mix3_f = (self.w1*(self.img_two.ft_abs)+(1-self.w1)*(self.img_one.ft_abs))*np.exp(1j*(self.w2*(self.img_two.ft_uniform_phase)+(1-self.w2)*(self.img_one.ft_uniform_phase)))
            self.mix3_f_inv=np.fft.ifft2(self.mix3_f)
            self.mix3_real = np.real(self.mix3_f_inv)
            self.mix4_f = (self.w1*(self.img_two.ft_phase)+(1-self.w1)*(self.img_one.ft_phase))*np.exp(1j*(self.w2*(self.img_two.ft_uniform_Mag)+(1-self.w2)*(self.img_one.ft_uniform_Mag)))
            self.mix4_f_inv=np.fft.ifft2(self.mix4_f)
            self.mix4_real = np.real(self.mix4_f_inv)    

    
        

        
        

       
        
        



from PyQt5 import QtWidgets
from Gui import Ui_MainWindow
from image import *
from Mixing import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QFileDialog, QAction , QComboBox ,QMessageBox
from PyQt5.QtGui import QIcon, QPixmap ,QImage
import pyqtgraph as pg
from pyqtgraph import ImageView
#import logging
import cv2
import numpy as np
import sys
import logging

logging.basicConfig(filename="test.log",level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')



class ApplicationWindow(QtWidgets.QMainWindow):
    w1 = 0
    w2 = 0
    curr_img_comp1 =0
    curr_img_comp2=0
    curr_comp1 =0
    curr_comp2 =0
    curr_index_out = 0

  
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ######### Open Images ##################
        l1 = [self.ui.actionOpen_Img1,self.ui.actionOpen_Img2]
        l2 = [self.openImage1,self.openImage2]
        for i in range(len(l1)):
            l1[i].triggered.connect(l2[i])
        #########combo Box ############
        
        l3=[self.ui.img1_comp,self.ui.img2_comp,self.ui.comboBox_out,  self.ui.comboBox1_img,self.ui.comboBox2_img,self.ui.comboBox_comp1,self.ui.comboBox_comp2,self.ui.comboBox_comp1]
        l4=[self.view_comp1,self.view_comp2,  self.view_out,self.comp1_img,self.comp2_img,self.comp1_data,self.comp2_data,self.disable_comboBox]
        for i in range (len(l3)):
            l3[i].currentIndexChanged.connect(l4[i])
        ########################## slider ###################
        self.ui.Slider1.valueChanged[int].connect(self.slider1)
        self.ui.slider2.valueChanged[int].connect(self.slider2)
        ###############remove items #######################
       
        
        
    
    def openImage1(self):
        filename = QFileDialog.getOpenFileName(self)
        if filename[0]:
                self.imagePath1 = filename[0]
                self.ViewImage1(self.imagePath1)
        logging.info('User start to choose image 1')       

    def ViewImage1(self,imagePath1):
        self.img1 = Image_Comp(imagePath1)
        self.ui.view_img1.show()
        self.ui.view_img1.setImage(self.img1.img.T )
     

    def openImage2(self):
        filename = QFileDialog.getOpenFileName(self)
        if filename[0]:
                self.imagePath2 = filename[0]
                self.ViewImage2(self.imagePath2) 
        logging.info('User start to choose image 2')

    def ViewImage2(self,imagePath2):
        self.img2 = Image_Comp(imagePath2)
        if self.img2.img.shape != self.img1.img.shape:
            error_message = QMessageBox()
            error_message.setIcon(QMessageBox.Critical)
            error_message.setText("Please, Enter Image Two of size same as image One which is : {}".format(self.img1.img.shape))
            error_message.setWindowTitle("Error")
            error_message.exec_()
            logging.error("user enter image of wrong size")
        else:
            self.ui.view_img2.show()
            self.ui.view_img2.setImage(self.img2.img.T)
           


    def view_comp1(self):
        self.curr_index = self.ui.img1_comp.currentIndex() 
        if self.curr_index == 1 : 
            self.ui.view_comp1.show()
            self.ui.view_comp1.setImage(self.img1.ft_Mag.T)
        elif self.curr_index == 2 :
            self.ui.view_comp1.show()
            self.ui.view_comp1.setImage(self.img1.ft_phase.T)
        elif self.curr_index == 3 :
            self.ui.view_comp1.show()
            self.ui.view_comp1.setImage(self.img1.ft_real.T)
        elif self.curr_index == 4 :
            self.ui.view_comp1.show()
            self.ui.view_comp1.setImage(self.img1.ft_imag.T)
        elif self.curr_index == 5 :
            self.ui.view_comp1.show()
            self.ui.view_comp1.setImage(self.img1.ft_uniform_Mag.T)
        elif self.curr_index == 6 :
            self.ui.view_comp1.show()
            self.ui.view_comp1.setImage(self.img1.ft_uniform_phase.T)
        logging.info("user select a component from image 1")

    def view_comp2(self):
        self.curr_index = self.ui.img2_comp.currentIndex()
        print(self.curr_index)
        if self.curr_index == 1 :
            self.ui.view_comp2.show()
            self.ui.view_comp2.setImage(self.img2.ft_Mag.T)
        elif self.curr_index == 2 :
            self.ui.view_comp2.show
            self.ui.view_comp2.setImage(self.img2.ft_phase.T)
        elif self.curr_index == 3 :
            self.ui.view_comp2.show()
            self.ui.view_comp2.setImage(self.img2.ft_real.T)
        elif self.curr_index == 4 :
            self.ui.view_comp2.show()
            self.ui.view_comp2.setImage(self.img2.ft_imag.T)
        elif self.curr_index == 5 :
            self.ui.view_comp2.show()
            self.ui.view_comp2.setImage(self.img2.ft_uniform_Mag.T)
        elif self.curr_index == 6 :
            self.ui.view_comp2.show()
            self.ui.view_comp2.setImage(self.img2.ft_uniform_phase.T)
        logging.info("user select a component from image 2")
    
    def disable_comboBox(self):
        curr_comp1 = self.ui.comboBox_comp1.currentIndex()
        if curr_comp1 == 0 :
            self.ui.comboBox_comp2.clear()
            items = ["Phase","Uniform Phase"]
            for i in items :
                self.ui.comboBox_comp2.addItem(i)
        elif curr_comp1 == 1:
            self.ui.comboBox_comp2.clear()
            items = ["Magnitude","Uniform Magnitude"]
            for i in items :
                self.ui.comboBox_comp2.addItem(i)
        elif curr_comp1 == 2:
            self.ui.comboBox_comp2.clear()
            items = ["Imaginary"]
            for i in items :
                self.ui.comboBox_comp2.addItem(i)

        
    def comp1_img(self):
        self.curr_img_comp1 = self.ui.comboBox1_img.currentIndex()
   

    def comp1_data(self):
        self.curr_comp1 = self.ui.comboBox_comp1.currentIndex()
        
    def slider1 (self,value):
        self.w1 = value/100 
        self.mixing() 
        logging.info("user ready to view mixing outputs")
  
#####################################
    def comp2_img(self):
        self.curr_img_comp2 = self.ui.comboBox2_img.currentIndex()
        
    def comp2_data(self):
        self.curr_comp2 = self.ui.comboBox_comp2.currentIndex()

    def slider2(self,value):
        self.w2 = value/100 
        self.mixing() 
        logging.info("user ready to view mixing outputs")
  ###################################### 
    def view_out(self):
        self.curr_index_out = self.ui.comboBox_out.currentIndex()
        
            ########################################           
    def mixing(self):
        self.mix1 = mixer(self.imagePath1,self.imagePath2,self.w1,self.w2 , self.curr_img_comp1 , self.curr_img_comp2)
        if self.curr_comp1 == 0  and self.curr_comp2 == 0:
                if self.curr_index_out == 0 :
                    self.ui.view_out1.show()
                    self.ui.view_out1.setImage(self.mix1.mix1_real.T)
                    logging.info('user mix {} of Magnitude in image {} and {} of phase in image {} on output 1'.format(self.w1,self.curr_img_comp1,self.w2,self.curr_img_comp2))
                elif self.curr_index_out == 1 :
                    self.ui.view_out2.show()
                    self.ui.view_out2.setImage(self.mix1.mix1_real.T)
                    logging.info('user mix {} of Magnitude in image {} and {} of phase in image {} on output 2'.format(self.w1,self.curr_img_comp1,self.w2,self.curr_img_comp2))
        elif self.curr_comp1 == 2  and self.curr_comp2 == 0:
                if self.curr_index_out == 0 :
                    self.ui.view_out1.show()
                    self.ui.view_out1.setImage(self.mix1.mix2_real.T)
                    logging.info('user mix {} of Real in image {} and {} of Imaginary in image {} on output 1'.format(self.w1,self.curr_img_comp1,self.w2,self.curr_img_comp2))
                elif self.curr_index_out == 1 :
                    self.ui.view_out2.show()
                    self.ui.view_out2.setImage(self.mix1.mix2_real.T) 
                    logging.info('user mix {} of Real in image {} and {} of Imaginary in image {} on output 2'.format(self.w1,self.curr_img_comp1,self.w2,self.curr_img_comp2))
        elif self.curr_comp1 == 0  and self.curr_comp2 == 1:
                if self.curr_index_out == 0 :
                    self.ui.view_out1.show()
                    self.ui.view_out1.setImage(self.mix1.mix3_real.T)
                    logging.info('user mix {} of Magnitude in image {} and {} of Uniform Phase in image {} on output 1'.format(self.w1,self.curr_img_comp1,self.w2,self.curr_img_comp2))
                elif self.curr_index_out == 1 :
                    self.ui.view_out2.show()
                    self.ui.view_out2.setImage(self.mix1.mix3_real.T) 
                    logging.info('user mix {} of Magnitude in image {} and {} of Uniform Phase in image {} on output 2'.format(self.w1,self.curr_img_comp1,self.w2,self.curr_img_comp2))
        elif self.curr_comp1 == 1  and self.curr_comp2 == 1:
                if self.curr_index_out == 0 :
                    self.ui.view_out1.show()
                    self.ui.view_out1.setImage(self.mix1.mix4_real.T)
                    logging.info('user mix {} of Phase in image {} and {} of Uniform Magnitude in image {} on output 1'.format(self.w1,self.curr_img_comp1,self.w2,self.curr_img_comp2))
                elif self.curr_index_out == 1 :
                    self.ui.view_out2.show()
                    self.ui.view_out2.setImage(self.mix1.mix4_real.T)
                    logging.info('user mix {} of Phase in image {} and {} of Uniform Magnitude in image {} on output 2'.format(self.w1,self.curr_img_comp1,self.w2,self.curr_img_comp2))
            
 
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main() 
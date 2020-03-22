# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np


if __name__=="__main__":
    
    GaussOne = np.array([[1,2,1],
                         [2,4,2],
                         [1,2,1]])
    GaussOne = np.true_divide(GaussOne, 16)
    
    GaussTwo = np.array([[1,4,7,4,1],
                         [4,16,26,16,4],
                         [7,26,41,26,7],
                         [4,16,26,16,4],
                         [1,4,7,4,1]])
    GaussTwo = np.true_divide(GaussTwo, 273)
    
    GaussThree = np.array([[0,0,1,2,1,0,0],
                           [0,3,13,22,13,3,0],
                           [1,13,59,97,59,13,1],
                           [2,22,97,159,97,22,2],
                           [1,13,59,97,59,13,1],
                           [0,3,13,22,13,3,0],
                           [0,0,1,2,1,0,0]])
    GaussThree = np.true_divide(GaussThree, 1003)
    
    PrewittVert = np.array([[-1,0,1],
                            [-1,0,1],
                            [-1,0,1]])
    
    PrewittHor = np.array([[1,1,1],
                           [0,0,0],
                           [-1,-1,-1,]])

    
    kernels = (
        ("GaussOne", GaussOne),
        ("GaussTwo", GaussTwo),
        ("GaussThree", GaussThree),
        ("PrewittVert", PrewittVert),
        ("PrewittHor", PrewittHor),
        )
    
    img = cv2.imread(r"C:\Users\bentw\Desktop\InputIMG.JPG")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    
    
    blur1 = cv2.GaussianBlur(img, (3,3),10)
    cv2.imwrite(r"C:\Users\bentw\Desktop\Blur1.JPG", blur1)
    
    blur2 = cv2.GaussianBlur(img, (5,5),10)
    cv2.imwrite(r"C:\Users\bentw\Desktop\Blur2.JPG", blur2)

    blur3 = cv2.GaussianBlur(img, (11,11),10)
    cv2.imwrite(r"C:\Users\bentw\Desktop\Blur3.JPG", blur3)
    
    blur4 = cv2.GaussianBlur(img, (15,15),10)
    cv2.imwrite(r"C:\Users\bentw\Desktop\Blur4.JPG", blur4)

    blur5 = cv2.GaussianBlur(img, (23,23),10)
    cv2.imwrite(r"C:\Users\bentw\Desktop\Blur5.JPG", blur5)
    
    
    
    
    prew = cv2.filter2D(blur1, -1, PrewittHor)
    cv2.imwrite(r"C:\Users\bentw\Desktop\Guass HW\b1Hor.JPG", prew)
    
    prew = cv2.filter2D(blur2, -1, PrewittHor)
    cv2.imwrite(r"C:\Users\bentw\Desktop\Guass HW\b2Hor.JPG", prew)
    
    prew = cv2.filter2D(blur3, -1, PrewittHor)
    cv2.imwrite(r"C:\Users\bentw\Desktop\Guass HW\b3Hor.JPG", prew)
    
    prew = cv2.filter2D(blur4, -1, PrewittHor)
    cv2.imwrite(r"C:\Users\bentw\Desktop\Guass HW\b4Hor.JPG", prew)
    
    prew = cv2.filter2D(blur5, -1, PrewittHor)
    cv2.imwrite(r"C:\Users\bentw\Desktop\Guass HW\b5Hor.JPG", prew)
    
    
    
    
    prew = cv2.filter2D(blur1, -1, PrewittVert)
    cv2.imwrite(r"C:\Users\bentw\Desktop\Guass HW\b1Vert.JPG", prew)
    
    prew = cv2.filter2D(blur2, -1, PrewittVert)
    cv2.imwrite(r"C:\Users\bentw\Desktop\Guass HW\b2Vert.JPG", prew)
    
    prew = cv2.filter2D(blur3, -1, PrewittVert)
    cv2.imwrite(r"C:\Users\bentw\Desktop\Guass HW\b3Vert.JPG", prew)
    
    prew = cv2.filter2D(blur4, -1, PrewittVert)
    cv2.imwrite(r"C:\Users\bentw\Desktop\Guass HW\b4Vert.JPG", prew)
    
    prew = cv2.filter2D(blur5, -1, PrewittVert)
    cv2.imwrite(r"C:\Users\bentw\Desktop\Guass HW\b5Vert.JPG", prew)
    
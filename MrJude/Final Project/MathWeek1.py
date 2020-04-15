# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 10:15:17 2020

@author: Clarissa
"""
import numpy as np

#Python Numpy Notes

#Creating special arrays
x = np.array ([1, 2, 3]) #x = [1, 2, 3]
x = np.array ([ [1], [2], [3] ]) #creates a 3x1 matrix

#Check dimensions 
#Check shape
A = np.array ([ [1,2,3],[4,5,6] ]) #creates a 2x3 matrix 
A.ndim #2
A.shape #(2,3)

A= np.array([1,2,3])
A.ndim #1
A.shape #(1,3)

A = np.zeros( (2,3) ) # creates matrix 2x3 contains all 0

A = np.ones ( (2,3) ) #creates matrix 2x3 contains all 1
A = np.diag( [1.0, 2.0] ) #Creates a diagonal matrix containing 1 and 2 
# 1 0
# 0 2
#%%
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print (a)
#[[ 1  2 3  4  5  6  7]]
# [8  9 10 11 12 13 14]]

#Get specific element [r,c]
a[1,5] #13

#Get specific row 
a[0, :]
#Get specific column
a[:,2]

#changing value 
a[1,5] = 20
#[[ 1  2 3  4  5  6  7]]
# [8  9 10 11 12 20 14]]

x = np.arange (1,6,2) #x = [1,3,5]
x = np.linspace(0,1,5) #x = [0.0, 0.25, 0.50, 0.75, 1]

#Indexing and SLicing 

x = [2, 3, 4, 5, 6]
#x[0] = 2
#x[-1] = 6
#x[1:-1:2] = 3,5 
#x[::-1]= 6,5,4,3,2
#x[0:-1:2]= 2,4 

#%%
np.reshape() #reshape a matrix
np.flatten() #flatten a matrix

#%%
#3-d arrays 
b = np.array([[[1,2], [3,4]], [[5,6],[7,8]]])
#[[[1 2]
  #[3 4]]
  
  #[[5 6]
  #[7 8]]]

#get a specific element 
b[0,1,1] #4 
b[0,1,0] #3 
b[1,1,0] #7 
b[:,1,:]
#([[3, 4],
       #[7, 8]])

#replace
b[:,1,:] = [[8,9], [10,11]]
#([[[ 1,  2],
        #[ 8,  9]],

       #[[ 5,  6],
        #[10, 11]]])

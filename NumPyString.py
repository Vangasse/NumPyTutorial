# %%
import numpy as np
import pandas as pd
import matplotlib.image as img 
import matplotlib.pyplot as plt

# %% Repeat all the elements of a NumPy array of strings
a = np.array(['Salvem', 'as', 'baleias'], dtype = np.str) 
print(np.char.multiply(a, 2)) 
# %% How to split the element of a given NumPy array with spaces?
a = np.array(['Salvem as baleias'], dtype = np.str) 
print(np.char.split(a)) 
# %% How to insert a space between characters of all the elements of a given NumPy array?
a = np.array(['Salvem', 'as', 'baleias'], dtype = np.str) 
print(np.char.join(" ", a))
# %% Find the length of each string element in the Numpy array
a = np.array(['Salvem', 'as', 'baleias'], dtype = np.str)
length = np.vectorize(len)
print(length(a))
# %% Swap the case of an array of string
a = np.array(['SaLvEm', 'As', 'BaLeIaS'], dtype = np.str)
print(np.char.swapcase(a))
# %% Change the case to uppercase of elements of an array
a = np.array(['SaLvEm', 'As', 'BaLeIaS'], dtype = np.str)
print(np.char.upper(a))
# %% Change the case to lowercase of elements of an array
a = np.array(['SaLvEm', 'As', 'BaLeIaS'], dtype = np.str)
print(np.char.lower(a))
# %% Join String by a seperator
a = np.array(['SaLvEm', 'As', 'BaLeIaS'], dtype = np.str)
print(np.char.join('-', a))
# %% Check if two same shaped string arrayss one by one
a = np.array(['Salvem', 'as', 'baleias'], dtype = np.str) 
b = np.array(['Cuidem', 'das', 'baleias'], dtype = np.str) 
print(np.char.equal(a, b))
# %% Count the number of substrings in an array
a = np.array(['Salvem', 'as', 'baleias'], dtype = np.str) 
print(np.char.count(a, sub='al'))
# %% Find the lowest index of the substring in an array
a = np.array(['Salvem', 'as', 'baleias'], dtype = np.str) 
print(np.char.find(a, sub='al'))
# %% Get the boolean array when values end with a particular character
a = np.array(['Salvem', 'as', 'baleias'], dtype = np.str) 
print(np.char.endswith(a, 'as'))
# %% Different ways to convert a Python dictionary to a NumPy array
a = {1: 'Salvem', 2: 'as', 3: 'Baleias'}
print(np.array(list(a.items())))
# %% How to convert a list and tuple into NumPy arrays?
a = ['Save', 'the', 'whales']
b = ('Save', 'the', 'whales')
print(np.array(a))
print(np.array(b))
# %% Ways to convert array of strings to array of floats
a = np.array(['1.1', '1.2', '1.3'])
print(a.astype(np.float))
# %% Convert a NumPy array into a csv file
a = np.arange(9).reshape([3, 3])
DF = pd.DataFrame(a)
DF.to_csv("data.csv")
# %% How to Convert an image to NumPy array and save it to CSV file using Python?
# read an image 
imageMat = img.imread('rafiki.jpg') 
print("Image shape:",  
      imageMat.shape) 
  
# if image is colored (RGB) 
if(imageMat.shape[2] == 3): 
    
  # reshape it from 3D matrice to 2D matrice 
  imageMat_reshape = imageMat.reshape(imageMat.shape[0], 
                                      -1) 
  print("Reshaping to 2D array:",  
        imageMat_reshape.shape) 
  
# if image is grayscale 
else: 
  # remain as it is 
  imageMat_reshape = imageMat 
      
# converting it to dataframe. 
mat_df = pd.DataFrame(imageMat_reshape) 
  
# exporting dataframe to CSV file. 
mat_df.to_csv('rafikifile.csv', 
              header = None, 
              index = None) 
  
# retrieving dataframe from CSV file 
loaded_df = pd.read_csv('rafikifile.csv',  
                        sep = ',', 
                        header = None) 
# getting matrice values. 
loaded_2D_mat = loaded_df.values 
  
# reshaping it to 3D matrice 
loaded_mat = loaded_2D_mat.reshape(loaded_2D_mat.shape[0], 
                                   loaded_2D_mat.shape[1] // imageMat.shape[2], 
                                   imageMat.shape[2]) 
  
print("Image shape of loaded Image :", 
      loaded_mat.shape) 
  
# check if both matrice have same shape or not 
if((imageMat == loaded_mat).all()): 
  print("\n\nYes", 
        "The loaded matrice from CSV file is same as original image matrice")
# %% How to save a NumPy array to a text file?
a = np.arange(9)
file = open("file.txt", "w+")
content = str(a)
file.write(content)
file.close()

# %% Load data from a text file
file = open("file.txt", "r") 
content = file.read()

print(content)
file.close()
# %% Plot line graph from NumPy array
x = np.arange(100)
y = x

plt.title("Line graph")  
plt.xlabel("X axis")  
plt.ylabel("Y axis")  
plt.plot(x, y, color ="blue")  
plt.show()
# %% 

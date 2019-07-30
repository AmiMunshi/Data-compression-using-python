
# coding: utf-8

# In[52]:

import sys
import numpy as np
string1= "and or and with or not go for and not got for with and for go on there" ## Enter the string to be compressed


list1= string1.split() #separate individual words in the string

dict1={} ## create dictionary to store the word in the list as key and iths freuquency as value

for i in list1:
    count= list1.count(i) #count frequency of occurence of word in the list
    temp= {i:count} 
    dict1.update(temp) # update the dictionary with word and its frequency

a= np.array(dict1)
print(a)

k=0
dict2={} # create one more dictionary to store word and its corresponding index
for key1 in dict1:
    k= k+1
    temp = {key1:k}
    dict2.update(temp)
print("\n The dictionary with word and its corresponding index is:\n")
print(dict2)
list2=[]
##output the index of the word in the list to obtain compressed text
for p in range(len(list1)):
    for j in dict2:
        if j== list1[p]:
            list2.append(dict2[j])
print("\nThe compressed sequence is ")
print(list2)


# In[28]:

## To find size of original string and the compressed string

coded_original= []
for k in range(len(string1)):
    coded_original.append(bin(ord(string1[k]))[2:])
print("\n The original encoded string is:\n")
print(coded1)
print('\nThe size of encoded string is:'+str(sys.getsizeof(coded_original)) +' bytes\n')

coded_compressed=[]
for n in list2:
    x= bin(n)[2:]
    coded_compressed.append(x)

print("\n The compressed encoded string is:\n")
print(coded_compressed)
print('\nThe size of encoded string is:'+str(sys.getsizeof(coded_compressed)) +' bytes')


# In[50]:

##To find compression ratio
Original_size= float(sys.getsizeof(coded_original))
Compressed_size=float(sys.getsizeof(coded_compressed))
CR= round(float(Original_size/Compressed_size),3)
print('The compression ratio is:'+str(CR))


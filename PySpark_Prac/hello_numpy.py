import numpy as np

array = np.array([1,2,3,4])*2
# print(array.ndim)

array_2 = np.array([[['A','B','C'], ['D','E','F'], ['G','H','I']],
                    [['J','K','L'], ['M','N','O'], ['P','Q','R']],
                    [['S','T','U'], ['V','W','X'], ['Y','Z','I']]])
# print(array_2.ndim)
# print(array_2.shape)
# print(array_2[2,2,1])
word = array_2[2,0,0]+array_2[0,0,0]+array_2[1,1,1]
# print(word)
# print(array_2[2])

array_num = np.array([[1,2,3,10],
                      [4,5,6,11],
                      [7,8,9,12]
                      ])
# print(array_num[1])
# print(array_num[-1])
# print(array_num[0:1])
# print(array_num[::-1])
# print(array_num[:, 1])
# print(array_num[:, -2])
# print(array_num[:, 1:3])
# print(array_num[:, ::2])
# print(array_num[:, ::-3])
# print(array_num[0:2, 0:2])
# print(array_num[1:3, 1:4])
# print(array_num[0:3, 1:3])
# print(array_num[1:, 0:])

add_array = np.array([1,2,3,4])
print(add_array+1)
print(add_array-1)
print(add_array*3)
print(add_array/4)
print(add_array**5)

num_add = [1.01, 2.6, 3.99]
#Vectorized math funcs
print(np.sqrt(add_array))
print(np.round(num_add))
print(np.floor(num_add))
print(np.ceil(num_add))

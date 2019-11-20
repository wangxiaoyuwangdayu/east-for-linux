'''
created at 2019.11.20 14:31
authored @Jiayu Wang
for test script usage
'''
import numpy as np

# score = np.array([[7, 8, 9],
#                   [4, 5, 6],
#                   [1, 2, 3]])
# xy_text = np.argwhere(score > 2)
# print(xy_text)
# xy_text = xy_text[np.argsort(xy_text[:, 0])]
# print(xy_text)
# print(xy_text[:, ::-1])

a = np.array([[1,2,3,4,5,6], [3,4,5,6,7,8]])
print(a.shape)
b = a[:, np.newaxis, :]
print(b.shape)
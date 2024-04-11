import numpy as np

lst = [k for k in range(1, 9)]

for i in range(1, len(lst) + 1):
    if len(lst) % i == 0:
        reshaped_array = np.reshape(lst, (i, -1))
        print(f"{i}x{len(lst)//i}:")
        print(reshaped_array)
        print()

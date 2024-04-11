import numpy as np

lst = [k for k in range(1, 9)]
size = len(lst)

ary = np.array(lst)
for r in range(1, size + 1):
    if size % r == 0:
        print(f"{r}x{size//r}:")
        print(ary.reshape(r, size//r))
  

A = np.arange(1, 10).reshape(9, 1)
B = np.arange(1, 10).reshape(1, 9)
print(A)
C = np.dot(A, B)


row, col = C.shape  # 取得列行的方法。
for r in range(row):
    for c in range(col):
        print(f"{C[r, c]:2}", end=' ')
    print()

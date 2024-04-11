class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar):
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __mod__(self, other):
        cross_x = self.y * other.z - self.z * other.y
        cross_y = self.z * other.x - self.x * other.z
        cross_z = self.x * other.y - self.y * other.x
        return Vector3(cross_x, cross_y, cross_z)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def show(self):
        print(f"<{self.x}, {self.y}, {self.z}>")

# 資料設定
vec_1 = Vector3(1, 2, 3)
vec_2 = Vector3(6, 5, 4)

# 運算
result1 = vec_1 + vec_2
result2 = 2 * vec_1 - vec_2 * 3
result3 = vec_1.dot(vec_2)
A = vec_1 % vec_2
B = vec_2 % vec_1
result4 = A + B

# 顯示結果
print("vec_1 + vec_2 =>", end=" ")
result1.show()
print("2 * vec_1 - vec_2 * 3 =>", end=" ")
result2.show()
print("vec_1.dot(vec_2) =>", result3)
print("A, B, A + B =>", end=" ")
A.show()
B.show()
result4.show()

## 題目：2
請先寫一個 Triangle 類別，包含下列函式:
```python=
class Triangle:
    def __init__(self, a, b, c):  # 你可以在此判斷 a, b, c 是否可構成一個三角形。
        pass
        
    # 形成合法三角形的規則: 任兩邊和 大於 第三邊！       
    def check(self):
        return True or False 並告知是否能構成一個三角形。
        
    def area(self):  # 可以使用 Heron's formula。
        return area_value
    
    def perimeter(self):
        return perimeter_value
    
    def show(self):  # 顯示這是三角形，及三個邊長的資料。
        pass
```
最後使用下列邊長資料來逐一建構 Triangle 物件，同時將所有合法的三角形列出，並計算這些三角形的面積總和。\
1) 12,  9,  6
2) 10, 10, 10
3)  6,  8, 13
4)  3, 15,  2
5) 10,  8,  4
6)  2,  4,  3
7)  3, 14,  8
8)  6, 12, 12
9) 10, 14, 13

驗證資訊: \
1)上述第 1, 2, 3, 5, 6, 8, 9 項可以構成三角形。\
2)合法三角形的面積總和約為 201.5。 

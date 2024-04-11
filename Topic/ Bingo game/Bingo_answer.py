import random

def generate_bingo(square_size):
    if square_size < 2 or square_size > 9:
        print("請輸入2到9之間的數字！")
        return

    numbers = list(range(1, square_size ** 2 + 1))
    random.shuffle(numbers)

    row_separator = "+----" * square_size + "+"
    row_template = "| {:2} "
    row_end = "|"

    print(row_separator)

    for i in range(square_size):
        row = row_template.format(numbers.pop(0))
        for j in range(1, square_size):
            row += row_template.format(numbers.pop(0))
        row += row_end
        print(row)
        print(row_separator)

square_size = int(input("請輸入每邊的數字個數 (2-9): "))
generate_bingo(square_size)

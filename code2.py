total = 0
counter = 1
whlie counter <= 10:
    grad = int(input("정수입력: "))
    total = grad + total
    counter = counter + 1
aver = total / 10
print(total)
print(aver)
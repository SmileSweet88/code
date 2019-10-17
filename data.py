d1 = [23, 2, 45, 1, 9, 3]
i = 0
print("开始： ", d1)
while i < len(d1):
    j = i + 1
    temp = 0
    while j < len(d1):
        if d1[i] > d1[j]:
            temp = d1[j]
            d1[j] = d1[i]
            d1[i] = temp
        j += 1
    i += 1
print("结束： ", d1)

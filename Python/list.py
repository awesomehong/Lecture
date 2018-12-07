a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num = int(input("숫자를 입력하세요" ))

list = []

for i in a:
    if i < num:
        list.append(i)

print(list)

print([i for i in a if i < num])


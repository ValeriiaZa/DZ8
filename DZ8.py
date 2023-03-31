lst1 = [5, 6, 8, 4, 0, 10]
i = 0
summa = 0
if len(lst1) != 0:
    b = lst1[-1]
else:
    b = []
while i < len(lst1):
    l = lst1[i]
    i += 2
    summa = l + summa
a = b*summa
print(a)








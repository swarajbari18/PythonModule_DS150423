fibonachi_range = int(input('Enter the range upto which you want the fibonachi sequence:   '))
lst = list(range(fibonachi_range+1))
for i in range(fibonachi_range+1):
    if i == 0:
        lst[0] = 0
    elif i == 1:
        lst[1] = 1
    else:
        lst[i] = lst[i-1] + lst[i-2]

for j in lst:
    print(j, end = ' ')
    

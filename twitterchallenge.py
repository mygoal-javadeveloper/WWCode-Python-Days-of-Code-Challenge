# https://x.com/clcoding/status/1772086232983441874?s=20
# https://x.com/NDhoondia/status/1772188043799048417?s=20

def hourglass(hourglasslength : int):
    tempnum = 1
    for num in range(0, hourglasslength):
        if num==0 or num == hourglasslength-1:
           print("*"*hourglasslength)
        elif num < hourglasslength//2:
            print(' '*num, end = '')
            print('*', end = '')
            print(' '*(hourglasslength - ((num+1)*2)), end = '')
            print('*')
        elif num == hourglasslength//2:
            print(' ' * (num), end='')
            print('*')
        elif num > hourglasslength//2:
            print(' '*(hourglasslength - (num+1)), end = '')
            print('*', end = '')
            if num == hourglasslength//2 + 1:
                print(' '*(num-hourglasslength//2), end = '')
            else:
                print(' ' * ((num+tempnum) - hourglasslength // 2), end='')
                tempnum = tempnum + 1
            print('*')

hourglass(3)
hourglass(5)
hourglass(7)
hourglass(9)
hourglass(11)
hourglass(15)

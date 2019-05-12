month = [31,28,31,30,31,30,31,31,30,31,30,31]
a = input("Введите дату рождения дд.мм.гггг ")
#a = '12.03.2020'
a = a.split('.')
for i in range(len(a)):
    a[i] = int(a[i])
b = input("Введите дату исчисляемого дня дд.мм.гггг ")
#b = '29.11.2043'
b = b.split('.')
for i in range(len(b)):
    b[i] = int(b[i])

def OtDr(a,b,month):
    if b[1] == a[1] and b[0] >= a[0]:
        return b[0]-a[0]
    if month[a[1]-1] == 28:
        if a[2] % 4 == 0:
            d = 29 - a[0]
        else:
            d = 28- a[0]
    else:
        d = month[a[1]-1] - a[0]
    m = a[1]
    g = a[2]
    while m!= b[1]-1:
        if m == 12:
            g +=1
            m = 0
        if month[m] == 28:
            if g % 4 == 0:
                d += 29
                m+=1
                
            else:
                d += 28
                m+=1
        else:
            d+=month[m]
            m+=1
    d += b[0]
    return d

def SkokLet(a, b):
    if a[2] == b[2]:
        return 0
    d = 0
    if a[2] % 4 == 0:
        if a[1] >= 3:
            if b[2]%4 == 0:
                d+=366
            else:
                d+=365
        else:
            d+=366
    else:
        d+=365
    g1 = a[2] + 1
    while g1 != b[2]:
        if g1%4 == 0:
            d+=366
        else:
            d+=365
        g1+=1
    return d

print(OtDr(a,b,month)+SkokLet(a, b))

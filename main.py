n = int(input())
st = list(input())
obc = 0
ob = 0
obz = 0
kv = 0
kvz = 0
fi = 0
fiz = 0
check = False
for i in st:
    if ord(i) == 123:
        fi += 1
        obc += 1
    elif ord(i) == 125 and obc > 1 or ord(i) == 125 and fiz == 0:
        chck = True
        break
    elif ord(i) == 125:
        fiz -= 1
        obc -= 1
    elif ord(i) == 1:
        print(True)

        # test
        # test2
        # test 12
        # freature dad
        # feature egor

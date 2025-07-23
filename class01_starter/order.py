#order arhan

x = str(input("โปรดใส่ประเภทสมาชิก (Gold or Silver or none) "))
y = float(input("จำนวนเงินรวมที่สั่งอาหาร "))
z = int(input("วันที่สั่งอาหาร "))


if x == "Gold" :
    if y >= 1000 :
        discout = y * 15 / 100
        y = y - discout
    else :
        discout = y * 10 / 100
        y = y - discout
elif x == "Silver" :
    if x >= 1000 :
        discout = y * 10 / 100
        y = y - discout
    else :
        discout = y * 5 / 100
        y = y - discout
elif x == "none" :
    y = y
else :
    print("error")

if z % 2 == 1 :
    if y >= 500 :
        sum = y * 5 / 100
        final = y - sum
    else :
        final = y
else :
    final = y

if final <= 800 :
    end = final + 50
else :
    end = final

print("ประเภทสมาชิก ",x)
print(end)
print("วันสั่งซื้อ ",z)
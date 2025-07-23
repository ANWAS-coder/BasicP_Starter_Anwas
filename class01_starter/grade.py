#grade kumnuan

x = float(input("โปรดใส่คะแนนที่ต้องการคำนวณ "))

if x >= 50 :
    print("ผ่าน")
    if 51 <= x <= 59 :
        print("เกรด D")
    elif 60 <= x <= 69 :
        print("เกรด C")
    elif 70 <= x <= 79 :
        print("เกรด B")
    else :
        print("เกรด A")
else :
    print("คุณไม่ผ่าน")
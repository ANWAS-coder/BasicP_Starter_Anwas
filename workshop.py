x = float(input("ระยะทางในการขนส่ง = "))
if x < 5 :
    print(x," km")
    print("0 บาท")
    print("ภาษี 0 บาท")
    print("ราคารวม vat ",x," บาท")
elif 5 <= x <= 50 :
    print(x," km")
    print("10 บาท")
    print("ภาษี ",10*7/100," บาท")
    print("ราคารวม vat ",10 + (10 * 7 / 100)," บาท")
elif 51 <= x <= 100 :
    print(x," km")
    print("15 บาท")
    print("ภาษี ",15*7/100," บาท")
    print("ราคารวม vat ",15 + (15 * 7 / 100)," บาท")
elif 101 <= x <= 300 :
    print(x," km")
    print("25 บาท")
    print("ภาษี ",25*7/100," บาท")
    print("ราคารวม vat ",25 + (25 * 7 / 100)," บาท")
elif 301 <= x <= 500 :
    print(x," km")
    print("35 บาท")
    print("ภาษี ",35*7/100," บาท")
    print("ราคารวม vat ",35 + (35 * 7 / 100)," บาท")
elif x > 500 :
    print(x," km")
    print("45 บาท")
    print("ภาษี ",45*7/100," บาท")
    print("ราคารวม vat ",45 + (45 * 7 / 100)," บาท")
else :
    print("error")
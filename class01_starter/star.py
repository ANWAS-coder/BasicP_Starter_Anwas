monsterHP = int(1000)
gun = int(100)
sword = int(200)
punch = int(40)
x = int(input("โปรดเลือกที่จะสู้หรือหนี หากสู้พิมพ์ 1 หากหนีพิมพ์ 2 = "))

if x == 1 :
    fight = int(input("โปรดเลืิอกว่าตีกี่รอบ "))
    for i in range(fight) :
        print("มีอาวุธ gun sword punch")
        weapon = int(input("เลือกที่จะใช้อาวุธที่เท่าไหร่ "))
        if weapon == 1 :
            monsterHP = monsterHP - gun
        elif weapon == 2 :
            monsterHP = monsterHP - sword
        elif weapon == 3 :
            monsterHP = monsterHP - punch
        print(monsterHP)
        if monsterHP < 0 :
            monsterHP = 20
        elif monsterHP == 0 :
            print("you win")
            break    
    if monsterHP > 0 :
        print("you die")
elif x == 2 :
    print("quit")
         



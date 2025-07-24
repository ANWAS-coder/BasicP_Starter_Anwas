
# def grade(x):
#     if x < 50 :
#         print("ไม่ผ่าน")
#     elif x < 60 :
#         print("เกรด D")
#     elif x < 70 :
#         print("เกรด C")
#     elif x < 80 :
#         print("เกรด B")
#     else :
#         print("เกรด A")

# grade(80)
# grade(50)
# grade(49)

# x = int(input("first number "))
# y = int(input("second number "))


# def koon(x , y):
#     for i in range(1,3):
#         x **= y
    
#     print(x)

# koon(2 , 3)

# def plus(x , y):
#     print(f"ผลบวก = {x+y}")

# plus(5,8)

x = int(input("x เท่ากับ "))
y = int(input("y เท่ากับ "))

def koon(x,y):
    for i in range(1,y+1):
        print(f"ผลคูณของ {x} * {i} = {x * i} ") 
        
koon(x,y)
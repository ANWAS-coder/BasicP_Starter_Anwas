
# ฟังก์ชันแสดงรายชื่อหนังทั้งหมดในระบบ
# def show_movies(movie_list):
#     # TODO: วนลูปแสดงชื่อหนังพร้อมราคาตั๋ว
#     for i in movie_list :
#         print(f"{i["movie_name"]} {i["ticket_price"]}")

# print(show_movies(movies))

# ฟังก์ชันตรวจสอบอายุตามข้อจำกัดของหนัง
# def check_age(user_age, age_restriction):
#     # TODO: ถ้า age_restriction เป็น 'G' ให้ผ่านเลย
#     # ถ้าไม่ใช่ ให้ดึงเลขอายุขั้นต่ำมาเปรียบเทียบกับ user_age
    
#     if age_restriction == G :
#         return True
#     elif user_age < age_restriction :
#         return False
#     else :
#         return True



# ฟังก์ชันคำนวณราคาตั๋วโดยขึ้นกับประเภทหนัง
# def calculate_price(base_price, genre):
#     # TODO: ถ้า genre เป็น 'Action' บวกเพิ่ม 50 บาท
#     if genre == "Action" :
#         base_price = base_price + 50
#     else :
#         return base_price
#     # ถ้าไม่ใช่ คืนราคาเดิม

# # ฟังก์ชันสำหรับการซื้อบัตรชมหนัง
# def buy_ticket(movie_list,show_movies):
#     # TODO: 
#     # 1. เรียก show_movies เพื่อแสดงรายชื่อหนัง
#     print(show_movies(movies))

#     # 2. รับค่าตัวเลือกหนังจากผู้ใช้ (1-5)
#     doomovie = input("เลือกหนังที่ต้องการจะดู (1-5)")

#     # 3. รับอายุผู้ใช้
#     user_age = int(input("อายุของคุณ "))

#     # 4. ตรวจสอบอายุผ่าน check_age
#    check_age(user_age,movie_list[doomovie["age_restriction"]])
#     if user_age == False :
#         print("อายุน้อยเกินไป")
#     #    - ถ้าไม่ผ่าน ให้แสดงข้อความว่าอายุน้อยเกินไปและ return ออกจากฟังก์ชัน
#     # 5. ให้ผู้ใช้เลือกเสียงพากย์ (1 = พากย์ไทย, 2 = Soundtrack)
#     print("กรุณาเลือกเสียงพากษ์ 1 = พากย์ไทย, 2 = Soundtrack")
#     sound = str(input())
#     # 6. คำนวณราคาตั๋วโดยใช้ calculate_price
#     finalprice = calculate_price(doomovie["ticket_price"],doomovie["genre"])
#     # 7. แสดงผลการซื้อบัตร พร้อมชื่อหนัง, เสียงที่เลือก, ราคาตั๋ว

def main():
    # TODO: สร้างรายการหนังเป็น list ของ dict โดยเก็บข้อมูล movie_name, ticket_price, genre, age_restriction
    movies = [
        {'movie_name': 'Avengers Endgame', 'ticket_price': 300, 'genre': 'Action', 'age_restriction': '13'},
        {'movie_name': 'Inception', 'ticket_price': 280, 'genre': 'Sci-Fi', 'age_restriction': '13'},
        {'movie_name': 'It', 'ticket_price': 180, 'genre': 'Horror', 'age_restriction': '18'},
        {'movie_name': 'The Notebook', 'ticket_price': 250, 'genre': 'Romantic', 'age_restriction': '13'},
        {'movie_name': 'Harry Potter and the Sorcerer\'s Stone', 'ticket_price': 260, 'genre': 'Fantasy', 'age_restriction': 'G'}
    ]

    # TODO: แสดงเมนูให้ผู้ใช้เลือก
    # 1. แสดงหนังทั้งหมด
    def show_movies(movie_list):
        for i in movie_list :
            print(f"{i["movie_name"]} {i["ticket_price"]}")
    
    print(show_movies(movies))
    # 2. ซื้อตั๋วหนัง
    def buy_ticket(movie_list,show_movies):
        print(show_movies(movies))

    doomovie = int(input("เลือกหนังที่ต้องการจะดู (1-5)"))
    selectedmovie = movies[doomovie-1]
    user_age = int(input("อายุของคุณ "))

    def check_age(user_age, age_restriction):
        if age_restriction == "G" :
            return True
        elif int(user_age) < int(age_restriction) :
            return False
        else :
            return 

    check_age(user_age,selectedmovie["age_restriction"])
    if user_age == False :
        print("อายุน้อยเกินไป")

    print("กรุณาเลือกเสียงพากษ์ 1 = พากย์ไทย, 2 = Soundtrack")
    sound = int(input())

    def calculate_price(base_price, genre):
        if genre == 'Action' :
            base_price = base_price + 50
        return base_price
    
    finalprice = calculate_price(selectedmovie['ticket_price'],selectedmovie['genre'])

    # 7. แสดงผลการซื้อบัตร พร้อมชื่อหนัง, เสียงที่เลือก, ราคาตั๋ว
    print(f"ตั๋วเรืิ่อง {selectedmovie['movie_name']} เสียงที่เลือก {sound} ราคา {finalprice}")
    # รับค่าตัวเลือกเมนูจากผู้ใช้
    menu = int(input("เลือกเมนู: "))

    if menu == 1 :
        show_movies
    elif menu == 2 :
        buy_ticket
    else :
        print("เมนูไม่ถูกต้อง")

    # TODO: ตรวจสอบเมนูที่เลือก
    # ถ้าเลือก 1 ให้เรียก show_movies พร้อมส่ง movies
    # ถ้าเลือก 2 ให้เรียก buy_ticket พร้อมส่ง movies
    # ถ้าเลือกอื่น ให้แสดงข้อความว่าเมนูไม่ถูกต้อง

# เรียก main เพื่อเริ่มโปรแกรม
main()

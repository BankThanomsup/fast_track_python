# โจทย์ฝึกทำความเข้าใจการใช้งาน class , constructor(__int__) , object , method , การเรียกใช้  if__name__ == "__main__"
# ==============================================================================================================
# Constructor ใน Python (หรือในหลายภาษา) คือ ฟังก์ชันพิเศษในคลาส ที่จะถูกเรียกอัตโนมัติ ทันทีที่มีการสร้าง Object จากคลาสนั้น
# ใน Python ชื่อของมันคือ __init__ (มีขีดล่าง 2 ข้าง)
# ==============================================================================================================
#ระบบจัดการสัตว์เลี้ยง
#โดยมีเงื่อนไขดังนี้

    # สร้าง Class ชื่อ Pet
    # มี Constructor (__init__) รับข้อมูล 2 อย่าง: name และ species
    # เก็บข้อมูลเหล่านี้ในตัวแปรของ object
    # เพิ่ม method ชื่อ speak()

    # ถ้า species เป็น "dog" ให้พิมพ์ "Woof!"

    # ถ้า species เป็น "cat" ให้พิมพ์ "Meow!"

    # อย่างอื่นให้พิมพ์ "..."
    
    # เขียนโค้ดในส่วน if __name__ == "__main__":

    # สร้างสัตว์เลี้ยง 2 ตัว (หมาและแมว)

    # เรียก speak() ของแต่ละตัว
    
class Pet :
    # Constructor
    def __init__(self,name,species):
        self.name = name
        self.species = species
    # Method
    def speak(self):
        if self.species == "dog" :
        # print("Woof!")
            print(f"{self.name} says: Woof!")
        elif self.species == "cat" :
            print(f"{self.name} says: Meow!")
        else :
            print(f"{self.name} says: ...")
        
# ส่วนนี้จะทำงานก็ต่อเมื่อรันไฟล์นี้โดยตรง
 # รับข้อมูลจาก command line
if __name__ == "__main__" :
    # dog = Pet("Alexader","dog")
    # cat = Pet("Mizo","cat")    
    # dog.speak()
    # cat.speak()
    while True:
        name = input("Enter pet's name (or 'q' to quit) : ")
        if name.lower() == "q":
            print("Exiting Program Bye!")
            break
        
        species = input("Enter pet's species (dog/cat/other): ")
        pet = Pet(name , species)
        pet.speak()
        print("-" * 20)

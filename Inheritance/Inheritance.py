# 1. INHERITANCE (การสืบทอด) 🧬
# =============================================================================
# โจทย์ที่ 1: สร้างระบบการสืบทอดสำหรับสัตว์เลี้ยง
# 
# 📝 สิ่งที่ต้องทำ:
# - สร้าง Base Class ชื่อ Animal มี properties: name, age, color
# - สร้าง method eat(), sleep(), get_info()
# - สร้าง Child Classes: Dog, Cat, Bird ที่สืบทอดจาก Animal
# - แต่ละ Child Class มี method พิเศษของตัวเอง:
#   * Dog: bark(), fetch()
#   * Cat: meow(), climb()
#   * Bird: fly(), sing()
# - ทุกตัวต้องสามารถ override method speak() ของ parent ได้

#Base Class
class Animal:
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color
        
    def eat(self):
        """สัตว์กิน"""
        return f"{self.name} กำลังกินอาหาร"
    def sleep(self):
        """สัตว์นอน"""
        return(f"{self.name} กำลังนอน")
    def get_info(self):
        """แสดงข้อมูลสัตว์"""
        return(f"ชื่อ: {self.name} ,อายุ: {self.age} ,สี: {self.color}")
    def speak(self):
        """เสียงของสัตว์"""
        return f"{self.name} ส่งเสียง"
    
# Child Class: Dog       
class Dog(Animal):
    def __init__(self,name,age,color,breed="ไม่ระบุ"):
        super().__init__(name,age,color)
        self.breed = breed
    def bark(self):
        return(f"{self.name} เห่าดังๆ: วัฟ วัฟ!")
    def spark(self):
        return(f"{self.name} เห่า: โฮ่ง โฮ่ง!")
    def fetch(self):
        return(f"{self.name} วิ่งไปเอาลูกบอลมา")
    def get_info(self):
        """Override ข้อมูลหมามา
        Returns:
            str: ข้อมูลหมาในรูปแบบของข้อความ
        """
        return super().get_info() + f", สายพันธุ์: {self.breed}"
        
class Cat(Animal):
    def __init__(self, name, age, color,indoor=True):
        super().__init__(name, age, color)
        self.indoor = indoor
    
    def speak(self):
        return f"{self.name} ร้อง: เหมียว เหมียว🐱!"
    def meow(self):
        return f"{self.name} ร้องเรียกเจ้าของ: เหมียววววเหมียว🐱🎵!"
    def climb(self):
        return f"{self.name} ปีนขึ้นต้นไม้อย่างคล่องแคล่ว🐱🌳!"
    def get_info(self):
        """
        Override ข้อมูลแมว

        Returns:
            str: ข้อมูลแมวในรูปแบบข้อความ
        """
        location = "บ้าน" if self.indoor else "นอกบ้าน"
        return super().get_info() + f", อยู่: {location}"     
        
class Bird(Animal):
    def __init__(self, name, age, color, can_fly=True):
        super().__init__(name, age, color)
        self.can_fly = can_fly
    
    def speak(self):
        return f"{self.name} ร้อง: จิ๊บ จิ๊บ! 🐦"
    
    def fly(self):
        """นกบิน"""
        if self.can_fly:
            return f"{self.name} บินสูงขึ้นฟ้า ✈️"
        else:
            return f"{self.name} ไม่สามารถบินได้"
    
    def sing(self):
        """นกร้องเพลง"""
        return f"{self.name} ร้องเพลงไพเราะ: ลา ลา ลา~ 🎶"
    
    def get_info(self):
        """Override ข้อมูลนก"""
        flight_status = "บินได้" if self.can_fly else "บินไม่ได้"
        return super().get_info() + f", {flight_status}"    
# =============================================================================
# ทดสอบการใช้งาน
# =============================================================================
if __name__ == "__main__":
    
    print("=" * 50)
    print(" ระบบการสิบทอดสำหรับสัตว์เลี้ยง ")
    print("=" * 50)
    
    #สร้างสัตว์เลี้ยงแต่ละประเภท
    dog = Dog("บัดดี้","2ปี","สีดำ")
    cat = Cat("มิว", 2, "ขาว", indoor=True)
    bird = Bird("ปีกแก้ว", 1, "เขียว", can_fly=True)
    animals = [dog, cat, bird]
    
    # ทดสอบ method พื้นฐาน
    for animal in animals:
        print(f"\n📋 {animal.get_info()}")
        print(f"🗣️  {animal.speak()}")
        print(f"🍽️  {animal.eat()}")
        print(f"😴 {animal.sleep()}")
        
        # ทดสอบ method เฉพาะของแต่ละสัตว์
        if isinstance(animal, Dog):
            print(f"🐕 {animal.bark()}")
            print(f"🎾 {animal.fetch()}")
        elif isinstance(animal, Cat):
            print(f"🐱 {animal.meow()}")
            print(f"🌳 {animal.climb()}")
        elif isinstance(animal, Bird):
            print(f"✈️  {animal.fly()}")
            print(f"🎶 {animal.sing()}")
        
# โจทย์ฝึกฝน Advanced OOP Concepts - ระบบจัดการสัตว์เลี้ยงขั้นสูง
# =============================================================================
# ต่อยอดจาก Pet Manager เพื่อฝึก: Inheritance, Polymorphism, Encapsulation, Abstract Classes
# =============================================================================

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

# 2. POLYMORPHISM (พหุรูป) 🎭
# =============================================================================
# โจทย์ที่ 2: สร้างระบบที่สามารถจัดการสัตว์หลายชนิดในรูปแบบเดียวกัน
#
# 📝 สิ่งที่ต้องทำ:
# - สร้าง method make_sound() ที่ทำงานต่างกันในแต่ละ class
# - สร้าง function animal_concert() ที่รับ list ของสัตว์
# - ให้สัตว์แต่ละตัวร้องเพลง (เรียก make_sound()) ตามลักษณะของตัวเอง
# - ทดสอบด้วยการสร้างสัตว์หลายตัว แล้วใส่ใน list เดียวกัน

# 3. ENCAPSULATION (การห่อหุ้ม) 🔒
# =============================================================================
# โจทย์ที่ 3: ปกป้องข้อมูลสำคัญของสัตว์เลี้ยง
#
# 📝 สิ่งที่ต้องทำ:
# - สร้าง class Pet ที่มี private attributes: __health, __happiness, __energy
# - สร้าง getter methods: get_health(), get_happiness(), get_energy()
# - สร้าง setter methods ที่มีการตรวจสอบ:
#   * set_health(value) - ต้องอยู่ระหว่าง 0-100
#   * set_happiness(value) - ต้องอยู่ระหว่าง 0-100
#   * set_energy(value) - ต้องอยู่ระหว่าง 0-100
# - สร้าง methods: feed() เพิ่ม health, play() เพิ่ม happiness, rest() เพิ่ม energy
# - สร้าง method get_status() แสดงสถานะทั้งหมด

# 4. ABSTRACT CLASSES (คลาสนามธรรม) 🎨
# =============================================================================
# โจทย์ที่ 4: สร้างแม่แบบสำหรับสัตว์เลี้ยงที่บังคับให้ implement methods
#
# 📝 สิ่งที่ต้องทำ:
# - import ABC และ abstractmethod จาก abc module
# - สร้าง abstract class PetInterface ที่มี:
#   * Abstract methods: make_sound(), move(), care_instruction()
#   * Concrete method: introduce() ที่แสดงข้อมูลพื้นฐาน
# - สร้าง concrete classes: HouseCat, GuardDog, TalkingBird
# - แต่ละ class ต้อง implement abstract methods ทั้งหมด
# - ทดสอบการสร้าง object และเรียกใช้ methods

# =============================================================================
# 🎯 เป้าหมายการเรียนรู้:
# 1. เข้าใจการใช้ super() ใน inheritance
# 2. เข้าใจความแตกต่างระหว่าง method overriding และ method overloading
# 3. เข้าใจการใช้ __, _, public, protected, private
# 4. เข้าใจการใช้ @property และ @setter
# 5. เข้าใจการทำงานของ abstract classes และ interfaces
# =============================================================================

print("🚀 พร้อมเริ่มฝึก Advanced OOP แล้ว!")
print("📋 เริ่มจากข้อ 1: Inheritance ก่อนนะครับ")
print("-" * 50)
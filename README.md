# 🐾 Fast Track Python - Pet Management System

โปรเจคเรียนรู้ Python แบบเร่งรัดผ่านการสร้างระบบจัดการสัตว์เลี้ยง ครอบคลุมตั้งแต่ OOP พื้นฐานไปจนถึง Web API และฐานข้อมูล

## 🎯 คำอธิบายโปรเจค

โปรเจคนี้เป็นการเรียนรู้ Python แบบครบวงจรผ่านการสร้างระบบจัดการสัตว์เลี้ยง โดยครอบคลุม:

### 🏗️ หัวข้อการเรียนรู้หลัก
1. **Object-Oriented Programming (OOP)**
   - Classes และ Objects
   - Constructor (`__init__`)
   - Methods และ Properties
   - Interactive Console Interface

2. **Inheritance (การสืบทอด)**
   - Base Class: `Animal`
   - Child Classes: `Dog`, `Cat`, `Bird`
   - Method Overriding
   - Polymorphism

3. **Database Integration**
   - MongoDB Atlas connection
   - CRUD operations with pymongo
   - Environment variables configuration

4. **Web Development**
   - FastAPI framework
   - RESTful API design
   - Pydantic data validation
   - Automatic API documentation

## 📁 โครงสร้างโปรเจค

```
fast_track_python/
├── 📂 Object-Oriented Design/
│   └── pet_manager.py          # OOP พื้นฐาน - Pet class
├── 📂 Inheritance/
│   ├── Inheritance.py          # การสืบทอด - Animal hierarchy
│   └── readme.txt
├── 📂 Database Integration/
│   ├── crud_petMate.py         # FastAPI + MongoDB CRUD
│   ├── test_FastAPI_connect.py # ทดสอบ FastAPI พื้นฐาน
│   ├── test_mongodb_connect.py # ทดสอบการเชื่อมต่อ MongoDB
│   └── .env                    # การตั้งค่าฐานข้อมูล
├── 📄 learnCurve.txt          # รายการเทคโนโลยีที่ควรเรียน
├── 📄 requirements.txt        # Python dependencies
├── 📄 .env.example           # ตัวอย่างไฟล์ environment
└── 📄 README.md              # คู่มือนี้
```

## 💻 ความต้องการระบบ

- **Python**: 3.10+ (แนะนำ 3.11+)
- **MongoDB Atlas**: สำหรับฐานข้อมูล cloud
- **Operating System**: Windows, macOS, หรือ Linux

### 📦 Dependencies หลัก
- `fastapi` - Web framework สำหรับสร้าง API
- `uvicorn` - ASGI server
- `pymongo` - MongoDB driver
- `pydantic` - Data validation
- `python-dotenv` - Environment variables

## 🚀 การติดตั้งและใช้งาน

### ขั้นตอนที่ 1: Clone และ Setup

```bash
# Clone repository
git clone https://github.com/YourUsername/fast_track_python.git
cd fast_track_python

# สร้าง virtual environment
python -m venv .venv

# เปิดใช้งาน virtual environment
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# Windows CMD:
.\.venv\Scripts\activate.bat
# macOS/Linux:
source .venv/bin/activate

# ติดตั้ง dependencies
pip install -r requirements.txt
```

### ขั้นตอนที่ 2: ตั้งค่าฐานข้อมูล

```bash
# คัดลอกไฟล์ environment variables
cp .env.example Database\ Integration/.env

# แก้ไขไฟล์ .env และใส่ MongoDB connection string ของคุณ
# MONGODB_URL=mongodb+srv://username:password@cluster.mongodb.net/
```

### ขั้นตอนที่ 3: ทดสอบการเชื่อมต่อ

```bash
# ทดสอบการเชื่อมต่อ MongoDB
python "Database Integration/test_mongodb_connect.py"

# ควรเห็นข้อความ: ✅ Pinged your deployment. Successfully connected to MongoDB!
```

## 📚 คู่มือการใช้งาน

### 🎮 1. Object-Oriented Programming

```bash
# รันโปรแกรมจัดการสัตว์เลี้ยงแบบ interactive
python "Object-Oriented Design/pet_manager.py"

# ป้อนชื่อและประเภทสัตว์เลี้ยง
# พิมพ์ 'q' เพื่อออก
```

### 🧬 2. Inheritance System

```bash
# ทดสอบระบบการสืบทอด
python "Inheritance/Inheritance.py"

# จะแสดงการทำงานของ:
# - Animal (base class)
# - Dog, Cat, Bird (child classes)
# - Method overriding และ polymorphism
```

### 🗄️ 3. Database Operations

```bash
# ทดสอบการ CRUD กับ MongoDB
cd "Database Integration"
python test_mongodb_connect.py

# รัน CRUD API server
python -m uvicorn crud_petMate:app --reload
```

### 🌐 4. Web API Server

```bash
# รัน FastAPI server
cd "Database Integration"
python -m uvicorn crud_petMate:app --reload --host 0.0.0.0 --port 8000

# เปิด browser ไปที่:
# http://127.0.0.1:8000/docs - API Documentation
# http://127.0.0.1:8000/redoc - Alternative docs
```

## 📖 API Documentation

### 🔗 Endpoints หลัก

| Method | Endpoint | Description | Body |
|--------|----------|-------------|------|
| `GET` | `/pets` | ดึงรายการสัตว์เลี้ยงทั้งหมด | - |
| `GET` | `/pets/{name}` | ดึงข้อมูลสัตว์เลี้ยงตามชื่อ | - |
| `POST` | `/pets` | เพิ่มสัตว์เลี้ยงใหม่ | `Pet` object |
| `PUT` | `/pets/{name}` | อัปเดตข้อมูลสัตว์เลี้ยง | `Pet` object |
| `DELETE` | `/pets/{name}` | ลบสัตว์เลี้ยง | - |

### 📝 Data Models

```json
{
  "name": "string",
  "type": "string", 
  "age": 0
}
```

### 🧪 ตัวอย่างการใช้งาน API

```bash
# สร้างสัตว์เลี้ยงใหม่
curl -X POST "http://127.0.0.1:8000/pets" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "บัดดี้",
    "type": "dog",
    "age": 3
  }'

# ดึงรายการทั้งหมด
curl "http://127.0.0.1:8000/pets"

# ดึงข้อมูลตามชื่อ
curl "http://127.0.0.1:8000/pets/บัดดี้"
```

## 🔧 การพัฒนาต่อ

### 📋 To-Do List

- [ ] **เพิ่มการ Authentication**
  - JWT tokens
  - User registration/login

- [ ] **ปรับปรุง Data Models**
  - เพิ่มฟิลด์ `owner`, `breed`, `medical_history`
  - Validation rules ที่ซับซ้อนขึ้น

- [ ] **Testing Framework**
  - Unit tests ด้วย pytest
  - Integration tests สำหรับ API
  - Mock database สำหรับการทดสอบ

- [ ] **Deployment**
  - Docker containerization
  - Cloud deployment (AWS, Google Cloud, Azure)
  - CI/CD pipeline

- [ ] **Frontend Interface**
  - React.js หรือ Vue.js
  - Mobile app ด้วย React Native

### 🎯 ภารกิจฝึกหัด

#### 📊 Database Level
1. เพิ่มฟิลด์ `owner` (String) ใน Pet model
2. สร้างระบบค้นหาตาม `age range` (min_age, max_age)
3. เพิ่ม validation: species ต้องอยู่ใน {dog, cat, bird}

#### 🌐 API Level
1. เพิ่ม endpoint `PATCH /pets/{id}` สำหรับแก้ไขบางฟิลด์
2. เพิ่ม query parameters สำหรับ filtering และ pagination
3. เพิ่มการจัดการ error แบบละเอียด

#### 🧪 Testing Level
1. เขียน unit tests สำหรับ CRUD operations
2. เขียน API tests ด้วย httpx/pytest
3. เพิ่ม performance testing

## 📚 ทรัพยากรการเรียนรู้

### 🛠️ Essential Technologies (ตาม learnCurve.txt)

#### Backend Development
- **FastAPI/Flask** - Web Framework ✅
- **SQLAlchemy** - Database ORM 
- **Pydantic** - Data Validation ✅
- **JWT** - Authentication
- **Docker** - Containerization

#### Database
- **PostgreSQL/MySQL** - Production Database
- **Redis** - Caching
- **Database Migrations**

#### Testing
- **pytest** - Unit Testing
- **Factory Pattern** - Test Data
- **Mocking** - Isolated Testing

#### Production
- **uvicorn** - ASGI Server ✅
- **nginx** - Reverse Proxy
- **Logging** - Application Monitoring
- **Environment Variables** ✅

### 📖 แหล่งเรียนรู้เพิ่มเติม

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [MongoDB Python Driver](https://pymongo.readthedocs.io/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Python OOP Tutorial](https://docs.python.org/3/tutorial/classes.html)

## 🤝 การมีส่วนร่วม

หากต้องการพัฒนาโปรเจคต่อ:

1. Fork repository นี้
2. สร้าง feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. เปิด Pull Request

## 📄 License

โปรเจคนี้ใช้ MIT License - ดูรายละเอียดใน [LICENSE](LICENSE) file

## 👨‍💻 ผู้พัฒนา

**BankThanomsup** - [GitHub Profile](https://github.com/BankThanomsup)

---

## 🎉 ขอบคุณ

ขอบคุณทุกคนที่ใช้โปรเจคนี้เพื่อการเรียนรู้ Python และการพัฒนา Web Application

**Happy Coding! 🚀**

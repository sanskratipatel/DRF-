#  Django REST Framework (DRF) Learning Repository

This repository contains my notes and revision material while learning **Django REST Framework (DRF)**.  
The goal is to clearly understand **REST APIs, Serializers, Models, and DRF concepts**.

---

## 📖 Key Concepts

### 🔹 API (Application Programming Interface)
- A set of rules that allows two software systems to communicate.  
- Works as a **bridge** between different applications.  
- Example: A mobile app fetching data from a web server via API.

---

### 🔹 REST API (Representational State Transfer)
- A type of API that follows REST architecture principles.  
- Operates using **HTTP methods**:  
  - **GET** → Retrieve data  
  - **POST** → Create new data  
  - **PUT/PATCH** → Update existing data  
  - **DELETE** → Remove data  
- Uses **JSON** or **XML** for data exchange.  
- **Stateless** → Each request contains all the information needed, no client context stored on the server.

---

### 🔹 Django REST Framework (DRF)
- A toolkit built on top of Django for building **REST APIs** easily.  
- Provides:
  - Serializers (convert data formats)  
  - Authentication and permissions  
  - Class-based and function-based views  
  - Browsable API for testing  
  - Integration with Django ORM  

---

### 🔹 Serializers & Deserializers
- **Serializer:** Converts Python/Django objects or database models into JSON or other formats that can be sent over an API.  
- **Deserializer:** Converts JSON or input data received from an API into Python/Django objects for further processing or database storage.  
- Important for communication between **backend (Django)** and **frontend/client applications**.

---

### 🔹 Models
- Define the **structure of database tables** in Django.  
- Each model is a Python class that maps to a database table.  
- Used by DRF with serializers to convert model instances into API responses.  

---

### 🔹 Views in DRF
- **Function-Based Views (FBVs):** Simple Python functions that handle requests and return responses.  
- **Class-Based Views (CBVs):** Organized as Python classes, making the code more reusable and structured.  
- **Generic Views & ViewSets:** Pre-built views provided by DRF that reduce the amount of boilerplate code needed for common operations.

---

### 🔹 CRUD Operations in REST API (Theory)
- **Create (POST):** Add new data to the database through API.  
- **Read (GET):** Fetch data from the database and send it to the client.  
- **Update (PUT/PATCH):** Modify existing records in the database.  
- **Delete (DELETE):** Remove data from the database.  

---

### 🔹 DRF Workflow (Step-by-step)
1. **Client** sends request (usually in JSON).  
2. **URL Routing** maps the request to the correct view.  
3. **View** processes the request logic.  
4. **Serializer** converts data (between model objects and JSON).  
5. **Model/Database** stores or retrieves information.  
6. **Response** is sent back to the client in JSON format.  

---

## 📝 Quick Revision Notes
- **API:** Rules for communication between applications.  
- **REST API:** Stateless, uses HTTP methods for CRUD operations.  
- **DRF:** Django toolkit for building REST APIs.  
- **Model:** Defines database structure.  
- **Serializer:** Converts Django objects → JSON.  
- **Deserializer:** Converts JSON → Django objects.  
- **View Types:** Function-Based, Class-Based, Generic Views, ViewSets.  
- **CRUD:** Create, Read, Update, Delete via HTTP methods.  
- **Workflow:** Client → URL → View → Serializer → Model → Response.  

---

## 👩‍💻 Author
**Sanskrati Patel**  
📧 (mailto:patelsanskrati05@gmail.com)  
 


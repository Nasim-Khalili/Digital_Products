# **Digital Products Marketplace - Django**  

A Django-powered platform for selling and managing digital products (e-books, courses, software licenses, etc.).  

---

## **Key Features**  
🛒 **Product Management**  
- Upload/edit/delete digital products (PDFs, videos, ZIPs)  
- Categorize with tags and collections  

👤 **User System**  
- Secure authentication (signup/login/password reset)  
- User profiles with purchase history  

🔍 **Discovery**  
- Search and filter products by name/category/price  
- Featured products section  

---

## **Installation**  

### **Prerequisites**  
- Python 3.8+  
- Django 4.0+  
- PostgreSQL (recommended) / SQLite (dev)  

### **Setup**  
1. Clone repo:  
   ```bash
   git clone https://github.com/yourusername/django-digital-products.git
   cd django-digital-products
   ```

2. Create virtual env:  
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install requirements:  
   ```bash
   pip install -r requirements.txt
   ```

4. Configure `.env` file:  
   ```env
   SECRET_KEY=your_secret_key_here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. Run migrations:  
   ```bash
   python manage.py migrate
   ```

6. Create admin:  
   ```bash
   python manage.py createsuperuser
   ```

7. Run server:  
   ```bash
   python manage.py runserver
   ```
   Access: [http://localhost:8000](http://localhost:8000)  

---

## **Project Structure**  
```
django-digital-products/
├── products/          # Main products app
├── accounts/          # User accounts
├── payments/          # Payment processing
├── static/            # CSS/JS/images
├── media/             # Uploaded files
├── templates/         # HTML templates
└── requirements.txt   # Dependencies
```

---

## **Tech Stack**  
- **Backend**: Django 4.x  
- **Database**: PostgreSQL  
- **Frontend**: Bootstrap 5  
- **Deployment**: Docker (ready for Heroku/AWS)  

---

## **License**  
MIT License  

--- 

## Contribution
Feel free to contribute by opening an issue or submitting a pull request.

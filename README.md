# SETUP

1. **Open Terminal or Command Prompt**: Launch your terminal (Linux/Mac) or Command Prompt (Windows).

2. **Navigate to Project Directory**:
   - Use the `cd` command to change to the directory where your Django project is located. 
   - Example: 
     ```bash
     cd path/to/your/project
     ```

3. **Activate the Virtual Environment**:
   - Activate your virtual environment to ensure all dependencies are correctly loaded.
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On Linux/Mac:
     ```bash
     source env/bin/activate
     ```

4. **Run Database Migrations (if necessary)**:
   - Ensure your database is up to date with the latest migrations.
   - Run:
     ```bash
     python manage.py migrate
     ```

5. **Start the Django Development Server**:
   - Start the server with the following command:
     ```bash
     python manage.py runserver
     ```
   - By default, this will run the server on `http://127.0.0.1:8000/`.

6. **Access the Application**:
   - Open a web browser and go to the URL provided by the server (typically `http://127.0.0.1:8000/`).

You can modify or add any additional steps specific to your project!
```
.\env\Scripts\activate
```

# Some Useful Codes



```markdown
# Django Migrations and Database Operations

## Making Migrations
To create and apply migrations for database schema changes:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Accessing the Shell
To interact with the database through Django's shell:
```bash
python manage.py shell
```

### Example: Creating a Student Object
```python
from home.models import *

# Creating and saving a Student object
student_1 = Student(name="ADITYA SHAH", age=19, email="", address="")
student_1.save()

# Viewing all Student objects
Student.objects.all()
```
> Alternatively, you can edit the database using **DB Browser**.

---

## CRUD Operations (Create, Read, Update, Delete)

### Creating Data
1. **Method 1**:
   ```python
   car_1 = Car(car_name="NAME 1", speed=45)
   car_1.save()
   ```

2. **Method 2**:
   ```python
   car = Car(car_name="NAME 2", speed=167)
   car.save()
   ```

3. **Method 3**:
   ```python
   Car.objects.create(car_name="NAME 3", speed=160)
   ```

4. **Method 4**:
   ```python
   car_dict = {"car_name": "NAME 4", "speed": 133}
   Car.objects.create(**car_dict)
   ```

### Reading Data
- Retrieve all objects:
  ```python
  car = Car.objects.all()
  for item in car:
      print(f"Name is {item.car_name} and speed is {item.speed}")
  ```

- Retrieve a single object by ID:
  ```python
  Car.objects.get(id=1)
  ```

- Filter objects:
  ```python
  Car.objects.filter(id=10)  # Avoid errors when no object exists
  ```

### Updating Data
- Update a single object:
  ```python
  car = Car.objects.get(id=1)
  car.car_name = "NEW NAME"
  car.speed = 45
  car.save()
  ```

- Update using a query:
  ```python
  Car.objects.filter(id=1).update(car_name="NEW NAME")
  ```

---

## Advanced Authentication in Django

### Accessing User Data in Shell
1. Import the `User` model:
   ```python
   from django.contrib.auth.models import User
   ```

2. View all user objects:
   ```python
   User.objects.all()
   ```

--- 

This guide provides a basic understanding of managing migrations, interacting with the database, performing CRUD operations, and accessing user data in Django.

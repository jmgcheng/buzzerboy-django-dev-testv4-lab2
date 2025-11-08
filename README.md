# Buzzerboy Django Dev Testv4 Lab2

## Notes

- Python 3.10.19
- Django 5.2.7

## Clone Project

```
git clone https://github.com/jmgcheng/buzzerboy-django-dev-testv4-lab2.git
cd buzzerboy-django-dev-testv4-lab2
```

## Setup

```
# windows
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
# migrate will run seed if database is new
python manage.py migrate

# linux
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
# migrate will run seed if database is new
python manage.py migrate
```

## Run

```
python manage.py runserver
```

## Default Seeded User

```
username=system
email=system@helloworld.com
password=system123
```

## Need to run specific Python environment?

Use Conda

```
conda create -n venv_conda_3.10 python=3.10 -y
conda activate venv_conda_3.10
```

---

## 🧾 Lab 2 Submission

👉 [Click here to view the Lab 2 submission screenshots](https://github.com/jmgcheng/buzzerboy-django-dev-testv4-lab2/blob/main/submission-lab2/lab2.md)

---

## 🧾 Research 1 Submission

👉 [Click here to view the Research 1 submission](https://github.com/jmgcheng/buzzerboy-django-dev-testv4-lab2/tree/main/submission-research1)

### 0. Prerequisite

```bash
python version >= 3.9.x 
CapstoneProject % sudo apt install python3.x-venv
CapstoneProject % python3 -m venv .venv
CapstoneProject % source .venv/bin/activate
```

### 1.Install package

```bash
(.venv) CapstoneProject % sudo apt install python3-pip
(.venv) CapstoneProject % pip install flask
(.venv) CapstoneProject % pip install flask-cors
(.venv) CapstoneProject % pip install requests
(.venv) CapstoneProject % pip install pandas

(.venv) CapstoneProject % pip install mariadb==1.1.7
```

### 2. Run server

```bash
Way 1: (.venv) dt-demo-be % python app.py

Way 2: (.venv) FLASK_APP=app.py flask run 
```

# api_final

## How to start a project:

Clone repository and change to it on the command line:

```
git clone git@github.com:user-Roma/api_final_yatube.git
```

```
cd kittygram
```


Create and activate virtual environment:

```
python3 -m venv env
```

```
source env/bin/activate
```


Install dependencies from a file requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```


Make migrations:

```
python3 manage.py migrate
```


Start the project:

```
python3 manage.py runserver
```

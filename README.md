# Meme Tarot
A tarot fortune teller based on memes

## Developer Guide
1. Create a virtual environment in the root directory of the repository and run it.

```python3 -m venv memevenv```

```source memevenv/bin/activate```

2. Install the dependencies using the requirements.txt file.

```pip install -r requirements.txt```

3. Migrate

```python manage.py migrate```

4. Populate the database with card and spread data.

```python manage.py loaddata card.json spread.json```

5. Run the local server and view the basic site framework.

```python manage.py runserver```


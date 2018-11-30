# Meme Tarot
A tarot fortune teller based on memes

## Developer Guide
1. Create a virtual environment in the root directory of the repository and run it.

```python3 -m venv memevenv```

```source memevenv/bin/activate```

2. Install the dependencies using the requirements.txt file.

```pip install -r requirements.txt```

3. Run the server locally and view the starter page.

```python manage.py runserver```

To run the local copy, make sure you've completed steps 1-3, and have merged the local-copy branch.

4. Populate the database with card data.

```python manage.py loaddata fixtures/cards.json```

5. Run the local server and view the basic site framework.

```python manage.py runserver```


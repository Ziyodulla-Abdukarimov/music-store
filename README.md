## MUSIC MARKET

#### - PRODUCTS
#### - ORDERS
#### - CART
### Setup
The first thing to do is to clone the repository:
```sh
$ git clone https://github.com/Ziyodulla-Abdukarimov/music_store.git
$ cd /music_store
```
Create a virtual environment to install dependencies in and activate it:
```sh
$ pip install pipenv
$ pipenv shell
```
Then install the dependencies:
```sh
(env)$ pip install -r requirements.txt
```
Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
# Python: Getting Started

A simple Django app, which can easily be deployed to Heroku.


## Running Locally

- Make sure you have Python 3.7.5 
- To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

### 1、 heroku login
```sh
$ heroku login -i
```

### 2、 git clone and run local
```sh
$ git clone https://github.com/mo891916/start-heroku.git
$ cd start-heroku
$ pip3 install -r requirements.txt
$ python3 manage.py migrate
$ python3 manage.py collectstatic

$ heroku local web --port 8000
```


Your app should now be running on [localhost:8000](http://localhost:8000/).

### 3、 Deploying to Heroku

```sh
$ heroku create
$ git push heroku master
$ heroku run python manage.py migrate
$ heroku run python manage.py createsuperuser
$ heroku open
```

### 4、 

[manage heroku app](https://dashboard.heroku.com/apps)
[manage heroku database](https://data.heroku.com/)
[Official dev center](https://devcenter.heroku.com/articles/deploying-python)

## heroku dev center

For more information about using Python on Heroku, see these Dev Center articles:

- [Deploying Python and Django Apps on Heroku](https://devcenter.heroku.com/articles/deploying-python)

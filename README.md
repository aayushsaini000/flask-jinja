

#for setup this project python 3.5 or greater should be install in your system.

step1 -> Clone project from repo.
step2 -> Go to project directory /flask-jinja/
step3 -> Run cammand > pip install pipenv
step4 -> Then run cammand > pipenv install --dev
step5 -> run cammand pipenv shell
step6 -> after that enviornment will be activate.
step7 -> go to app/ directory.

for run flask app

->In windows you can use

>set FLASK_APP=__init__
>flask run


->In Ubuntu

>export FLASK_APP=__init__
>flask run

App will be run by default on http://127.0.0.1:5000/

You can test app demo template on this route

http://127.0.0.1:5000/user/username  ----------------
http://127.0.0.1:5000/home  ----------------
http://127.0.0.1:5000/about  ----------------
http://127.0.0.1:5000/contact ---------------------

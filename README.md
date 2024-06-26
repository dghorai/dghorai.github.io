# dghorai-portfolio-projects
This is my personal website, consisting of a portfolio of projects.

URL 1: https://dghorai-flaskapp.herokuapp.com/

URL 2: https://dghorai.github.io/

**`Steps Followed to Deploy Python Flask App on Heroku:`**
* Step-1: [Login Heroku](https://www.heroku.com/)
* Step-2: Select 'Create new app'
* Step-3: Download [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) and installed
* Step-4: Go to the project folder
  * Create following two files in the project folder
    * requirements.txt (list of the modules and packages required for the project)
    * Procfile (with File extention)
  * Open Procfile and then write the following line:
    * web: gunicorn app:app (the first app in this case is the Python file app.py and the second app is the flask app, a variable in app.py)
  * Select the full path of the project folder, and then type "CMD" or open "CMD" from the Windows Start Menu.
  * Type 'git init' and press enter (this command creates an empty Git repository in the project folder)
  * Type 'heroku login' and press enter (this will open heroku login page)
  * Type 'heroku git:remote -a flask-app-name' and press enter (flask-app-name will be the name used in Create new app in the step-2)
  * Type 'pip install gunicorn' (this will install gunicorn package in the python virtual environment availale in project folder/some other directory)
  * Type 'pip freeze > requirements.txt' to get all the modules and packages actual version used for the project
  * Type 'git add .'
  * Type 'git commit -m "first commit"'
  * Type 'git push heroku master'
  * Type 'heroku open' (it will open web application)
* Done!

**`Steps Followed to Publish Static Website on GitHub:`**
* Step-1: Create a new GitHub repository
* Step-2: Clone the repository on your computer
* Step-3: Create a static website (single or multi-page)
* Step-4: Push your code to GitHub
* Step-5: Open your repository settings
* Step-6: Click on Pages
* Step-7: Select source - 'Deploy from a branch' from drop-down
* Step-8: Select branch - 'main' from drop-down
  * Save this settings
  * It will take some times to publish site
  * It will create a link of your site
* Done!


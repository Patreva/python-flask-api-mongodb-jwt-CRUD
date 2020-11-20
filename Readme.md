## pip install --user pipenv => Pipenv is used to create a virtual environment which isolates the python packages you used in this project from other system python packages

## pipenv install flask => This will create a new virtual environment and install flask. This command will create two files Pipfile and Pipfile.lock. Pipfile contains the packages that are required for your application. As you can see flask is added to [packages] list. This means when someone downloads your code and runs pipenv install, flask gets installed in their system.


## We have created a one-many relationship between user and movie. That means a user can have one or more movies and a movie can only be created by one user. Here reverse_delete_rule in the movies field of User represents that a movie should be pulled from the user document if the movie is deleted.

## Similarly, User.register_delete_rule(Movie, 'added_by', db.CASCADE) creates another delete rule which means if a user is deleted then the movie created by the user is also deleted.

## Note: I had to register delete rule for added_by separately because User is not yet defined while defining Movie

## pipenv shell -> start the virtual environment

## pipenv exit ->stop the virtual enviroment

## python -m smtpd -n -c DebuggingServer localhost:1025 => Start a SMTP server in terminal
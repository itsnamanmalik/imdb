# Setup On Local Environment
- Clone this repo
- Open Repo in any text editor or IDE (VS Code Recommended)
- Run Some Commands in terminal
-  py -m venv imdbEnv
-  imdbEnv/Scripts/Activate.ps1
-  pip install -r requirements.txt
-  create a database named imdb through phpmyadmin xamp
-  python manage.py makemigrations
-  python manage.py migrate
-  python manage.py runserver
-  check API with valid end-points
-  Valid end-points 
-- fetchmovies (GET)
-- moviesapi (GET or POST)
-- searchmovie : queries = name, year (GET)


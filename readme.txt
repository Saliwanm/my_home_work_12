 a. Add validation of data to registration.
 
 1) Open project
 2) Create file .env
 3) Insert next information in file .env :
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@database:3306/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    PYTHONUNBUFFERED=1
  
 4) run container: sudo docker-compose up --build
 5) enter in our container: sudo docker-compose exec web bash
 6) enter next string: flask db upgrade
 

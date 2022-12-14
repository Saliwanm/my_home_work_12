from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object("config.Config")
app.secret_key = "blablabla"
db = SQLAlchemy(app)

migrate = Migrate(app, db)
# db.init_app(app)

with app.app_context():
    from routes.main import *
    from routes.employees import *
    from routes.plants import *
    from models.models import *
    # db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

#mysql+pymysql://scott:tiger@localhost/foo - mysql
#sqlite:///students.sqlite3 - sqlite
#postgresql+pg8000://scott:tiger@localhost/mydatabase - postgresql
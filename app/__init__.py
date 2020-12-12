from flask             import Flask
from flask_sqlalchemy  import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
from app import models #wtf sqlalchemy!
# https://stackoverflow.com/a/35066886/890858
db.create_all()

from app import routes

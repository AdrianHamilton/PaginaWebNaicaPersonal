from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
import json

with open('/etc/config.json', 'r') as jsonfile:
    config = json.load(jsonfile)

# App initialization
app = Flask(__name__)

# App configuration
app.config['SECRET_KEY'] = config['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = config['SQLALCHEMY_DATABASE_URI']
app.config['MAIL_SERVER'] = config['MAIL_SERVER']
app.config['MAIL_PORT'] = config['MAIL_PORT']
app.config['MAIL_USE_TLS'] = config['MAIL_USE_TLS']
app.config['MAIL_USERNAME'] = config['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = config['MAIL_PASSWORD']

# App extensions
db = SQLAlchemy(app)
mail = Mail(app)

from .NAICA import routes











# from flask import Flask
# from flask_mail import Mail
# from flask_sqlalchemy import SQLAlchemy
# import json

# # App initialization
# app = Flask(__name__)

# # App configuration
# app.config['SECRET_KEY'] = config['SECRET_KEY']
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///NaicaData.db'

# # App extensions
# db = SQLAlchemy(app)

# # Importar los modelos después de definir 'db' para que los modelos estén asociados a SQLAlchemy
# from .NAICA.models import ContactInfo

# # Crear todas las tablas en la base de datos si no existen
# with app.app_context():
#     db.create_all()
#     print("Tablas creadas correctamente")

# # Imprimir lista de tablas creadas
#     tables = db.engine.table_names()
#     print("Tablas en la base de datos:")
#     for table in tables:
#         print(table)


#     # Imprimir columnas de la tabla ContactInfo
#     columns = ContactInfo.__table__.columns.keys()
#     print("Columnas de la tabla ContactInfo:")
#     for column in columns:
#         print(column)
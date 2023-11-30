from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
import json

# with open('/etc/config.json', 'r') as jsonfile:
#     config = json.load(jsonfile)

# App initialization
app = Flask(__name__)

# App configuration
app.config['SECRET_KEY'] = "claveSecreta"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///NaicaData.db'
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = "587"
app.config['MAIL_USE_TLS'] = "True"
app.config['MAIL_USERNAME'] = "no-reply@naica.com"
app.config['MAIL_PASSWORD'] = "B52C670107AF90B397D82911B9987D3C11854017D68BA69BBEE7366B8C3D5D97"

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
# app.config['SECRET_KEY'] = "claveSecreta"
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
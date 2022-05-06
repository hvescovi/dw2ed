from config_comum import *

# sqlalchemy com sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://hylsonco_poo2_user:ifcPoo2!#$@51.222.203.22/hylsonco_poo2"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
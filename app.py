from flask import Flask
from models import db, connect_db, Pet

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['testing'] = True
app.config['SECRET_KEY'] = 'secret'

app
connect_db(app)
# if __name__ == '__main__':
#     app.run(debug=True)
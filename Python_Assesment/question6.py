from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# creating db model
class Accessory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ordquan = db.Column(db.Integer, nullable=False)
    remQuan = db.Column(db.Integer, nullable=False)
    vendN = db.Column(db.String(59), nullable=False)
    purchP = db.Column(db.Float,nullable=False )
    sellinP = db.Column(db.Float,nullable=False)
    # added_date = db.Column(db.Datetime, nullable=False, default=datetime.utcnow)
    # updated_date = db.Column(db.Datetime, nullable=False, default=datetime.utcnow)
    def findAccessory(self,accno):
        Accessorys=[]
        item=Accessory.query.filter(Accessory.accno==accno).first()
        if(item):
            Accessorys.append(item)
        return Accessorys
    def __repr__(self):
        return '<Accessory %r' %self.name
    
    # created database table
    db.create_all()


# I tried completing it on time but unable to do so, i am missing the database table but database has been created in inventory.db
# also i realized i haven't done the model part as well. I was slow in the start as i was focused on the small problems and i forgot to did this one because of that only.
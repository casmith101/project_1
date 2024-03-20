from app import db

class Property(db.Model):
    __tablename__ = 'Project_1'
    id= db.Column(db.Integer, primary_key= True, autoincrement= True)
    title= db.Column(db.String(100), nullable=False)
    bedrooms= db.Column(db.Integer, nullable=False)
    bathrooms= db.Column(db.Integer, nullable=False)
    location= db.Column(db.String(255), nullable=False)
    price= db.Column(db.Float, nullable=False)
    type= db.Column(db.String(50), nullable=False)
    description= db.Column(db.Text, nullable=False)
    photo= db.Column(db.String(255), nullable=True)

   
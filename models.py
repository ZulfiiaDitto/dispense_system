
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key  = True)
    email = db.Column(db.String(100), unique  = True, nullable = False)
    password = db.Column(db.String(100), nullable = False)
    name = db.Column(db.String(100), nullable = False)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    pt_first_name = db.Column(db.String(100), nullable = False)
    pt_last_name = db.Column(db.String(100), nullable = False)
    pt_dob = db.Column(db.String(100), nullable = False)
    pt_address = db.Column(db.String(100), nullable = False)
    pt_state = db.Column(db.String(2), nullable = False)
    pt_city = db.Column(db.String(100), nullable = False)
    pt_zip = db.Column(db.Integer, nullable= False)
    pt_phone = db.Column(db.Integer, nullable= False)
    prescription = db.relationship('Prescriptions', backref = 'patient')

class Physician(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phys_first_name = db.Column(db.String(100), nullable = False)
    phys_last_name = db.Column(db.String(100), nullable = False)
    phys_address = db.Column(db.String(100), nullable = False)
    phys_state = db.Column(db.String(2), nullable = False)
    phys_city = db.Column(db.String(100), nullable = False)
    phys_zip = db.Column(db.Integer, nullable= False)
    phys_phone = db.Column(db.Integer, nullable= False)
    #phys_npi = db.Column(db.Integer, nullable= False)
    presc = db.relationship("Prescriptions", backref = 'physician')

class Prescriptions(db.Model):
    rx_number = db.Column(db.Integer, primary_key=True)
    fill_number = db.Column(db.Integer, nullable= False)
    drug_name = db.Column(db.String(100), nullable = False)
    drug_strenght = db.Column(db.Integer, nullable = False)
    drug_form = db.Column(db.String(100), nullable = False)
    gpi14 = db.Column(db.Integer, nullable = False)
    drug_quantity = db.Column(db.Integer, nullable = False)
    day_supply = db.Column(db.Integer, nullable = False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    physician_id = db.Column(db.Integer, db.ForeignKey('physician.id'))
from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from flask_login import current_user, login_required
from .models import User, Patient, Prescriptions, Physician
from . import db 

# login process here 
main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email_user = request.form['email']
        name_user = request.form['name']
        password_user = request.form['password']
        found_user = User.query.filter_by(email = email_user).first()
        if found_user: 
            flash('Logged in successfully!', category='success')
            return render_template('/dispense.html') 
        else: 
            usr = User(email = email_user, password = password_user, name = name_user )
            db.session.add(usr)
            db.session.commit()
            flash('Registred successfully!', category='success')
            return render_template('/dispense.html') 
    return render_template('/login.html')

@main.route('/logout')
def logout():
    return render_template('logout.html')

@main.route('/dispense.html', methods = ['POST', "GET"])
def dispense():
    if request.method == 'POST':
        form = request.form
        patient = Patient(
            pt_first_name =form['first_name'],
            pt_last_name = form['last_name'], 
            pt_dob = form['dob'],
            pt_address = form['pt_address'],
            pt_state = form['pt_state'],
            pt_city = form['pt_city'],
            pt_zip = form['pt_zip'],
            pt_phone = form['pt_phone'])

        erx = Prescriptions(   
            fill_number = form['fill_number'], 
            drug_name = form['dispense_drug_name'],
            drug_strenght = form['dispense_drug_strenght'],
            drug_form = form['dispense_drug_form'],
            gpi14 = form['gpi14'], 
            drug_quantity = form['dispense_drug_quantity'],
            day_supply = form['day_supply'])
        
        doc = Physician(
            phys_first_name =form['phys_first_name'],
            phys_last_name = form['phys_last_name'], 
            phys_address = form['phys_address'],
            phys_state = form['phys_state'],
            phys_city = form['phys_city'],
            phys_zip = form['phys_zip'],
            phys_phone = form['phys_phone'])
        db.session.add(patient)
        db.session.add(erx)
        db.session.add(doc)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('dispense.html')


@main.route('/reports_requests.html', methods =['POST', 'GET'])
def reports_requests():
    if request.method == "POST":
        drug_name_form = request.form['drug_name']
        found_drug = db.session.execute(db.select(Prescriptions).filter_by(drug_name = drug_name_form)).scalars()
        
        #found_drug = Prescriptions.query.filter_by(drug_name = drug_name_form).all()
        print(found_drug)
        
        header =  ['rx_number', 'fill_number', 'drug_name', 
                   'drug_strenght', 'drug_form', 'gpi14', 
                   'drug_quantity', 'day_supply']
        return render_template('reports.html', headings = header, data = found_drug)
    else: return render_template('reports_requests.html')    
    

#TODO: 1. style table
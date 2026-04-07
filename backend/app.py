from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Change password here (your MySQL password)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:MySql%402026%23Dev@localhost/doctor_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ------------------ MODELS ------------------

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    specialization = db.Column(db.String(100))


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    date = db.Column(db.String(20))
    time_slot = db.Column(db.String(20))


# ------------------ CREATE TABLES ------------------
with app.app_context():
    db.create_all()


# ------------------ APIs ------------------

# Add Doctor
@app.route('/doctors', methods=['POST'])
def add_doctor():
    data = request.json

    name = data.get('name')
    specialization = data.get('specialization')

    # VALIDATION ADDED
    if not name or not specialization:
        return jsonify({"error": "Name and specialization required"}), 400
    
    existing = Doctor.query.filter_by(name=name).first()
    if existing:
        return jsonify({"error": "Doctor already exists"}), 400
    doctor = Doctor(
        name=name,
        specialization=specialization
    )

    db.session.add(doctor)
    db.session.commit()

    return jsonify({
    "status": "success",
    "message": "Doctor added successfully"
}), 201


# Get All Doctors
@app.route('/doctors', methods=['GET'])
def get_doctors():
    doctors = Doctor.query.all()

    result = []
    for d in doctors:
        result.append({
            "id": d.id,
            "name": d.name,
            "specialization": d.specialization
        })

    return jsonify(result)

# Get Docter by ID
@app.route('/doctors/<int:id>', methods=['GET'])
def get_doctor(id):
    doctor = Doctor.query.get(id)

    if not doctor:
        return jsonify({"error": "Doctor not found"}), 404

    return jsonify({
        "id": doctor.id,
        "name": doctor.name,
        "specialization": doctor.specialization
    })


# Book Appointment
@app.route('/appointments', methods=['POST'])
def book_appointment():
    data = request.json

    patient_name = data.get('patient_name')
    doctor_id = data.get('doctor_id')
    date = data.get('date')
    time_slot = data.get('time_slot')

    # ✅ VALIDATION ADDED
    if not patient_name or not doctor_id or not date or not time_slot:
        return jsonify({"error": "All fields are required"}), 400

    existing = Appointment.query.filter_by(
        doctor_id=doctor_id,
        date=date,
        time_slot=time_slot
    ).first()

    if existing:
        return jsonify({"error": "Slot already booked"}), 400

    appointment = Appointment(
        patient_name=patient_name,
        doctor_id=doctor_id,
        date=date,
        time_slot=time_slot
    )

    db.session.add(appointment)
    db.session.commit()

    return jsonify({"message": "Appointment booked successfully"})


#  Get All Appointments
@app.route('/appointments', methods=['GET'])
def get_appointments():
    appts = Appointment.query.all()

    result = []
    for a in appts:
        result.append({
            "id": a.id,
            "patient_name": a.patient_name,
            "doctor_id": a.doctor_id,
            "date": a.date,
            "time_slot": a.time_slot
        })

    return jsonify(result)

# Get filter appointments
@app.route('/appointments/filter', methods=['GET'])
def filter_appointments():
    doctor_id = request.args.get('doctor_id')
    date = request.args.get('date')

    query = Appointment.query

    if doctor_id:
        query = query.filter_by(doctor_id=doctor_id)

    if date:
        query = query.filter_by(date=date)

    appts = query.all()

    result = []
    for a in appts:
        result.append({
            "id": a.id,
            "patient_name": a.patient_name,
            "doctor_id": a.doctor_id,
            "date": a.date,
            "time_slot": a.time_slot
        })

    return jsonify(result)


# ------------------ RUN APP ------------------

if __name__ == '__main__':
    app.run(debug=True)
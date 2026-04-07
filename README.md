# Doctor Appointment Booking System

## Project Overview

This is a full-stack Doctor Appointment Booking System developed using:

Frontend: React.js
Backend:Flask (Python)
Database: MySQL

The application allows users to view doctors, book appointments, and manage schedules efficiently.

---

##  Features

* View list of doctors
* Book appointments
* Prevent duplicate bookings 
* REST API integration
* Responsive user interface

---

##  Setup Instructions

###  Backend Setup (Flask)

1. Navigate to backend folder:

```bash
cd backend
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the server:

```bash
python app.py
```

 Backend will run at: `http://localhost:5000`

---

###  Frontend Setup (React)

1. Navigate to frontend folder:

```bash
cd frontend
```

2. Install dependencies:

```bash
npm install
```

3. Start the app:

```bash
npm start
```

Frontend will run at: `http://localhost:3000`

---
 API Documentation

#Get Doctors

Endpoint:`/doctors`
Method:GET

#Add Doctor

Endpoint: `/doctors`
Method: POST

#Book Appointment

Endpoint: `/appointments`
Method: POST

#Get Appointments

Endpoint:`/appointments`
Method: GET

---

# Assumptions Made

* Each doctor has fixed available time slots
* A user cannot book the same slot twice (duplicate booking restricted)
* Basic validation is implemented on both frontend and backend

---

# Screenshots

Screenshots are available in the `/Screenshots` folder.

---



import React, { useState } from "react";

function App() {
  // Doctor state
  const [dname, setDname] = useState("");
  const [dspec, setDspec] = useState("");

  // Appointment state
  const [pname, setPname] = useState("");
  const [did, setDid] = useState("");
  const [date, setDate] = useState("");
  const [time, setTime] = useState("");

  // Data lists
  const [doctors, setDoctors] = useState([]);
  const [appointments, setAppointments] = useState([]);

  // Add Doctor
  const addDoctor = () => {
    if (!dname || !dspec) {
      alert("Enter all doctor details");
      return;
    }

    fetch("http://127.0.0.1:5000/doctors", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name: dname, specialization: dspec })
    })
      .then(res => res.json())
      .then(data => {
        alert(data.message || data.error);
        setDname("");
        setDspec("");
      });
  };

  // Book Appointment
  const bookAppointment = () => {
    if (!pname || !did || !date || !time) {
      alert("Fill all appointment fields");
      return;
    }

    fetch("http://127.0.0.1:5000/appointments", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        patient_name: pname,
        doctor_id: did,
        date: date,
        time_slot: time
      })
    })
      .then(res => res.json())
      .then(data => {
        alert(data.message || data.error);
        setPname("");
        setDid("");
        setDate("");
        setTime("");
      });
  };

  // Get Doctors
  const getDoctors = () => {
    fetch("http://127.0.0.1:5000/doctors")
      .then(res => res.json())
      .then(data => setDoctors(data));
  };

  // Get Appointments
  const getAppointments = () => {
    fetch("http://127.0.0.1:5000/appointments")
      .then(res => res.json())
      .then(data => setAppointments(data));
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h2>Doctor Appointment System (React)</h2>

      <hr />

      {/* Add Doctor */}
      <h3>Add Doctor</h3>
      <input
        placeholder="Doctor Name"
        value={dname}
        onChange={(e) => setDname(e.target.value)}
      />
      <input
        placeholder="Specialization"
        value={dspec}
        onChange={(e) => setDspec(e.target.value)}
      />
      <button onClick={addDoctor}>Add Doctor</button>

      <hr />

      {/* Book Appointment */}
      <h3>Book Appointment</h3>
      <input
        placeholder="Patient Name"
        value={pname}
        onChange={(e) => setPname(e.target.value)}
      />
      <input
        placeholder="Doctor ID"
        value={did}
        onChange={(e) => setDid(e.target.value)}
      />
      <input
        placeholder="Date (YYYY-MM-DD)"
        value={date}
        onChange={(e) => setDate(e.target.value)}
      />
      <input
        placeholder="Time Slot"
        value={time}
        onChange={(e) => setTime(e.target.value)}
      />
      <button onClick={bookAppointment}>Book Appointment</button>

      <hr />

      {/* Doctors List */}
      <h3>Doctors</h3>
      <button onClick={getDoctors}>Load Doctors</button>
      <ul>
        {doctors.map((d) => (
          <li key={d.id}>
            {d.id} - {d.name} ({d.specialization})
          </li>
        ))}
      </ul>

      <hr />

      {/* Appointments List */}
      <h3>Appointments</h3>
      <button onClick={getAppointments}>Load Appointments</button>
      <ul>
        {appointments.map((a) => (
          <li key={a.id}>
            {a.patient_name} - Doctor {a.doctor_id} - {a.date} at {a.time_slot}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
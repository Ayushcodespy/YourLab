import React, { useState } from "react";
import axios from "axios";
import "./Register.css"; // CSS file for styling

const Register = () => {
  const [form, setForm] = useState({
    full_name: "",
    email: "",
    password: "",
    password2: "",
    age: "",
    role: "patient", // default value
  });

  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post("http://127.0.0.1:8000/api/register/", form);
      setMessage("✅ Registration Successful! You can now login.");
    } catch (err) {
      if (err.response) {
        setMessage(`❌ Registration Failed! ${JSON.stringify(err.response.data)}`);
      } else {
        setMessage("⚠️ Something went wrong!");
      }
    }
  };

  return (
    <div className="auth-container">
      <form className="auth-form" onSubmit={handleSubmit}>
        <h2>Register</h2>

        <input
          type="text"
          name="full_name"
          placeholder="Full Name"
          value={form.full_name}
          onChange={handleChange}
          required
        />

        <input
          type="email"
          name="email"
          placeholder="Email"
          value={form.email}
          onChange={handleChange}
          required
        />

        <input
          type="password"
          name="password"
          placeholder="Password"
          value={form.password}
          onChange={handleChange}
          required
        />

        <input
          type="password"
          name="password2"
          placeholder="Confirm Password"
          value={form.password2}
          onChange={handleChange}
          required
        />

        <select
          name="role"
          value={form.role}
          onChange={handleChange}
          required
        >
          <option value="patient">Patient</option>
          <option value="doctor">Doctor</option>
        </select>

        <button type="submit">Register</button>

        <p className="message">{message}</p>

      </form>
    </div>
  );
};

export default Register;

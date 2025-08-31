import { useState } from "react";
import API from "../api";

function Register() {
  const [form, setForm] = useState({
    full_name: "",
    email: "",
    username: "",
    role: "patient",
    password: "",
    password2: "",
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await API.post("register/", form);
      console.log("User Registered:", res.data);
      alert("Registration Successful!");
    } catch (err) {
      console.error(err.response.data);
      alert("Registration Failed!");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="full_name" placeholder="Full Name" onChange={handleChange} required />
      <input name="email" type="email" placeholder="Email" onChange={handleChange} required />
      <input name="username" placeholder="Username" onChange={handleChange} required />
      <select name="role" onChange={handleChange}>
        <option value="patient">Patient</option>
        <option value="doctor">Doctor</option>
      </select>
      <input name="password" type="password" placeholder="Password" onChange={handleChange} required />
      <input name="password2" type="password" placeholder="Confirm Password" onChange={handleChange} required />
      <button type="submit">Register</button>
    </form>
  );
}

export default Register;

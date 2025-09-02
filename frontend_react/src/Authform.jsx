import React, { useState } from "react";
import './Authform.css';

export default function Authform() {

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
      console.log(await axios.post("http://127.0.0.1:8000/api/register/", form))
      setMessage("✅ Registration Successful! You can now login.");
    } catch (err) {
      if (err.response) {
        setMessage(`❌ Registration Failed! ${JSON.stringify(err.response.data)}`);
      } else {
        setMessage("⚠️ Something went wrong!");
      }
    }
  };

    const [isLogin, setIsLogin] = useState(true);
    return (
        <div className="container">
            <div className="form-container">
                {isLogin ? (
                    <>
                        <h2>Login</h2>
                        <form>
                            <input type="email" placeholder="Email" required />
                            <input type="password" placeholder="Password" required />
                            <button type="submit">Login</button>
                        </form>
                        <p>
                            Don't have an account?{" "}
                            <a href="#" onClick={(e) => { e.preventDefault(); setIsLogin(false); }}>
                                Signup
                            </a>
                        </p>
                    </>
                ) : (
                    <>
                        <h2>Signup</h2>
                        <form onSubmit={handleSubmit}>
                            <input type="text" name="full_name" placeholder="Full name" value={form.full_name} onChange={handleChange} required/>
                            <input type="email" name="email" placeholder="Email" value={form.email} onChange={handleChange} required/>
                            <select name="role" value={form.role} onChange={handleChange} required>
                                <option value="patient">Patient</option>
                                <option value="doctor">Doctor</option>
                            </select>
                            <input type="password" name="password" placeholder="Password" value={form.password} onChange={handleChange} required />

                            <input type="password" name="password2" placeholder="Confirm Password" value={form.password2} onChange={handleChange} required />
                            <button type="submit">Register</button>
                            <p className="message">{message}</p>
                        </form>
                        <p>
                            Already have an account?{" "}
                            <a href="#" onClick={(e) => { e.preventDefault(); setIsLogin(true); }}>
                                Login
                            </a>
                        </p>
                    </>
                )}
            </div>
        </div>
    )
}
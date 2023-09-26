import React from 'react'
import { useState } from 'react';
import '../style/Signin.css'

const Signup = () => {
  
    const [formData, setFormData] = useState({
      username: '',
      password: '',
      email: '',
    });
  
    const handleInputChange = (e) => {
      const { name, value } = e.target;
      setFormData({
        ...formData,
        [name]: value,
      });
    };
  
    const handleSubmit = async (e) => {
      e.preventDefault();
      console.log(formData)
      // You can add your login logic here
      const result = await fetch('http://localhost:3001/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      }).then(data => data.json())
      .catch(err => err)
  
      console.log(result)
    };
  
    return (
      <div className="login-container">
        <form className="login-form" onSubmit={handleSubmit}>
          <h2>Sign Up</h2>
          <div className="form-group">
            <label htmlFor="username">Username</label>
            <input
              type="text"
              id="username"
              name="username"
              value={formData.username}
              onChange={handleInputChange}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input
              type="password"
              id="password"
              name="password"
              value={formData.password}
              onChange={handleInputChange}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input
              type="email"
              id="email"
              name="email"
              value={formData.email}
              onChange={handleInputChange}
              required
            />
          </div>
          <button type="submit">Sign Up</button>
        </form>
      </div>
    );
  }


export default Signup
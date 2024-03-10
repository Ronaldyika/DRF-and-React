import React, { useState } from 'react';
import api from '../services/api';

const UserLogin = () => {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
  });

  const handleInputChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const response = await api.post('login/', formData);
      console.log('Login success:', response);
      // Perform actions upon successful login, e.g., redirect or update state
    } catch (error) {
      console.error('Login failed:', error);
      // Handle login failure, e.g., show error message to the user
    }
  };

  return (
    <div>
      <h2>User Login</h2>
      <form onSubmit={handleLogin}>
        <label>
          Username:
          <input type="text" name="username" value={formData.username} onChange={handleInputChange} />
        </label>
        <br />
        <label>
          Password:
          <input type="password" name="password" value={formData.password} onChange={handleInputChange} />
        </label>
        <br />
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default UserLogin;

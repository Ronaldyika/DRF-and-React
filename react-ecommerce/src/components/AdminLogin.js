import React, { useState } from 'react';
import api from '../services/api';

const AdminLogin = () => {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
  });

  const handleInputChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleAdminLogin = async (e) => {
    e.preventDefault();

    try {
      const response = await api.post('admin-login/', formData);
      console.log('Admin Login success:', response);
      // Handle success, e.g., set authentication token, redirect to admin dashboard
    } catch (error) {
      console.error('Admin Login failed:', error);
      // Handle failure, e.g., show error message to the admin
    }
  };

  return (
    <div>
      <h2>Admin Login</h2>
      <form onSubmit={handleAdminLogin}>
        {/* Add admin login form fields */}
        <button type="submit">Admin Login</button>
      </form>
    </div>
  );
};

export default AdminLogin;

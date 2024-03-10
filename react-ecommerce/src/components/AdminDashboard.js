import React, { useState, useEffect } from 'react';
import api from '../services/api';

const AdminDashboard = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await api.get('admin-products/');
        setProducts(response.data);
      } catch (error) {
        console.error('Error fetching admin products:', error);
      }
    };

    fetchProducts();
  }, []);

  const handleDeleteProduct = async (productId) => {
    try {
      await api.delete(`admin-products/${productId}/`);
      // Handle success, e.g., update state or show a success message
    } catch (error) {
      console.error('Error deleting product:', error);
      // Handle failure, e.g., show an error message to the admin
    }
  };

  return (
    <div>
      <h2>Admin Dashboard</h2>
      <ul>
        {products.map((product) => (
          <li key={product.id}>
            {product.name} - <button onClick={() => handleDeleteProduct(product.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default AdminDashboard;

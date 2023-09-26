import React from 'react'
import { useState } from 'react';
import '../style/Createproduct.css'
import { useNavigate } from 'react-router-dom';

const Createproduct = () => {
  const navigation = useNavigate()
  
    const [productData, setProductData] = useState({
      name: '',
      price: '',
      quantity: '',
    });
  
    const handleInputChange = (e) => {
      const { name, value } = e.target;
      setProductData({
        ...productData,
        [name]: value,
      });
    };
  
    const handleSubmit = async (e) => {
      e.preventDefault();
      console.log(productData)
      // You can add your login logic here
      const result = await fetch('http://localhost:3001/product/create', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(productData),
      }).then(data => data.json())
      .catch(err => err)
  
      console.log(result)
    };
    return (
      <div className="product-form-container">
        <form className="product-form" onSubmit={handleSubmit}>
          <h2>Add Product</h2>
          <div className="form-group">
            <label htmlFor="name">Product Name</label>
            <input
              type="text"
              id="name"
              name="name"
              value={productData.name}
              onChange={handleInputChange}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="price">Product Price</label>
            <input
              type="number"
              id="price"
              name="price"
              value={productData.price}
              onChange={handleInputChange}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="quantity">Product Quantity</label>
            <input
              type="number"
              id="quantity"
              name="quantity"
              value={productData.quantity}
              onChange={handleInputChange}
              required
            />
          </div>
          <button type="submit">Add Product</button>
          <button onClick={() => navigation('/home')} style={{ marginTop: 20 }}>Home</button>

        </form>



      </div>
    );
  }


export default Createproduct
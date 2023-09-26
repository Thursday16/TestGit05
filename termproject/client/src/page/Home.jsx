import React, { useEffect, useState } from 'react'
import '../style/Home.css'
import { useNavigate } from 'react-router-dom';

const Home = () => {
  const navigation = useNavigate()
  const [products, setProducts] = useState([])

  useEffect(() => {
    // Make an HTTP GET request to fetch product data
    // Replace the URL with the actual API endpoint
    fetch('http://localhost:3001/product/getall') // Use the correct API endpoint
      .then((response) => response.json())
      .then((data) => {
        setProducts(data.message);
      })
      .catch((error) => {
        console.error('Error fetching product data:', error);
      });
  }, []);
  console.log(products)
  return (
    <div className="product-table-container">
      <h2 className="product-table-title">Product List</h2>
      <div className="glassmorphism-table">
        <table className="product-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Product Name</th>
              <th>Price</th>
              <th>Quantity</th>
            </tr>
          </thead>
          <tbody>
            {products?.map((product, index) => (
              <tr key={product.id} className="table-row">
                <td>{index+1}</td>
                <td>{product.name}</td>
                <td>${product.price.toFixed(2)}</td>
                <td>{product.quantity}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <button onClick={() => navigation('/createproduct')} style={{ marginTop: 20 }}>Add Product</button>
    </div>
  );
}

export default Home
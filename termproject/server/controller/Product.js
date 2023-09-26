const Product = require('../model/Product')

exports.getall = async (req, res) => {
    try {
      const products = await Product.find(); // Retrieve all products
      console.log(products, 'here')
      // Send the product data as JSON response
      res.status(200).json({ success: true, message: products});
    } catch (error) {
      // Handle any errors (e.g., database error)
      res.status(400).json({ message: 'Failed to fetch products', error: error.message });
    }
  };



exports.create = async (req, res) => {
  const { name, price, quantity, description } = req.body;

  try {
    // Create a new product instance using the Product schema
    const newProduct = new Product({
      name,
      price,
      quantity,
      description,
    });

    // Save the product to the database
    const savedProduct = await newProduct.save();

    // Send a success response with the saved product data
    res.status(200).json({success: true, message:'product created successfully'});
  } catch (error) {
    // Handle any errors (e.g., validation error or database error)
    res.status(400).json({ sucess: false,  message: 'Product creation failed', error: error.message });
  }
}
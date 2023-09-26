const User = require('../model/User')

exports.Signup = async (req, res) => {
  try {
    // Create a new user instance using the User schema
    const newUser = new User({
      username: req.body.username,
      email: req.body.email,
      password: req.body.password,
    });

    // Save the user to the database
    const savedUser = await newUser.save();

    // Send a success response
    res.status(201).json({success: true, message: 'user is created'});
  } catch (error) {
    // Handle any errors (e.g., duplicate username or database error)
    res.status(400).json({ message: 'Registration failed', error: error.message });
  }
} 
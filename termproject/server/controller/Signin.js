const User = require('../model/User')

exports.Signin = async (req, res) => {
  const { email, password } = req.body;

try {
  // Find the user by their email
  const user = await User.findOne({ email });

  // If the user is not found, return an error
  if (!user) {
    return res.status(404).json({ message: 'User not found' });
  }

  // Compare the provided password with the stored password
  if (password === user.password) {
    // Passwords match, user is authenticated (not recommended for production)
    return res.status(200).json({ success: true, message: 'Authentication successful' });
  } else {
    // Passwords do not match, return an error
    return res.status(401).json({ success: false, message: 'Authentication failed' });
  }
} catch (error) {
  // Handle any errors (e.g., database error)
  return res.status(500).json({ message: 'Sign-in failed', error: error.message });
}
}
const express = require('express')
const { Signup } = require('../controller/SignUp')
const route = express.Router()

route.get('/test', (req, res) => {
  return res.status(200).json({ success: true, message: 'this is signin route'})
})
route.post('/', Signup)

module.exports = route
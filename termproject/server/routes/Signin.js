const express = require('express')
const { Signin } = require('../controller/Signin')
const route = express.Router()

route.get('/test', (req, res) => {
  return res.status(200).json({ success: true, message: 'this is signin route'})
})

route.post('/', Signin)

module.exports = route
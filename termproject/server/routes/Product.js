const express = require('express')
const { create, getall } = require('../controller/Product')
const route = express.Router()


route.get('/test', (req, res) => {
  return res.status(200).json({ success: true, message: 'this is product route'})
})

route.post('/create', create)

route.get('/getall', getall)

module.exports = route
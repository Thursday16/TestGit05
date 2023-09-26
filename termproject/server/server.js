const express = require('express')
const app = express()
const bodyparser = require('body-parser')
const cors = require('cors')
const mongoose = require('mongoose')
const signin = require('./routes/Signin')
const signup = require('./routes/Signup')
const product = require('./routes/Product')

app.use(cors())
app.use(bodyparser.urlencoded({ extended: true }))
app.use(bodyparser.json())

var url = "mongodb+srv://percy2545:jxxw0n5FAVAB3j95@webdevdb.kxwvcal.mongodb.net/?retryWrites=true&w=majority"
mongoose.connect(url, { 
  useNewUrlParser: true, 
  useUnifiedTopology: true
}).then(() => console.log('connected'))

app.get('/', (req, res) => {
  return res.status(200).json({ success: true, message: 'You are getting the basic route'})
})

app.use('/signin', signin)
app.use('/signup', signup)
app.use('/product', product)

const port = 3001
app.listen(port, () => console.log('server running port', port))
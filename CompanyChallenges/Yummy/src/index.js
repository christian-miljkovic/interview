// index.js
const sqlHelper = require('./helperFunctions/sqlFunctions.js'); 
const jsonHelper = require('./helperFunctions/jsonifyFunctions.js');
const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const mysql = require('mysql');


// Add middleware
app.use(bodyParser.urlencoded({ extended: false }));


const client = mysql.createConnection({
    host: "remotemysql.com",
    user: "OtgFo6e2XB",
    password: "AC0kHW1ecK",
    database:"OtgFo6e2XB"
  });


client.connect((err)=> {
    if (err) throw err;
    console.log("Connected!");
});

// Main endpoint for application
app.get('/api/v1/orders',(req,res)=>{

    if(Object.keys(req.query).length === 0){
        throw new Error('400: User Id is Required');
    }

    const userId = req.query.user_id;
    res.send({body:jsonHelper.jsonifyMeals(client,1,2)});
});

app.listen(3000);





// Server name: remotemysql.com 
// Port: 3306

// username: OtgFo6e2XB
// password: AC0kHW1ecK
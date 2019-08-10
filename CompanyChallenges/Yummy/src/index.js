// index.js
const jsonHelper = require('./helperFunctions/jsonifyFunctions.js');
const generalHelper = require('./helperFunctions/generalFunctions.js');
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
app.get('/api/v1/orders', async (req,res)=>{

    if(Object.keys(req.query).length === 0){
        throw new Error('400: User Id is Required');
    }

    const userId = req.query.user_id;
    let userOrder = {}

    
    jsonHelper.jsonifyOrders(client,userId)
    .then(result =>{
        userOrder.orders = result;
        let orderAttributes = [];
        jsonHelper.jsonifyOrderAttributes(client,userOrder.orders.id).then(result=>{
            for(let i = 0; i < result.length; i++){
                orderAttributes.push(result[i]);
            }
            let orderQuantity = generalHelper.getOrderSize(orderAttributes);
            userOrder.orders.meal_count = orderQuantity;
            return orderAttributes            
        })
        .then(result => {            
            for(let i = 0; i < result.length; i++){
                // look at the jsonify function thats where the issue is
                jsonHelper.jsonifyMeals(client,result[i].id).then(result=>{
                    userOrder.orders.meals.push(result);
                    res.send({body:userOrder});
                });
            }
        })    
    })
    
});

app.listen(3000);





// Server name: remotemysql.com 
// Port: 3306

// username: OtgFo6e2XB
// password: AC0kHW1ecK
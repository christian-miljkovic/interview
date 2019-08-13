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
    let userOrder = {
        "orders":[],
    }

    let currentIndex;
    
    jsonHelper.jsonifyOrders(client,userId)
    .then(results =>{
        for(let i = 0; i < results.length; i++){
            
            let order = results[i];
            currentIndex = i;

            userOrder.orders.push(order);
            let orderAttributes = [];
            jsonHelper.jsonifyOrderAttributes(client,order.id).then(result=>{                               
                for(let i = 0; i < result.length; i++){
                    orderAttributes.push(result[i]);
                }
                let orderQuantity = generalHelper.getOrderSize(orderAttributes);
                if(orderQuantity !=0 ){
                    userOrder.orders[currentIndex].meal_count = orderQuantity;
                }
                else{
                    userOrder.orders[currentIndex].meal_count = 0;
                }
                
                return result;
            })
            .then(result => {
                if(result.length > 0){                                    
                    jsonHelper.jsonifyMultipleMeals(client, result).then(meals => { 
                                                                                                                               
                        userOrder.orders[currentIndex].meals = meals;                      
                        res.send({body:userOrder});                                          
                    })                                                    
                }                                                                                                  
            })
        }    
    })
});

app.listen(3000);





// Server name: remotemysql.com 
// Port: 3306

// username: OtgFo6e2XB
// password: AC0kHW1ecK
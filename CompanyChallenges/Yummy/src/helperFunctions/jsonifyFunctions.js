// jsonifyFunctions.js
// Methods to help convert data returned from MySQL to JSON Object
const sqlHelper = require('./sqlFunctions.js'); 

const jsonHelper = {

    jsonifyMeals : (client, mealId, mealQuantity) => {

        return sqlHelper.getMealAttributes(client, mealId, mealQuantity).then(result=>{        
            
            if(result != null){
                let meal = {
                    "id":result.id,
                    "quantity": mealQuantity,
                    "name":result.name,
                    "description": result.description,
                    "image_url": result.image_url
                }
                return meal;
            }
        });
    },

    jsonifyMultipleMeals: (client, mealsArray) => {
        return new Promise((resolve) => {
            sqlHelper.getMultipleMealAttributes(client, mealsArray).then(result=>{        
            
                promiseArray = [];
    
                for(let i = 0; i < result.length; i++){
                    promiseArray.push(result[i]);
                }
    
                Promise.all(promiseArray)
                .then(values => {
                    newArray = [];
                    for(let i = 0; i < values.length; i++){
                        let meal = {
                            "id":values[i].id,
                            "quantity": values[i].quantity,
                            "name":values[i].name,
                            "description": values[i].description,
                            "image_url": values[i].image_url
                        }
                        newArray.push(meal);
                    }            
                    resolve(newArray);
                })
             }) 
            
        })
    },

    jsonifyOrders : (client, userId) => {

        return sqlHelper.getUserOrders(client, userId).then(result=>{
            
            let orders = [];
            for(let i = 0; i < result.length; i++){
                let order = {
                    "id":result[i].id,
                    "delivery_date": result[i].delivery_date,
                    "meal_count": null,
                    "meals":[],
                }
                orders.push(order);
            }
            return orders;
        });
    },

    jsonifyOrderAttributes : (client, orderId) => {
        return sqlHelper.getOrderAttributes(client,orderId).then(result => {
            let orderAttributes = [];
            for(let i = 0; i < result.length; i++){
                orderAttributes.push({"id": result[i].id, "meal_id": result[i].meal_id, "order_id": result[i].order_id, "quantity": result[i].quantity});
            }
            return orderAttributes;
        });
    }

}


module.exports = jsonHelper;
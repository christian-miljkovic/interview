// jsonifyFunctions.js
// Methods to help convert data returned from MySQL to JSON Object
const sqlHelper = require('./sqlFunctions.js'); 
const util = require('util');

const jsonHelper = {

    jsonifyMeals : (client, mealId) => {


        return sqlHelper.getMealAttributes(client, mealId).then(result=>{
            let meal = {
                "id":result.id,
                "quantity": null,
                "name":result.name,
                "description": result.description,
                "image_url": result.image_url
            }
            return meal;
        });
    },

    jsonifyOrders : (client, userId) => {

        return sqlHelper.getUserOrders(client, userId).then(result=>{
            let orders = {
                "id":result.id,
                "delivery_date": result.delivery_date,
                "meal_count": null,
                "meals":[],
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
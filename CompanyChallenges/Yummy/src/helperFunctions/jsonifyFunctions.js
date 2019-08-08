// jsonifyFunctions.js
// Methods to help convert data returned from MySQL to JSON Object
const sqlHelper = require('./sqlFunctions.js'); 
const util = require('util');

const jsonHelper = {

    jsonifyMeals : (client, mealId, quantity) => {


        return sqlHelper.getMealAttributes(client, mealId).then(result=>{
            let meal = {
                "id":result.id,
                "quantity": quantity,
                "name":result.name,
                "description": result.description,
                "image_url": result.image_url
            }
            return meal;
        });
    },

}


module.exports = jsonHelper;
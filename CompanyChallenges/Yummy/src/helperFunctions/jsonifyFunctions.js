// jsonifyFunctions.js
// Methods to help convert data returned from MySQL to JSON Object
const sqlHelper = require('./sqlFunctions.js'); 

const jsonHelper = {

    jsonifyMeals : (client, mealId, quantity) => {

        let meals = {};
        
        sqlHelper.getMealAttributes(client, mealId).then(
            meals.name = result.name
        );
        
        // let meals = {
        //     "id":mealAtrributes.id,
        //     "quantity": quantity,
        //     "name":mealAtrributes.name,
        //     "description": mealAtrributes.description,
        //     "image_url": mealAtrributes.image_url
        // }

        return meals;
    },

}


module.exports = jsonHelper;
// sqlFunctions.js 
// Helper functions for making queries to MySQL database

const sqlHelper = {

    getUserById : (client, userId) => {
        client.query(`SELECT * FROM users WHERE  id=${userId}`, (err, result) =>{
            if (err) throw err;
            return result;
            });
    },

    getUserOrders: (client, userId) => {

        return new Promise((resolve, reject) => {
            client.query(`SELECT * FROM orders WHERE user_id=${userId}`, (err, result) =>{
                if (err){
                    reject(err);
                }
                else{                    
                    resolve(result);
                } 
            });
        })
        
    },

    getOrderAttributes: (client, orderId) => {
        return new Promise((resolve, reject) => {
            client.query(`SELECT * FROM order_attributes WHERE order_id=${orderId}`, (err, result) =>{
                if (err){
                    reject(err);
                }
                else{
                    resolve(result);
                }
            });
        })
    },

    getMealAttributes: (client, mealId) => {
        const promise = new Promise((resolve, reject) => {
            client.query(`SELECT * FROM meals WHERE id=${mealId}`, (err, result) =>{
                if (err){
                    reject(err);
                } 
                else{
                    resolve(result);
                }
            });
        })

        return promise;
    },

    getMultipleMealAttributes: (client, mealsArray) =>{

        let queryString = `SELECT * FROM meals WHERE id=${mealsArray[0].meal_id}`;
        for(let i = 1; i < mealsArray.length; i++){
            queryString = queryString.concat(` OR id=${mealsArray[i].meal_id}`);
        }
        
        const promise = new Promise((resolve, reject) => {
            client.query(queryString, (err, result) =>{
                if (err){
                    reject(err);
                } 
                else{
                    resolve(result);
                }
            });
        })

        return promise;
    }
}

module.exports = sqlHelper;
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
            client.query(`SELECT * FROM orders WHERE id=${userId}`, (err, result) =>{
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
                    resolve(result[0]);
                }
            });
        })

        return promise;
    }
}

module.exports = sqlHelper;
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

        client.query(`SELECT * FROM orders WHERE id=${userId}`, (err, result) =>{
            if (err) throw err;
            return result;
            });
    },

    getOrderAttributes: (client, orderId) => {
        client.query(`SELECT * FROM order_attributes WHERE order_id=${orderId}`, (err, result) =>{
            if (err) throw err;
            return result;
            });
    },

    getMealAttributes: (client, mealId) => {
        client.query(`SELECT * FROM meals WHERE id=${mealId}`, (err, result) =>{
            if (err) throw err;
            return result[0];
            });
    }
}

module.exports = sqlHelper;
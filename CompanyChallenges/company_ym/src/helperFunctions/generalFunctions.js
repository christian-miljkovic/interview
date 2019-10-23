// generealFunctions.js 
// Helper functions for general repeated logic
const jsonHelper = require('./jsonifyFunctions.js');

const generalHelper = {

    getOrderSize: (orderAttributes)=>{
        let quantity = 0
        for(let i = 0; i < orderAttributes.length; i++){
            quantity = quantity + orderAttributes[i].quantity;
        }
        return quantity;
    },

    // default: sorts by id ascending
    sortDescending: (userOrder) => {
        userOrder.orders = userOrder.orders.sort((a,b) => (a.id > b.id) ? 1 : -1);
    },

    getOrderById: (userOrder, lookUpId) => {
        for(let i =0; i < userOrder.orders.length; i++){
            if(userOrder.orders[i].id == lookUpId){
                return userOrder.orders[i];
            }
        }
    },
}

module.exports = generalHelper;
// generealFunctions.js 
// Helper functions for general repeated logic

const generalHelper = {

    getOrderSize(orderAttributes){
        let quantity = 0
        for(let i = 0; i < orderAttributes.length; i++){
            quantity = quantity + orderAttributes[i].quantity;
        }
        return quantity;
    }
}

module.exports = generalHelper;
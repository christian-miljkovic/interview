# High Level
- sell various prints of Herman’s work


# Feature Requests
- Order print photo out of 100 photos
- Be able to print (small, medium, large) -> costs to each
- User provides their shipping info
- API endpoint returns entire photo catalog (options: lazy-load 20 photos at a time)
- API endpoint recieves:
    1. order details
    2. processes order
    3. saves order
    4. returns order number
    5. returns billing summary
- Use tests

# Assumptions
- Cannot buy multiple prints in an order

# Tech Spec
- Python 3
- Django 
- Follow RESTful design
- Photo catalog and order data are saved to db

# Wire Frame Data points
User Billing info
- First/Last name
- email 
- primary phone number
- Address Line 1 and 2
- City
- State/Region
- Postal Code
- Country

Print Info
- Print size
- cost
- shipping cost
- total 

# Endpoints
All Prints: prints/
Add Prints: admin/prints/prints/add/

All Orders: orders/
Add Orders: admin/prints/order/add/

All Photos: photos/
Paginated Photos: photos/?offset=20
Add Photos: admin/prints/photo/add/


Login Info:
user: admin
password: test1test1


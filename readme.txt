Hey !!!

1. GET ( API to fetch a bank details, given branch IFSC code ) 
    # http://127.0.0.1:8000/bank 
    # passparameter - > "ifsc" & jwt_authentication 


2. GET ( GET API to fetch all details of branches, given bank name and a city ) 
       http://127.0.0.1:8000/bank-branches  - > 
       passparameter = "city" & "bank_name" & jwt_authentication 


3. POST ( get jwt token ) - 
   		# http://127.0.0.1:8000/api/token/
   		# pass jwt parameter "username" & "password"
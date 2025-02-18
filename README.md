# PSP


# Register
curl -H  "Content-Type: application/json" -X POST -L http://0.0.0.0:5000/register --data '{"name": "Artem", "password": "12345", "surname": "Makanov", "patronymic": "", "login": "abcd"}'

# Login
curl -H  "Content-Type: application/json" -X POST -L http://0.0.0.0:5000/login --data '{"password": "12345", "login": "abcd"}'

# Protected
curl -H  "Content-Type: application/json" -H "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbiI6ImFiY2QiLCJleHAiOjE3Mzk0NTg2MzN9.E_KUF0WDwZoXqe1V6dzeXaUMMrqEOpNSUSYPx5XvgBA" -X GET -L http://0.0.0.0:5000/protected 


# Protected
curl -H  "Content-Type: application/json" -X GET -L http://localhost:5000/search  --data '{"q": ""}'

# Protected
curl -H  "Content-Type: application/json" -X GET -L http://localhost:5000/pdf/1 


curl -H  "Content-Type: application/json" -X GET -L http://localhost:5000/search?q=fairness

curl -H  "Content-Type: application/json" -X GET -L http://localhost:5000/page?id=1

curl -H  "Content-Type: application/json" -X GET -L http://localhost:5000/get_similar?id=1


curl -H  "Content-Type: application/json" -X POST -L http://0.0.0.0:5000/add_paper_to_favourites?login=abcd?id=1


curl -H  "Content-Type: application/json" -X GET -L http://0.0.0.0:5000/get_users_papers?login=abcd

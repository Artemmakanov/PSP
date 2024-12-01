# PSP


# Register
curl -H  "Content-Type: application/json" -X POST -L http://0.0.0.0:5000/register --data '{"name": "Artem", "password": "12345", "surname": "Makanov", "patronymic": "", "login": "abcd"}'

# Login
curl -H  "Content-Type: application/json" -X POST -L http://0.0.0.0:5000/login --data '{"password": "12345", "login": "abcd"}'

# Protected
curl -H  "Content-Type: application/json" -H "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbiI6ImFiY2QiLCJleHAiOjE3MzIxMDYzMzF9.bdsidLjbuABZShppM-xQBgxCAyQKTXI9XUn3049_eMA" -X GET -L http://0.0.0.0:5000/protected 

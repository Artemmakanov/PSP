# PSP


# Register
curl localhost:5000/register -d '{"login": "bar", "password": "foo", "surname": "sidorov", "patronymic": "", "name": "oleg"}' -H 'Content-Type: application/json'

# Login
curl localhost:5000/login -d '{"login": "bar", "password": "foo"}' -H 'Content-Type: application/json'


# Protected
curl -X GET http://localhost:5000/protected \
     -H "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbiI6ImJhciIsImV4cCI6MTczMTc5NjE4Nn0._420RSuWmh241DFD2ZQqwrSqyN5ffs_KVBO198Y2Wgg"

curl -X POST http://localhost:5000/change_password -H 'Content-Type: application/json' "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbiI6ImJhciIsImV4cCI6MTczMTc5NjE4Nn0._420RSuWmh241DFD2ZQqwrSqyN5ffs_KVBO198Y2Wgg" 


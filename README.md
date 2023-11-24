# УРБАТОН

## запуск проекта
- создать в корне проекта файл .env (рядом с .env.tmplt)
- сбилдить docker-compose build
- запустить docker-compose up -d
- остановить docker-compose down -v
- 
## порты
- send_email port: 9001 
- auth port: 9000
- common_information_service port: 9002


## схема апи
### авторизация
- http://localhost/api/auth/login
- POST 
- data: {
    "login": "login",
    "password": "TaCmxJBwVq10"
}
- response: {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwMDc4MjcxNywianRpIjoiNDBmMGMxNDMtNTU2ZS00ZTZiLWEyNDgtZTY5YzA4MmU3ZTBhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Imxvc2lra2lAbWFpbC5ydSIsIm5iZiI6MTcwMDc4MjcxNywiZXhwIjoxNzAwNzgzNjE3fQ.PrxkKegwLWipVCyoE6FniEavzqn1W8kIlUweVo_8Z64",
    "first_name": "Сергей",
    "role_id": "2b618d72-cd4e-4f90-81d2-293599e50e5e"
}
### регистрация пользователя в системе
- http://localhost/api/auth/register_user
- POST
- data: {
    "first_name": "Иван",
    "last_name": "Пупкин",
    "email": "klosepsergey123@gmail.com",
    "phone_number": "89150000",
    "role": "ученик"
}
- response: {
    "email_send_to_user": true,
    "user_created": true
}
- один имейл можно использовать только один раз

### header
- http://localhost/api/auth/header
- GET
- response: {
    "user_name": user.first_name,
    "role_id": user.role_id
}

### добавить заявку 
- http://localhost/api/auth/new_order
- POST
- data: {
    "parent": 
    {
        "first_name": "Бабушка",
        "last_name": "Пети",
        "email": "babushka@email.com",
        "phone_number": "123"
    },
    "student": 
    {
        "first_name": "Петя",
        "last_name": "Дудец",
        "email": "babushka@email.com",
        "phone_number": "123"
    }
    
}
- response: {
    "user_created": true
}

### регистрация школы
- http://localhost/api/auth/register_school
- POST
- data: {
    "name": "Школа горлового ми..ре фа",
    "email": "losikki@mail.ru",
    "phone_number": "8888",
    "address": "сосулькина д.69"
}
- response: {
    "email_send_to_school": true,
    "school_created": true
}

### получение всех школ
- http://localhost/api/common_information/all_schools
- GET
- response: {
    "schools": [
        {
            "address": "сосулькина д.69",
            "email": "losikki@mail.ru",
            "name": "Школа горлового ми..ре фа",
            "phone_number": "8888"
        }
    ]
}
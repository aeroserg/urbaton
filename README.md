# УРБАТОН

## запуск проекта
- создать в корне проекта файл .env (рядом с .env.tmplt)
- сбилдить docker-compose build
- запустить docker-compose up -d
- остановить docker-compose down -v
- 
## порты
- send_email port: 9001 
- api port: 9000
- auth port: 9003
- orders: 9004
- common_information_service port: 9002


## схема апи
### авторизация
- http://localhost/api/login
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
- http://localhost/api/register_user
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
- http://localhost/api/header
- GET
- response: {
    "user_name": user.first_name,
    "role_id": user.role_id
}

### добавить заявку 
- http://localhost/api/new_order
- POST
- data: {
    "parent": 
    {
        "first_name": "Бабушка",
        "last_name": "Пети",
        "email": "babushka@email.com",
        "phone_number": "123",
        "school_id": 1
      },
      "student": 
      {
          "first_name": "Петя",
          "last_name": "Дудец",
          "email": "babushka@email.com",
          "phone_number": "123",
          "school_id": 1
      }
    
}
- response: {
    "user_created": true
}

### регистрация школы
- http://localhost/api/register_school
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
- http://localhost/api/all_schools
- GET
- response: {
    "schools": [
        {
            "id": 1,
            "address": "сосулькина д.69",
            "email": "losikki@mail.ru",
            "name": "Школа горлового ми..ре фа",
            "phone_number": "8888"
        }
    ]
}

### получение заявок
- http://localhost/api/orders
- GET
- ОБЯЗАТЕЛЬНО JWT ТОКЕН
- response: {
    "orders": [
        {
            "email": "babushka@email.com",
            "first_name": "Бабушка",
            "id": 6,
            "last_name": "Пети",
            "phone_number": "123"
        },
        {
            "email": "babushka@email.com",
            "first_name": "Петя",
            "id": 15,
            "last_name": "Дудец",
            "phone_number": "123"
        }
    ]
}
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


## схема апи
### авторизация
- http://localhost/api/login
- POST 
- data: {
    "email": "losikki@mail.ru",
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
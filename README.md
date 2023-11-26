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
- message_service port: 9005


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

### получение списка классов
- http://localhost/api/classes
- GET
- ОБЯЗАТЕЛЬНО JWT ТОКЕН
- response: {
    "classes": [
        {
            "class_name": "до"
        },
        {
            "class_name": "ре"
        }
    ]
}

### получение параллели
- http://localhost/api/grade
- GET
- ОБЯЗАТЕЛЬНО JWT ТОКЕН
- response: {
    "grades": [
        {
            "grade": 1
        },
        {
            "grade": 2
        }
    ]
}

### получение списка студентов для расписания
- http://localhost/api/students_for_timetable
- GET
- ОБЯЗАТЕЛЬНО JWT ТОКЕН
- response: {
    "grades": {
        "1": {
            "до": [
                {
                    "first_name": "Иван",
                    "id": 2
                }
            ],
            "ре": [
                {
                    "first_name": "Иван",
                    "id": 11
                },
                {
                    "first_name": "Иван",
                    "id": 12
                }
            ]
        },
        "2": {
            "до": [
                {
                    "first_name": "Наталья",
                    "id": 13
                }
            ],
            "ре": [
                {
                    "first_name": "Сергей",
                    "id": 14
                }
            ]
        },
        "3": {
            "до": [
                {
                    "first_name": "Сергей",
                    "id": 15
                }
            ],
            "ре": [
                {
                    "first_name": "Ирина",
                    "id": 16
                }
            ]
        },
        "4": {
            "до": [
                {
                    "first_name": "Василий",
                    "id": 17
                }
            ],
            "ре": [
                {
                    "first_name": "Генадий",
                    "id": 18
                }
            ]
        },
        "5": {
            "до": [
                {
                    "first_name": "Райан",
                    "id": 19
                }
            ],
            "ре": [
                {
                    "first_name": "Марго",
                    "id": 20
                }
            ]
        },
        "6": {
            "до": [
                {
                    "first_name": "Николай",
                    "id": 21
                }
            ],
            "ре": [
                {
                    "first_name": "Данила",
                    "id": 22
                }
            ]
        },
        "7": {
            "до": [
                {
                    "first_name": "Ольга",
                    "id": 23
                }
            ],
            "ре": [
                {
                    "first_name": "Ким",
                    "id": 24
                }
            ]
        }
    }
}

### получение преподавателей для расписания 
- http://localhost/api/tutors_for_timetable
- GET
- ОБЯЗАТЕЛЬНО JWT ТОКЕН
- response: {
    "tutors": [
        {
            "common_course_name": "сольфеджио",
            "first_name": "Ханс",
            "individual_course_name": "Саксофон",
            "last_name": "Циммер"
        },
        {
            "common_course_name": "сольфеджио",
            "first_name": "Антонио",
            "individual_course_name": "Баян",
            "last_name": "Вивальда"
        },
        {
            "common_course_name": "оркестр",
            "first_name": "Рихард",
            "individual_course_name": "Губная гармошка",
            "last_name": "Вагнер"
        },
        {
            "common_course_name": "история музыки",
            "first_name": "Луис",
            "individual_course_name": "Губная гармошка",
            "last_name": "Армстронг"
        },
        {
            "common_course_name": "хор",
            "first_name": "Френк",
            "individual_course_name": "Губная гармошка",
            "last_name": "Синатра"
        },
        {
            "common_course_name": "хор",
            "first_name": "Валерий",
            "individual_course_name": "Фортепино",
            "last_name": "Миладзе"
        },
        {
            "common_course_name": "история музыки",
            "first_name": "Мэйби",
            "individual_course_name": "Губная гармошка",
            "last_name": "Бэйби"
        }
    ]
}

### отправка письма
- http://localhost/api/send_message
- POST
- data:{
    "id_to": "2",
    "text": "сообщение"
}
- request:{
    "success": true
}

### получение писем
- http://localhost/api/get_messages
- GET
- ОБЯЗАТЕЛЬНО JWT ТОКЕН
- response:{
    "messages": [
        {
            "sender_first_name": "Виктор",
            "sender_last_name": "Цой",
            "text": "тест"
        }
    ]
}

### получение писем
- http://localhost/api/get_all_users
- GET
- ОБЯЗАТЕЛЬНО JWT ТОКЕН
- response:{
    "users": [
        {
            "first_name": "Школа горлового ми..ре фа",
            "id": 3,
            "last_name": "Школа горлового ми..ре фа",
            "role": "школа"
        },
        {
            "first_name": "Ким",
            "id": 24,
            "last_name": "Кардашьян",
            "role": "ученик"
        }
    ]
}
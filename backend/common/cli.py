# role1 = Role(id='642b6836-51f6-4ace-8e1e-8ff7b47e5719', role='школа')
# role2 = Role(id='78c2d488-d982-4e5b-a4ef-d105f67e6935', role='родитель')
# role3 = Role(id='2b618d72-cd4e-4f90-81d2-293599e50e5e', role='ученик')
# role4 = Role(id='abfa64e6-78c7-40de-ab54-bb442554b117', role='преподаватель')
# role5 = Role(id='2efcffdc-d012-4c6b-931b-52c0a6f14c70', role='админ')
# db.session.add_all(
#     [role5])
# db.session.commit()

# student1 = User(first_name='Иван', last_name='Антипов', password='antipov123', email='test@email.com', login='ivan_antipov', phone_number='1', role_id='2b618d72-cd4e-4f90-81d2-293599e50e5e')
# student2 = User(first_name='Иван', last_name='Абрамов', password='abramov123', email='test@email.com', login='ivan_abramov',
#                 phone_number='1', role_id='2b618d72-cd4e-4f90-81d2-293599e50e5e')
# student3 = User(first_name='Наталья', last_name='Агашкина', password='agashkina123', email='test@email.com', login='nataliya_agashkina',
#                 phone_number='1', role_id='2b618d72-cd4e-4f90-81d2-293599e50e5e')
# student4 = User(first_name='Сергей', last_name='Клосеп', password='klosep123', email='test@email.com', login='sergey_klosep',
#                 phone_number='1', role_id='2b618d72-cd4e-4f90-81d2-293599e50e5e')
# student5 = User(first_name='Сергей', last_name='Анненков', password='annenkov123', email='test@email.com', login='sergey_annenkov',
#                 phone_number='1', role_id='2b618d72-cd4e-4f90-81d2-293599e50e5e')
# student6 = User(first_name='Ирина', last_name='Катошкина', password='katoshkina123', email='test@email.com', login='irina_katashkina',
#                 phone_number='1', role_id='2b618d72-cd4e-4f90-81d2-293599e50e5e')
# student7 = User(first_name='Василий', last_name='Попов', password='popov123', email='test@email.com', login='vasya_popov',
#                 phone_number='1', role_id='2b618d72-cd4e-4f90-81d2-293599e50e5e')
# student8 = User(first_name='Генадий', last_name='Букин', password='bukin123', email='test@email.com', login='gena_bukin',
#                 phone_number='1', role_id='2b618d72-cd4e-4f90-81d2-293599e50e5e')
# student9 = User(first_name='Райан', last_name='Гослинг', password='rayan123', email='test@email.com', login='rayan_gosling',
#                 phone_number='1', role_id='2b618d72-cd4e-4f90-81d2-293599e50e5e')
# student10 = User(first_name='Марго', last_name='Робби', password='robby123', email='test@email.com', login='margo_robby',
#                 phone_number='1', role_id='2b618d72-cd4e-4f90-81d2-293599e50e5e')
# student11 = User(first_name='Николай', last_name='Воронин', password='voronin123', email='test@email.com', login='nikolay_voronin',
#                 phone_number='1', role_id='2b618d72-cd4e-4f90-81d2-293599e50e5e')
# student12 = User(first_name='Данила', last_name='Богров', password='danila123', email='test@email.com', login='danila_bogrov',
#                 phone_number='1', role_id='2b618d72-cd4e-4f90-81d2-293599e50e5e')
# student13 = User(first_name='Ольга', last_name='Бузова', password='buzova123', email='test@email.com', login='olga_buzova',
#                 phone_number='1', role_id='2b618d72-cd4e-4f90-81d2-293599e50e5e')
# student14 = User(first_name='Ким', last_name='Кардашьян', password='kardashyan123', email='test@email.com', login='kim_kardashyan',
#                 phone_number='1', role_id='2b618d72-cd4e-4f90-81d2-293599e50e5e')
#
# db.session.add_all(
#     [student1, student2, student3, student4, student5, student6, student7, student8, student9, student10,
#      student11, student12, student13, student14])
# db.session.commit()

# tutor1 = User(first_name='Дени', last_name='Вильнев', password='vilnev123', email='test@email.com', login='deny_vilnev',
#                  phone_number='1', role_id='abfa64e6-78c7-40de-ab54-bb442554b117')
# tutor2 = User(first_name='Ханс', last_name='Циммер', password='zimmer123', email='test@email.com',
#               login='hans_zimmer',
#               phone_number='1', role_id='abfa64e6-78c7-40de-ab54-bb442554b117')
# tutor3 = User(first_name='Игорь', last_name='Моисеев', password='moiseev123', email='test@email.com',
#               login='igor_moiseev',
#               phone_number='1', role_id='abfa64e6-78c7-40de-ab54-bb442554b117')
# tutor4 = User(first_name='Антонио', last_name='Вивальда', password='vivaldy123', email='test@email.com',
#               login='antonio_vivaldy',
#               phone_number='1', role_id='abfa64e6-78c7-40de-ab54-bb442554b117')
# tutor5 = User(first_name='Рихард', last_name='Вагнер', password='vagner123', email='test@email.com',
#               login='richard_vagner',
#               phone_number='1', role_id='abfa64e6-78c7-40de-ab54-bb442554b117')
# tutor6 = User(first_name='Луис', last_name='Армстронг', password='armstrong123', email='test@email.com',
#               login='luis_armstrong',
#               phone_number='1', role_id='abfa64e6-78c7-40de-ab54-bb442554b117')
# tutor7 = User(first_name='Френк', last_name='Синатра', password='sinatra123', email='test@email.com',
#               login='frank_sinatra',
#               phone_number='1', role_id='abfa64e6-78c7-40de-ab54-bb442554b117')
# tutor8 = User(first_name='Валерий', last_name='Миладзе', password='miladze123', email='test@email.com',
#               login='valery_miladze',
#               phone_number='1', role_id='abfa64e6-78c7-40de-ab54-bb442554b117')
# tutor9 = User(first_name='Мэйби', last_name='Бэйби', password='baby123', email='test@email.com',
#               login='maybe_baby',
#               phone_number='1', role_id='abfa64e6-78c7-40de-ab54-bb442554b117')
# tutor10 = User(first_name='Виктор', last_name='Цой', password='tsoi123', email='test@email.com',
#               login='viktor_tsoi',
#               phone_number='1', role_id='abfa64e6-78c7-40de-ab54-bb442554b117')

# ed1 = EducationYear()
# ed2 = EducationYear()
# ed3 = EducationYear()
# ed4 = EducationYear()
# ed5 = EducationYear()
# ed6 = EducationYear()
# ed7 = EducationYear()

# cc1 = CourseCommon(name='хор')
# cc2 = CourseCommon(name='солльфеджио')
# cc3 = CourseCommon(name='оркестр')
# cc4 = CourseCommon(name='история музыки')

# ci1 = CourseIndividual(name='Фортепино')
# ci2 = CourseIndividual(name='Саксофон')
# ci3 = CourseIndividual(name='Баян')
# ci4 = CourseIndividual(name='Губная гармошка')

# c1 = Class(id='до')
# c2 = Class(id='ре')

# tcc1 = TutorCourseCommonRelationship(tutor_id=26, course_id=2)
# tcc2 = TutorCourseCommonRelationship(tutor_id=28, course_id=3)
# tcc3 = TutorCourseCommonRelationship(tutor_id=29, course_id=4)
# tcc4 = TutorCourseCommonRelationship(tutor_id=30, course_id=4)
# tcc5 = TutorCourseCommonRelationship(tutor_id=31, course_id=4)
# tcc6 = TutorCourseCommonRelationship(tutor_id=31, course_id=1)
# tcc7 = TutorCourseCommonRelationship(tutor_id=32, course_id=1)
# tcc8 = TutorCourseCommonRelationship(tutor_id=33, course_id=4)
# tcc9 = TutorCourseCommonRelationship(tutor_id=28, course_id=2)
# tcc10 = TutorCourseCommonRelationship(tutor_id=29, course_id=3)

# tci1 = TutorCourseIndividualRelationship(tutor_id=26, course_id=2)
# tci2 = TutorCourseIndividualRelationship(tutor_id=28, course_id=3)
# tci3 = TutorCourseIndividualRelationship(tutor_id=29, course_id=4)
# tci4 = TutorCourseIndividualRelationship(tutor_id=30, course_id=4)
# tci5 = TutorCourseIndividualRelationship(tutor_id=31, course_id=4)
# tci6 = TutorCourseIndividualRelationship(tutor_id=31, course_id=1)
# tci7 = TutorCourseIndividualRelationship(tutor_id=32, course_id=1)
# tci8 = TutorCourseIndividualRelationship(tutor_id=33, course_id=4)
# tci9 = TutorCourseIndividualRelationship(tutor_id=28, course_id=2)
# tci10 = TutorCourseIndividualRelationship(tutor_id=29, course_id=3)

# se1 = StudentEducationYearRelationship(student_id=2, education_year=1)
# se2 = StudentEducationYearRelationship(student_id=11, education_year=1)
# se3 = StudentEducationYearRelationship(student_id=12, education_year=1)
# se4 = StudentEducationYearRelationship(student_id=13, education_year=2)
# se5 = StudentEducationYearRelationship(student_id=14, education_year=2)
# se6 = StudentEducationYearRelationship(student_id=15, education_year=3)
# se7 = StudentEducationYearRelationship(student_id=16, education_year=3)
# se8 = StudentEducationYearRelationship(student_id=17, education_year=4)
# se9 = StudentEducationYearRelationship(student_id=18, education_year=4)
# se10 = StudentEducationYearRelationship(student_id=19, education_year=5)
# se11 = StudentEducationYearRelationship(student_id=20, education_year=5)
# se12 = StudentEducationYearRelationship(student_id=21, education_year=6)
# se13 = StudentEducationYearRelationship(student_id=22, education_year=6)
# se14 = StudentEducationYearRelationship(student_id=23, education_year=7)
# se15 = StudentEducationYearRelationship(student_id=24, education_year=7)

# cs1 = ClassStudentRelation(student_id=2, class_id="до")
# cs2 = ClassStudentRelation(student_id=11, class_id="ре")
# cs3 = ClassStudentRelation(student_id=12, class_id="ре")
# cs4 = ClassStudentRelation(student_id=13, class_id="до")
# cs5 = ClassStudentRelation(student_id=14, class_id="ре")
# cs6 = ClassStudentRelation(student_id=15, class_id="до")
# cs7 = ClassStudentRelation(student_id=16, class_id="ре")
# cs8 = ClassStudentRelation(student_id=17, class_id="до")
# cs9 = ClassStudentRelation(student_id=18, class_id="ре")
# cs10 = ClassStudentRelation(student_id=19, class_id="до")
# cs11 = ClassStudentRelation(student_id=20, class_id="ре")
# cs12 = ClassStudentRelation(student_id=21, class_id="до")
# cs13 = ClassStudentRelation(student_id=22, class_id="ре")
# cs14 = ClassStudentRelation(student_id=23, class_id="до")
# cs15 = ClassStudentRelation(student_id=24, class_id="ре")
#
#
# us1 = UsersSchool(school_id=1, user_id=2)
# us2 = UsersSchool(school_id=1, user_id=11)
# us3 = UsersSchool(school_id=1, user_id=12)
# us4 = UsersSchool(school_id=1, user_id=13)
# us5 = UsersSchool(school_id=1, user_id=14)
# us6 = UsersSchool(school_id=1, user_id=15)
# us7 = UsersSchool(school_id=1, user_id=16)
# us8 = UsersSchool(school_id=1, user_id=17)
# us9 = UsersSchool(school_id=1, user_id=18)
# us10 = UsersSchool(school_id=1, user_id=19)
# us11 = UsersSchool(school_id=1, user_id=20)
# us12 = UsersSchool(school_id=1, user_id=21)
# us13 = UsersSchool(school_id=1, user_id=22)
# us14 = UsersSchool(school_id=1, user_id=23)
# us15 = UsersSchool(school_id=1, user_id=24)
# us16 = UsersSchool(school_id=1, user_id=25)
# us17 = UsersSchool(school_id=1, user_id=26)
# us18 = UsersSchool(school_id=1, user_id=27)
# us19 = UsersSchool(school_id=1, user_id=28)
# us20 = UsersSchool(school_id=1, user_id=29)
# us21 = UsersSchool(school_id=1, user_id=30)
# us22 = UsersSchool(school_id=1, user_id=31)
# us23 = UsersSchool(school_id=1, user_id=32)
# us24 = UsersSchool(school_id=1, user_id=33)
# us25 = UsersSchool(school_id=1, user_id=34)
# u = User(first_name='Анастасия', last_name='Максимова', password='mama123', email='test@email.com',
#                       login='best_mama',
#                       phone_number='1', role_id='78c2d488-d982-4e5b-a4ef-d105f67e6935')
# db.session.add_all(
#     [cs1, cs2, cs3, cs4, cs5, cs6, cs7, cs8, cs9, cs10, cs11, cs12, cs13, cs14, cs15])
# db.session.commit()
import os
from collections import defaultdict

from dotenv import load_dotenv
if os.path.exists('../../.env'):
    load_dotenv('../../.env')
else:
    load_dotenv('.env')

SERVICE_PORT = os.getenv("COMMON_SERVICE_PORT")

from concurrent import futures
import datetime

import grpc
import common_pb2_grpc
from common_pb2 import (School, SchoolsResponse, GetClassResponse, Class, GetEducationYearResponse,
                        EducationYear, Grades, GradeFullInfo, Classes, Students, GetStudentsResponse,
                        Tutor, GetTutorResponse, User, GetUsersResponse, StudentMarks, GetTutorsStudentResponse,
                        GetParentStudentResponse)

from work_with_db import (get_schools, get_classes, get_education_years, get_students, get_tutors,
                          get_users, get_tutors_student, get_user, get_parents_student)


class CommonServiceServicer(common_pb2_grpc.CommonServiceServicer):
    def Schools(self, request, context):
        schools = get_schools()

        response = []

        for school in schools:
            response.append(
                School(
                    id=school.id,
                    name=school.name,
                    email=school.email,
                    phone_number=school.phone_number,
                    address=school.address
                )
            )

        return SchoolsResponse(schools=response)

    def GetClass(self, request, context):
        classes = get_classes()

        response = []

        for class_name in classes:
            response.append(
                Class(
                    class_name=class_name.id
                )
            )

        return GetClassResponse(classes=response)

    def GetEducationYear(self, request, context):
        education_years = get_education_years()

        response = []

        for year in education_years:
            response.append(
                EducationYear(
                    education_year=year.id
                )
            )

        return GetEducationYearResponse(education_years=response)

    def GetStudents(self, request, context):
        login = request.login

        students = get_students(login)

        result = Grades()

        # Используем defaultdict для удобства группировки данных
        grouped_data = defaultdict(lambda: defaultdict(list))

        for entry in students:
            grade = entry.get('grade', 0)
            class_name = entry.get('class_name') or entry.get('class_id') or 'Unknown'

            student_info = Students(
                first_name=entry.get('first_name', ''),
                last_name=entry.get('last_name', ''),
                id=entry.get('id', 0)
            )

            grouped_data[grade][class_name].append(student_info)

        for grade, classes in grouped_data.items():
            grade_info = GradeFullInfo(
                grade=grade,
                classes=[Classes(class_name=name, students=students) for name, students in classes.items()]
            )
            result.grade_full_info.append(grade_info)

        return GetStudentsResponse(grades=[result])

    def GetTutor(self, request, context):
        login = request.login

        tutors = get_tutors(login)

        response = []

        first_name_list = []

        for tutor in tutors:
            if tutor.common_course_name is not None and tutor.first_name not in first_name_list:
                response.append(
                    Tutor(
                        first_name=tutor.first_name,
                        last_name=tutor.last_name,
                        common_course_name=tutor.common_course_name,
                        individual_course_name=tutor.individual_course_name
                    )
                )
                first_name_list.append(tutor.first_name)

        return GetTutorResponse(tutors=response)

    def GetUser(self, request, context):
        users = get_users()

        response = []

        for first_name, last_name, id, role in users:
            response.append(
                User(
                    first_name=first_name,
                    last_name=last_name,
                    role=role,
                    id=id
                )
            )

        return GetUsersResponse(users=response)

    def GetTutorsStudent(self, request, context):
        login = request.login

        tutor = get_user(login=login)
        students = get_tutors_student(tutor.id)

        response = []
        for student in students:
            response.append(
                StudentMarks(
                    first_name=student["first_name"],
                    last_name=student["last_name"],
                    id=student["id"],
                    mark=student["marks"][0]
                )
            )

        return GetTutorsStudentResponse(student_marks=response)

    def GetParentStudent(self, request, context):
        login = request.login

        parent = get_user(login=login)
        children = get_parents_student(parent_id=parent.id)

        result = []
        for first_name, last_name, user_id in children:
            result.append(
                Students(
                    first_name=first_name,
                    last_name=last_name,
                    id=user_id
                ))

        return GetParentStudentResponse(students=result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    common_pb2_grpc.add_CommonServiceServicer_to_server(CommonServiceServicer(), server)
    server.add_insecure_port(f'[::]:{SERVICE_PORT}')
    server.start()
    print(str(datetime.datetime.now()) + f"Server started, listening on port: {SERVICE_PORT}")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

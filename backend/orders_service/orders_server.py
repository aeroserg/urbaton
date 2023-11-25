@app.route('/new_order', methods=['POST'])
def new_order():
    data = request.get_json()

    parent = data.get('parent')
    student = data.get('student')

    parent_order = Order(
        first_name=parent['first_name'],
        last_name=parent['last_name'],
        email=parent['email'],
        phone_number=parent['phone_number']
    )
    db.session.add(parent_order)
    db.session.commit()

    parent_order_school = OrderSchoolRelationship(order_id=parent_order.id, school_id=parent['school_id'])
    db.session.add(parent_order_school)
    db.session.commit()

    student_order = Order(
        first_name=student['first_name'],
        last_name=student['last_name'],
        email=student['email'],
        phone_number=student['phone_number']
    )
    db.session.add(student_order)
    db.session.commit()

    parent_order_school = OrderSchoolRelationship(order_id=student_order.id, school_id=parent['school_id'])
    db.session.add(parent_order_school)
    db.session.commit()

    parent_student_relationship = ParentStudentRelationshipOrder(parent_id=parent_order.id, student_id=student_order.id)
    db.session.add(parent_student_relationship)
    db.session.commit()

    return {'user_created': True}, 200
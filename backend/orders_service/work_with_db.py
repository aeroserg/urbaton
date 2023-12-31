from backend.common.models import (Order, OrderSchoolRelationship,
                                   ParentStudentRelationshipOrder, User, UsersSchool, app, db)


def add_order(first_name, last_name, email, phone_number):
    with app.app_context():
        order = Order(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number
        )
        db.session.add(order)
        db.session.commit()
        print(order.id)
        return order


def order_school_relation(user_order_id, user_school_id):
    with app.app_context():
        parent_order_school = OrderSchoolRelationship(order_id=user_order_id, school_id=user_school_id)
        db.session.add(parent_order_school)
        db.session.commit()

    return parent_order_school


def parent_student_order_relationship(parent_order_id, student_order_id):
    with app.app_context():
        parent_student_relationship = ParentStudentRelationshipOrder(parent_id=parent_order_id,
                                                                     student_id=student_order_id)
        db.session.add(parent_student_relationship)
        db.session.commit()

    return parent_student_relationship


def get_users_school(login):
    with app.app_context():
        user = (
            db.session.query(User, UsersSchool)
            .join(UsersSchool, User.id == UsersSchool.user_id)
            .filter(User.login == login)
            .first()
        )

        print(user.UsersSchool.school_id)
        return user.UsersSchool.school_id


def get_orders(school_id):
    with app.app_context():
        orders = (
            db.session.query(Order)
            .join(OrderSchoolRelationship, Order.id == OrderSchoolRelationship.order_id)
            .filter(OrderSchoolRelationship.school_id == school_id, Order.accepted == False)
            .all()
        )
        print(orders)
        return orders

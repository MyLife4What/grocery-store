from models.customer_model import CustomerModel
from sqlalchemy.orm.session import Session


class CustomerDao:
    def __init__(self, session: Session):
        self.__session = session

    def get_all_customer(self):
        return self.__session.query(CustomerModel).all()

    def get_customer_by_id(self, id):
        return self.__session.query(CustomerModel).filter(CustomerModel.id == id)[0]

    def get_customer_by_name(self, name):
        return self.__session.query(CustomerModel).filter(CustomerModel.name == name).all()

    def get_customer_by_gender(self, gender):
        return self.__session.query(CustomerModel).filter(CustomerModel.gender == gender).all()

    def get_customer_by_member_rank(self, rank):
        return self.__session.query(CustomerModel).filter(CustomerModel.member_rank == rank).all()

    def create_new_customer(self, customer: CustomerModel):
        self.__session.add(customer)
        self.__session.commit()
        print("New customer has been added to database!")
        print(customer)
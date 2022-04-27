from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.dao.product_dao import ProductDao
from utils.dao.customer_dao import CustomerDao


class GroceryStore:

    def __init__(self, connection_url="sqlite:///grocery_store.db"):
        engine = create_engine(connection_url)
        session = sessionmaker(bind=engine)
        self.__db_session = session()

    def product(self):
        return ProductDao(self.__db_session)

    def customer(self):
        return CustomerDao(self.__db_session)
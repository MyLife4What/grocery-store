from models.product_model import ProductModel
from sqlalchemy.orm.session import Session


class ProductDao:
    def __init__(self, session: Session):
        self.__session = session

    def get_all_products(self):
        return self.__session.query(ProductModel).all()

    def get_product_by_id(self, id):
        return self.__session.query(ProductModel).filter(ProductModel.product_id == id)[0]

    def get_product_by_name(self, product):
        return self.__session.query(ProductModel).filter(ProductModel.product == product).all()

    def get_product_by_sort_price(self):
        product_list = self.get_all_product()
        return sorted(product_list, key=lambda product: product.price)

    def get_product_by_sort_quantity(self):
        product_list = self.get_all_product()
        return sorted(product_list, key=lambda product: product.quantity)

    def create_new_product(self, product: ProductModel):
        self.__session.add(product)
        self.__session.commit()
        print("New product has been added to database!")
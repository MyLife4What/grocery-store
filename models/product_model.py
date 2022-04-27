from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class ProductModel(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, nullable=False)
    product = Column(Text, nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f"<Products: (id={self.product_id},name={self.product},price={self.price},quantity={self.quantity}>"

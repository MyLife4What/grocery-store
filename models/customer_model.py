from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class CustomerModel(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Text, nullable=False)
    gender = Column(Text, nullable=False)
    member_rank = Column(Text, nullable=False)
    product_id = Column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f"<Customers: (id={self.id},name={self.name},gender={self.gender},member-rank={self.member_rank}, " \
               f"product={self.product_id}> "

from infra.db.tables.customer import Customer
from infra.db.repository.customer_repository import CustomerRepository


class CustomerService():

    def __init__(self):
        self.__repository = CustomerRepository()

    def get_all(self):
        return self.__repository.get_all()

    def get_by_id(self, id):
        return self.__repository.get_by_id(id=id)

    def create(self, name):
        new_customer = Customer(name=name)
        return self.__repository.create(new_customer)

    def update(self, id, name):
        customer_info = self.__repository.get_by_id(id=id)

        if customer_info:
            entity = Customer(id=id, name=name)
            query_info = self.__repository.update(entity)
        else:
            query_info = f"Customer with id={id} not found"

        return query_info

    def delete(self, id):
        customer_info = self.__repository.get_by_id(id=id)

        if customer_info:
            query_info = self.__repository.delete(id=id)
        else:
            query_info = f"Customer with id={id} not found"

        return query_info

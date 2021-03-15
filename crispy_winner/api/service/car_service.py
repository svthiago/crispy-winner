from infra.db.tables.car import Car
from infra.db.tables.customer import Customer
from infra.db.repository.car_repository import CarRepository


class CarService():

    def __init__(self):
        self.repository = CarRepository()

    def get_all(self):
        return self.repository.get_all()
    
    def get_by_id(self, id):

        query = self.repository.get_by_id(id=id)

        return query._asdict()

    def get_all_cars_and_customers(self):
        return CarRepository().get_all_cars_and_customers()

    def get_cars_from_customer(self, customer_id):
        return CarRepository().get_cars_from_customer(customer_id=customer_id)

    def create(self, customer_id, model, color):
        car_amount = self.repository.get_count_by_customer_id(customer_id=customer_id)

        if car_amount < 3:
            new_car = Car(customer_id=customer_id, model=model, color=color)
            query_info = self.repository.create(new_car)
        else:
            query_info = f"Customer with id={customer_id} already have 3 cars"

        return query_info


    def update(self, id, customer_id, model, color):
        car_info = self.repository.get_by_id(id=id)
        car_amount = self.repository.get_count_by_customer_id(customer_id=customer_id)

        if car_amount < 3:
            if car_info:
                entity = Car(id=car_info['id'], model=model, color=color)
                query_info = self.repository.update(entity)
            else:
                query_info = f"Car with id={id} not found"
        else:
            query_info = f"Customer with id={customer_id} already have 3 cars"

        return query_info


    def update_color(self, id, color):
        car_info = self.repository.get_by_id(id=id)

        if car_info:
            entity = Car(id=car_info['id'], color=color)
            query_info = self.repository.update(entity)
        else:
            query_info = f"Car with id={id} not found"

        return query_info

    def update_owner(self, id, customer_id):
        car_info = self.repository.get_all()
        car_amount = cars_owned(car_info, customer_id)

        if car_amount < 3:
            car_info = self.repository.get_by_id(id=id)

            if car_info:
                entity = Customer(id=car_info.id, customer_id=customer_id)
                query_info = self.repository.update(entity)
            else:
                query_info = f"Car with id={id} not found"

        else:
            query_info = f"Customer with id={customer_id} already have 3 cars"

        return query_info

    def delete(self, id):
        car_info = self.repository.get_by_id(id=id)

        if car_info:
            query_info = self.repository.delete(id=car_info.id)
        else:
            query_info = f"Car with id={id} not found"

        return query_info

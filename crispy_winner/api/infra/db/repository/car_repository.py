from infra.db.repository.repository import Repository
from infra.db.tables.customer import Customer
from infra.db.tables.car import Car

from utils.parse import attr_aparse


class CarRepository(Repository):

   def __init__(self):
      super().__init__(Car)

   def get_count_by_customer_id(self, customer_id):
      query = self.ses.query(self.table_model).filter_by(self.table_model.customer_id == customer_id).count()
      self.ses.flush()

      return query

   def get_cars_by_customer_id(self, customer_id):
      query = self.ses.query(self.table_model).filter_by(customer_id=customer_id).all()
      self.ses.flush()

      return query
   
   def get_all_cars_and_customers(self):
      query = self.ses.query(Car, Customer).join(Customer).all()
      self.ses.flush()

      query_dicts = []

      for row in query:
         row_dict = row._asdict()
         print(row_dict)
         car_dict = row_dict['Car']._asdict()

         person_dict = row_dict['Customer']._asdict()
         car_dict['owner'] = person_dict['name']
         query_dicts.append(car_dict)

      return query_dicts

   def get_cars_from_customer(self, customer_id):

      query = self.ses.query(Car, Customer).join(Customer).filter_by(id=customer_id).all()
      self.ses.flush()

      query_dicts = []

      for row in query:
         row_dict = row._asdict()
         car_dict = row_dict['Car']._asdict()

         person_dict = row_dict['Customer']._asdict()
         car_dict['owner'] = person_dict['name']
         query_dicts.append(car_dict)

      return query_dicts


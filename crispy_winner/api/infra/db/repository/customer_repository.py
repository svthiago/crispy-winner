from infra.db.repository.repository import Repository
from infra.db.tables.customer import Customer
from infra.db.tables.car import Car


class CustomerRepository(Repository):

      def __init__(self):
         super().__init__(Customer)


      def get_sale_opportunities(self):
         query = self.ses.query(Customer).filter(Customer.id == Car.customer_id).all()

         return query
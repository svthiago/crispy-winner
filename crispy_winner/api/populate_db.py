from infra.db.config import Session
from infra.db.config import Base
from infra.db.config import eng

from infra.db.tables.car import Car
from infra.db.tables.customer import Customer


Base.metadata.drop_all(eng)
Base.metadata.create_all(eng)

ses = Session()
try:

    ses.add(Customer(name='Marcelo'))
    ses.add(Customer(name='Rodrigo'))
    ses.add(Customer(name='Thiago'))
    ses.add(Customer(name='Caio'))

    ses.add(Car(customer_id=1, model='hatch', color='gray'))
    ses.add(Car(customer_id=1, model='sedan', color='yellow'))
    ses.add(Car(customer_id=1, model='convertible', color='blue'))

    ses.add(Car(customer_id=2, model='sedan',color='blue'))
    ses.add(Car(customer_id=2, model='hatch',  color='yellow'))
    ses.add(Car(customer_id=2, model='convertible', color='gray'))

    ses.add(Car(customer_id=3, model='hatch', color='blue'))

    ses.add(Car(customer_id=4, model='convertible', color='yellow'))
    ses.add(Car(customer_id=4, model='sedan', color='gray'))

    ses.commit()

except:
    # on rollback, the same closure of state
    # as that of commit proceeds.
    ses.rollback()
    raise
finally:
    # close the Session.  This will expunge any remaining
    # objects as well as reset any existing SessionTransaction
    # state.  Neither of these steps are usually essential.
    # However, if the commit() or rollback() itself experienced
    # an unanticipated internal failure (such as due to a mis-behaved
    # user-defined event handler), .close() will ensure that
    # invalid state is removed.
    ses.close()

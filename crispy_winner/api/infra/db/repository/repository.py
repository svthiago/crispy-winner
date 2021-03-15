from infra.db.config import Session


error_message = {'message': 'Query failed, try again.'}

class Repository():

    def __init__(self, table_model):
        self.table_model = table_model

    def get_all(self):

        session = Session()
        try:
            query = [ row._asdict() for row in session.query(self.table_model).filter_by().all() ]

        except:
            # on rollback, the same closure of state
            # as that of commit proceeds.
            session.rollback()

            query = error_message

            raise
        finally:
            # close the Session.  This will expunge any remaining
            # objects as well as reset any existing SessionTransaction
            # state.  Neither of these steps are usually essential.
            # However, if the commit() or rollback() itself experienced
            # an unanticipated internal failure (such as due to a mis-behaved
            # user-defined event handler), .close() will ensure that
            # invalid state is removed.
            session.close()

        return query

    def get_by_id(self, id):

        session = Session()
        try:

            query = session.query(self.table_model).filter_by(id=id).first()
            query = query._asdict()

        except:
            # on rollback, the same closure of state
            # as that of commit proceeds.
            session.rollback()

            query = error_message
            raise
        finally:
            # close the Session.  This will expunge any remaining
            # objects as well as reset any existing SessionTransaction
            # state.  Neither of these steps are usually essential.
            # However, if the commit() or rollback() itself experienced
            # an unanticipated internal failure (such as due to a mis-behaved
            # user-defined event handler), .close() will ensure that
            # invalid state is removed.
            session.close()

        return query

        

    def create(self, entity):

        session = Session()
        try:

            session.add(entity)
            session.commit()

            query = entity._asdict()

        except:
            # on rollback, the same closure of state
            # as that of commit proceeds.
            session.rollback()

            query = error_message

            raise
        finally:
            # close the Session.  This will expunge any remaining
            # objects as well as reset any existing SessionTransaction
            # state.  Neither of these steps are usually essential.
            # However, if the commit() or rollback() itself experienced
            # an unanticipated internal failure (such as due to a mis-behaved
            # user-defined event handler), .close() will ensure that
            # invalid state is removed.
            session.close()

        return query


    def update(self, entity):

        session = Session()

        try:

            session.merge(entity)

            query = entity._asdict()

        except:
            # on rollback, the same closure of state
            # as that of commit proceeds.
            session.rollback()

            query = error_message

            raise
        finally:
            # close the Session.  This will expunge any remaining
            # objects as well as reset any existing SessionTransaction
            # state.  Neither of these steps are usually essential.
            # However, if the commit() or rollback() itself experienced
            # an unanticipated internal failure (such as due to a mis-behaved
            # user-defined event handler), .close() will ensure that
            # invalid state is removed.
            session.close()

        return query


    def delete(self, id):

        session = Session()

        try:

            entity = session.query(self.table_model).filter_by(id=id).first()
            session.query(self.table_model).filter_by(id=id).delete()

            query = entity._asdict()

        except:
            # on rollback, the same closure of state
            # as that of commit proceeds.
            session.rollback()

            query = error_message

            raise
        finally:
            # close the Session.  This will expunge any remaining
            # objects as well as reset any existing SessionTransaction
            # state.  Neither of these steps are usually essential.
            # However, if the commit() or rollback() itself experienced
            # an unanticipated internal failure (such as due to a mis-behaved
            # user-defined event handler), .close() will ensure that
            # invalid state is removed.
            session.close()

        return query

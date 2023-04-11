from .db_init import get_session_maker


def session(fun):
    def wrapper(*args, **kwargs):
        session_maker = get_session_maker()
        s = session_maker()
        try:
            result = fun(s, *args, **kwargs)
            s.commit()
            return result
        except Exception as e:
            s.rollback()
            raise e
        finally:
            s.close()
    return wrapper

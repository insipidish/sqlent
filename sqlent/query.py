from functools import wraps
from .helpers import proper_where_value, where_as_string

def newobj(method):
    @wraps(method)
    # Well, newobj can be decorated with function, but we will cover the case
    # where it decorated with method
    def inner(self, *args, **kwargs):
        obj = self.__class__.__new__(self.__class__)
        obj.__dict__ = self.__dict__.copy()
        method(obj, *args, **kwargs)
        return obj
    return inner

class Query(object):
    def __init__(self):
        self._query_type = None
        self._column_list = None
        self._table = None
        self._where_as_string_list = []

    @newobj
    def select(self, columns = None):
        self._query_type = 'SELECT'
        self._column_list = columns

    @newobj
    def table(self, table_name):
        self._table = table_name

    @newobj
    def field(self, field):
        self._column_list.append(field)

    def to_string(self):
        assert(self._query_type is not None)
        assert(self._table is not None)
        if (self._query_type == 'SELECT'):
            query = 'SELECT {cols} FROM {table}'.format(
                cols = self.cols_to_string(),
                table = self._table )
        if (len(self._where_as_string_list) < 1):
            return query
        else:
            return query + " WHERE " + " AND ".join(self._where_as_string_list)

    def cols_to_string(self):
        if self._column_list:
            return ', '.join(self._column_list)
        return '*'

    @newobj
    def where(self, *args):
        if len(args) == 2:
            col_name, value = args
            symbol = '='
        else:
            col_name, symbol, value = args
        self._where_as_string_list.append(where_as_string(col_name, symbol, value))

    @newobj
    def where_not(self, col_name, symbol, value):
        self._where_as_string_list.append("NOT " + where_as_string(col_name, symbol, value))

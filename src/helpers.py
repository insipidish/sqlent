import types, collections

def proper_where_value(val):
    if (isinstance(val, str)):
        return "'{}'".format(val)
    elif isinstance(val, collections.Iterable):
        return "({list})".format(list = ", ".join([str(proper_where_value(item)) for item in val]))
    return val

def where_as_string(col_name, symbol, value):
    return "{col} {symbol} {value}".format(
                col = col_name,
                value = proper_where_value(value),
                symbol = symbol)

def row_to_namedtuple(nt_cls, row):
    return nt_cls(*(row[f] for f in nt_cls._fields))

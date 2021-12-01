class NotPreparedError(Exception):
    def __str__(self):
        return 'Not prepared'


class NoSizeTableError(Exception):
    def __str__(self):
        return 'No size table'
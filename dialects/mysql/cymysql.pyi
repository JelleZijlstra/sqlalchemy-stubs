# Stubs for sqlalchemy.dialects.mysql.cymysql (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from .mysqldb import MySQLDialect_mysqldb as MySQLDialect_mysqldb
from .base import BIT as BIT, MySQLDialect as MySQLDialect

class _cymysqlBIT(BIT):
    def result_processor(self, dialect, coltype): ...

class MySQLDialect_cymysql(MySQLDialect_mysqldb):
    driver = ...  # type: str
    description_encoding = ...  # type: Any
    supports_sane_rowcount = ...  # type: bool
    supports_sane_multi_rowcount = ...  # type: bool
    supports_unicode_statements = ...  # type: bool
    colspecs = ...  # type: Any
    @classmethod
    def dbapi(cls): ...
    def is_disconnect(self, e, connection, cursor): ...

dialect = ...  # type: Any

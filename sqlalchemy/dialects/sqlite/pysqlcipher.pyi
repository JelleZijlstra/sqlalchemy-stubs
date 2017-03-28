# Stubs for sqlalchemy.dialects.sqlite.pysqlcipher (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from .pysqlite import SQLiteDialect_pysqlite as SQLiteDialect_pysqlite
from ...engine import url as _url

class SQLiteDialect_pysqlcipher(SQLiteDialect_pysqlite):
    driver = ...  # type: str
    pragmas = ...  # type: Any
    @classmethod
    def dbapi(cls): ...
    @classmethod
    def get_pool_class(cls, url): ...
    def connect(self, *cargs, **cparams): ...
    def create_connect_args(self, url): ...

dialect = ...  # type: Any
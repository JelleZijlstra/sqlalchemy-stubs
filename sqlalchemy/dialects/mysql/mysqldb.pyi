# Stubs for sqlalchemy.dialects.mysql.mysqldb (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .base import MySQLDialect as MySQLDialect, MySQLExecutionContext as MySQLExecutionContext, MySQLCompiler as MySQLCompiler, MySQLIdentifierPreparer as MySQLIdentifierPreparer
from .base import TEXT as TEXT

class MySQLExecutionContext_mysqldb(MySQLExecutionContext):
    @property
    def rowcount(self): ...

class MySQLCompiler_mysqldb(MySQLCompiler):
    def visit_mod_binary(self, binary, operator, **kw): ...
    def post_process_text(self, text): ...

class MySQLIdentifierPreparer_mysqldb(MySQLIdentifierPreparer): ...

class MySQLDialect_mysqldb(MySQLDialect):
    driver = ...  # type: str
    supports_unicode_statements = ...  # type: bool
    supports_sane_rowcount = ...  # type: bool
    supports_sane_multi_rowcount = ...  # type: bool
    supports_native_decimal = ...  # type: bool
    default_paramstyle = ...  # type: str
    execution_ctx_cls = ...  # type: Any
    statement_compiler = ...  # type: Any
    preparer = ...  # type: Any
    server_side_cursors = ...  # type: Any
    def __init__(self, server_side_cursors: bool = ..., **kwargs) -> None: ...
    def supports_server_side_cursors(self): ...
    @classmethod
    def dbapi(cls): ...
    def do_executemany(self, cursor, statement, parameters, context: Optional[Any] = ...): ...
    def create_connect_args(self, url): ...

dialect = ...  # type: Any
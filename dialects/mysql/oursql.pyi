# Stubs for sqlalchemy.dialects.mysql.oursql (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .base import BIT as BIT, MySQLDialect as MySQLDialect, MySQLExecutionContext as MySQLExecutionContext
from ... import types as sqltypes

class _oursqlBIT(BIT):
    def result_processor(self, dialect, coltype): ...

class MySQLExecutionContext_oursql(MySQLExecutionContext):
    @property
    def plain_query(self): ...

class MySQLDialect_oursql(MySQLDialect):
    driver = ...  # type: str
    supports_unicode_binds = ...  # type: bool
    supports_unicode_statements = ...  # type: bool
    supports_native_decimal = ...  # type: bool
    supports_sane_rowcount = ...  # type: bool
    supports_sane_multi_rowcount = ...  # type: bool
    execution_ctx_cls = ...  # type: Any
    colspecs = ...  # type: Any
    @classmethod
    def dbapi(cls): ...
    def do_execute(self, cursor, statement, parameters, context: Optional[Any] = ...): ...
    def do_begin(self, connection): ...
    def do_begin_twophase(self, connection, xid): ...
    def do_prepare_twophase(self, connection, xid): ...
    def do_rollback_twophase(self, connection, xid, is_prepared: bool = ..., recover: bool = ...): ...
    def do_commit_twophase(self, connection, xid, is_prepared: bool = ..., recover: bool = ...): ...
    def has_table(self, connection, table_name, schema: Optional[Any] = ...): ...
    def get_table_options(self, connection, table_name, schema: Optional[Any] = ..., **kw): ...
    def get_columns(self, connection, table_name, schema: Optional[Any] = ..., **kw): ...
    def get_view_names(self, connection, schema: Optional[Any] = ..., **kw): ...
    def get_table_names(self, connection, schema: Optional[Any] = ..., **kw): ...
    def get_schema_names(self, connection, **kw): ...
    def initialize(self, connection): ...
    def is_disconnect(self, e, connection, cursor): ...
    def create_connect_args(self, url): ...

dialect = ...  # type: Any

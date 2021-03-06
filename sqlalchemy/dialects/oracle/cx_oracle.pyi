# Stubs for sqlalchemy.dialects.oracle.cx_oracle (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from sqlalchemy.sql import sqltypes
from .base import OracleCompiler as OracleCompiler, OracleDialect as OracleDialect, OracleExecutionContext as OracleExecutionContext
from . import base as oracle
from ...engine import result as _result

class _OracleNumeric(sqltypes.Numeric):
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class _OracleDate(sqltypes.Date):
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class _LOBMixin(object):
    def result_processor(self, dialect, coltype): ...

class _NativeUnicodeMixin(object):
    def bind_processor(self, dialect): ...

class _OracleChar(_NativeUnicodeMixin, sqltypes.CHAR):
    def get_dbapi_type(self, dbapi): ...

class _OracleNVarChar(_NativeUnicodeMixin, sqltypes.NVARCHAR):
    def get_dbapi_type(self, dbapi): ...

class _OracleText(_LOBMixin, sqltypes.Text):
    def get_dbapi_type(self, dbapi): ...

class _OracleLong(oracle.LONG):
    def get_dbapi_type(self, dbapi): ...

class _OracleString(_NativeUnicodeMixin, sqltypes.String): ...

class _OracleEnum(_NativeUnicodeMixin, sqltypes.Enum):
    def bind_processor(self, dialect): ...

class _OracleUnicodeText(_LOBMixin, _NativeUnicodeMixin, sqltypes.UnicodeText):
    def get_dbapi_type(self, dbapi): ...
    def result_processor(self, dialect, coltype): ...

class _OracleInteger(sqltypes.Integer):
    def result_processor(self, dialect, coltype): ...

class _OracleBinary(_LOBMixin, sqltypes.LargeBinary):
    def get_dbapi_type(self, dbapi): ...
    def bind_processor(self, dialect): ...

class _OracleInterval(oracle.INTERVAL):
    def get_dbapi_type(self, dbapi): ...

class _OracleRaw(oracle.RAW): ...

class _OracleRowid(oracle.ROWID):
    def get_dbapi_type(self, dbapi): ...

class OracleCompiler_cx_oracle(OracleCompiler):
    def bindparam_string(self, name, **kw): ...

class OracleExecutionContext_cx_oracle(OracleExecutionContext):
    out_parameters = ...  # type: Any
    def pre_exec(self): ...
    def create_cursor(self): ...
    def get_result_proxy(self): ...

class OracleExecutionContext_cx_oracle_with_unicode(OracleExecutionContext_cx_oracle):
    statement = ...  # type: Any
    def __init__(self, *arg, **kw) -> None: ...

class ReturningResultProxy(_result.FullyBufferedResultProxy):
    def __init__(self, context, returning_params) -> None: ...

class OracleDialect_cx_oracle(OracleDialect):
    execution_ctx_cls = ...  # type: Any
    statement_compiler = ...  # type: Any
    driver = ...  # type: str
    colspecs = ...  # type: Any
    execute_sequence_format = ...  # type: Any
    threaded = ...  # type: Any
    arraysize = ...  # type: Any
    allow_twophase = ...  # type: Any
    supports_timestamp = ...  # type: Any
    auto_setinputsizes = ...  # type: Any
    auto_convert_lobs = ...  # type: Any
    cx_oracle_ver = ...  # type: Any
    exclude_setinputsizes = ...  # type: Any
    supports_unicode_binds = ...  # type: Any
    coerce_to_unicode = ...  # type: Any
    supports_native_decimal = ...  # type: Any
    supports_unicode_statements = ...  # type: bool
    dbapi_type_map = ...  # type: Any
    def __init__(self, auto_setinputsizes: bool = ..., exclude_setinputsizes: Any = ..., auto_convert_lobs: bool = ..., threaded: bool = ..., allow_twophase: bool = ..., coerce_to_decimal: bool = ..., coerce_to_unicode: bool = ..., arraysize: int = ..., **kwargs) -> None: ...
    @classmethod
    def dbapi(cls): ...
    def initialize(self, connection): ...
    def on_connect(self): ...
    def create_connect_args(self, url): ...
    def is_disconnect(self, e, connection, cursor): ...
    def create_xid(self): ...
    def do_executemany(self, cursor, statement, parameters, context: Optional[Any] = ...): ...
    def do_begin_twophase(self, connection, xid): ...
    def do_prepare_twophase(self, connection, xid): ...
    def do_rollback_twophase(self, connection, xid, is_prepared: bool = ..., recover: bool = ...): ...
    def do_commit_twophase(self, connection, xid, is_prepared: bool = ..., recover: bool = ...): ...
    def do_recover_twophase(self, connection): ...

dialect = ...  # type: Any

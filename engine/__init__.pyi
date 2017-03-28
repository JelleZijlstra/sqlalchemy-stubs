# Stubs for sqlalchemy.engine (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
from .interfaces import (
    Connectable as Connectable,
    CreateEnginePlugin as CreateEnginePlugin,
    Dialect as Dialect,
    ExecutionContext as ExecutionContext,
    ExceptionContext as ExceptionContext,
    Compiled as Compiled,
    TypeCompiler as TypeCompiler
)

from .base import (
    Connection as Connection,
    Engine as Engine,
    NestedTransaction as NestedTransaction,
    RootTransaction as RootTransaction,
    Transaction as Transaction,
    TwoPhaseTransaction as TwoPhaseTransaction,
)

from .result import (
    BaseRowProxy as BaseRowProxy,
    BufferedColumnResultProxy as BufferedColumnResultProxy,
    BufferedColumnRow as BufferedColumnRow,
    BufferedRowResultProxy as BufferedRowResultProxy,
    FullyBufferedResultProxy as FullyBufferedResultProxy,
    ResultProxy as ResultProxy,
    RowProxy as RowProxy,
)

from .util import (
    connection_memoize as connection_memoize
)

from . import util as util, strategies as strategies

def create_engine(*args, **kwargs): ...
def engine_from_config(configuration, prefix: str = ..., **kwargs): ...

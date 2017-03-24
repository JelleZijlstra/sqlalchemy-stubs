# Stubs for sqlalchemy.sql.dml (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .base import Executable as Executable, DialectKWArgs as DialectKWArgs, ColumnCollection as ColumnCollection
from .elements import ClauseElement as ClauseElement, Null as Null, and_ as and_
from .selectable import HasPrefixes as HasPrefixes, HasCTE as HasCTE

class UpdateBase(HasCTE, DialectKWArgs, HasPrefixes, Executable, ClauseElement):
    __visit_name__ = ...  # type: str
    named_with_column = ...  # type: bool
    def params(self, *arg, **kw): ...
    def bind(self): ...
    bind = ...  # type: Any
    def returning(self, *cols): ...
    def with_hint(self, text, selectable: Optional[Any] = ..., dialect_name: str = ...): ...

class ValuesBase(UpdateBase):
    __visit_name__ = ...  # type: str
    select = ...  # type: Any
    table = ...  # type: Any
    def __init__(self, table, values, prefixes) -> None: ...
    parameters = ...  # type: Any
    def values(self, *args, **kwargs): ...
    def return_defaults(self, *cols): ...

class Insert(ValuesBase):
    __visit_name__ = ...  # type: str
    select = ...  # type: Any
    include_insert_from_select_defaults = ...  # type: bool
    inline = ...  # type: Any
    def __init__(self, table, values: Optional[Any] = ..., inline: bool = ..., bind: Optional[Any] = ..., prefixes: Optional[Any] = ..., returning: Optional[Any] = ..., return_defaults: bool = ..., **dialect_kw) -> None: ...
    def get_children(self, **kwargs): ...
    select_names = ...  # type: Any
    def from_select(self, names, select, include_defaults: bool = ...): ...

class Update(ValuesBase):
    __visit_name__ = ...  # type: str
    inline = ...  # type: Any
    def __init__(self, table, whereclause: Optional[Any] = ..., values: Optional[Any] = ..., inline: bool = ..., bind: Optional[Any] = ..., prefixes: Optional[Any] = ..., returning: Optional[Any] = ..., return_defaults: bool = ..., preserve_parameter_order: bool = ..., **dialect_kw) -> None: ...
    def get_children(self, **kwargs): ...
    def where(self, whereclause): ...

class Delete(UpdateBase):
    __visit_name__ = ...  # type: str
    table = ...  # type: Any
    def __init__(self, table, whereclause: Optional[Any] = ..., bind: Optional[Any] = ..., returning: Optional[Any] = ..., prefixes: Optional[Any] = ..., **dialect_kw) -> None: ...
    def get_children(self, **kwargs): ...
    def where(self, whereclause): ...

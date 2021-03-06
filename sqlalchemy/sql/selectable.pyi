# Stubs for sqlalchemy.sql.selectable (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .elements import ClauseElement as ClauseElement, TextClause as TextClause, ClauseList as ClauseList, and_ as and_, Grouping as Grouping, UnaryExpression as UnaryExpression, literal_column as literal_column, BindParameter as BindParameter
from .base import Immutable as Immutable, Executable as Executable, ColumnCollection as ColumnCollection, ColumnSet as ColumnSet, Generative as Generative
from .annotation import Annotated as Annotated

class _OffsetLimitParam(BindParameter): ...

def subquery(alias, *args, **kwargs): ...
def alias(selectable, name: Optional[Any] = ..., flat: bool = ...): ...
def lateral(selectable, name: Optional[Any] = ...): ...
def tablesample(selectable, sampling, name: Optional[Any] = ..., seed: Optional[Any] = ...): ...

class Selectable(ClauseElement):
    __visit_name__ = ...  # type: str
    is_selectable = ...  # type: bool
    @property
    def selectable(self): ...

class HasPrefixes(object):
    def prefix_with(self, *expr, **kw): ...

class HasSuffixes(object):
    def suffix_with(self, *expr, **kw): ...

class FromClause(Selectable):
    __visit_name__ = ...  # type: str
    named_with_column = ...  # type: bool
    schema = ...  # type: Any
    def count(self, whereclause: Optional[Any] = ..., **params): ...
    def select(self, whereclause: Optional[Any] = ..., **params): ...
    def join(self, right, onclause: Optional[Any] = ..., isouter: bool = ..., full: bool = ...): ...
    def outerjoin(self, right, onclause: Optional[Any] = ..., full: bool = ...): ...
    def alias(self, name: Optional[Any] = ..., flat: bool = ...): ...
    def lateral(self, name: Optional[Any] = ...): ...
    def tablesample(self, sampling, name: Optional[Any] = ..., seed: Optional[Any] = ...): ...
    def is_derived_from(self, fromclause): ...
    def replace_selectable(self, old, alias): ...
    def correspond_on_equivalents(self, column, equivalents): ...
    def corresponding_column(self, column, require_embedded: bool = ...): ...
    @property
    def description(self): ...
    @property
    def columns(self): ...
    @property
    def primary_key(self): ...
    @property
    def foreign_keys(self): ...
    c = ...  # type: Any

class Join(FromClause):
    __visit_name__ = ...  # type: str
    left = ...  # type: Any
    right = ...  # type: Any
    onclause = ...  # type: Any
    isouter = ...  # type: Any
    full = ...  # type: Any
    def __init__(self, left, right, onclause: Optional[Any] = ..., isouter: bool = ..., full: bool = ...) -> None: ...
    @property
    def description(self): ...
    def is_derived_from(self, fromclause): ...
    def self_group(self, against: Optional[Any] = ...): ...
    def get_children(self, **kwargs): ...
    def select(self, whereclause: Optional[Any] = ..., **kwargs): ...
    @property
    def bind(self): ...
    def alias(self, *args, **kwargs): ...

class Alias(FromClause):
    __visit_name__ = ...  # type: str
    named_with_column = ...  # type: bool
    original = ...  # type: Any
    supports_execution = ...  # type: Any
    element = ...  # type: Any
    name = ...  # type: Any
    def __init__(self, selectable, name: Optional[Any] = ...) -> None: ...
    def self_group(self, target: Optional[Any] = ...): ...
    @property
    def description(self): ...
    def as_scalar(self): ...
    def is_derived_from(self, fromclause): ...
    def get_children(self, column_collections: bool = ..., **kw): ...
    @property
    def bind(self): ...

class Lateral(Alias):
    __visit_name__ = ...  # type: str

class TableSample(Alias):
    __visit_name__ = ...  # type: str
    sampling = ...  # type: Any
    seed = ...  # type: Any
    def __init__(self, selectable, sampling, name: Optional[Any] = ..., seed: Optional[Any] = ...) -> None: ...

class CTE(Generative, HasSuffixes, Alias):
    __visit_name__ = ...  # type: str
    recursive = ...  # type: Any
    def __init__(self, selectable, name: Optional[Any] = ..., recursive: bool = ..., _cte_alias: Optional[Any] = ..., _restates: Any = ..., _suffixes: Optional[Any] = ...) -> None: ...
    def alias(self, name: Optional[Any] = ..., flat: bool = ...): ...
    def union(self, other): ...
    def union_all(self, other): ...

class HasCTE(object):
    def cte(self, name: Optional[Any] = ..., recursive: bool = ...): ...

class FromGrouping(FromClause):
    __visit_name__ = ...  # type: str
    element = ...  # type: Any
    def __init__(self, element) -> None: ...
    @property
    def columns(self): ...
    @property
    def primary_key(self): ...
    @property
    def foreign_keys(self): ...
    def is_derived_from(self, element): ...
    def alias(self, **kw): ...
    def get_children(self, **kwargs): ...
    def __getattr__(self, attr): ...

class TableClause(Immutable, FromClause):
    __visit_name__ = ...  # type: str
    named_with_column = ...  # type: bool
    implicit_returning = ...  # type: bool
    name = ...  # type: Any
    primary_key = ...  # type: Any
    foreign_keys = ...  # type: Any
    def __init__(self, name, *columns) -> None: ...
    @property
    def description(self): ...
    def append_column(self, c): ...
    def get_children(self, **kwargs): ...
    def insert(self, values: Optional[Any] = ..., inline: bool = ..., **kwargs): ...
    def update(self, whereclause: Optional[Any] = ..., values: Optional[Any] = ..., inline: bool = ..., **kwargs): ...
    def delete(self, whereclause: Optional[Any] = ..., **kwargs): ...

class ForUpdateArg(ClauseElement):
    @classmethod
    def parse_legacy_select(self, arg): ...
    @property
    def legacy_for_update_value(self): ...
    nowait = ...  # type: Any
    read = ...  # type: Any
    skip_locked = ...  # type: Any
    key_share = ...  # type: Any
    of = ...  # type: Any
    def __init__(self, nowait: bool = ..., read: bool = ..., of: Optional[Any] = ..., skip_locked: bool = ..., key_share: bool = ...) -> None: ...

class SelectBase(HasCTE, Executable, FromClause):
    def as_scalar(self): ...
    def label(self, name): ...
    def autocommit(self): ...

class GenerativeSelect(SelectBase):
    use_labels = ...  # type: Any
    def __init__(self, use_labels: bool = ..., for_update: bool = ..., limit: Optional[Any] = ..., offset: Optional[Any] = ..., order_by: Optional[Any] = ..., group_by: Optional[Any] = ..., bind: Optional[Any] = ..., autocommit: Optional[Any] = ...) -> None: ...
    @property
    def for_update(self): ...
    @for_update.setter
    def for_update(self, value): ...
    def with_for_update(self, nowait: bool = ..., read: bool = ..., of: Optional[Any] = ..., skip_locked: bool = ..., key_share: bool = ...): ...
    def apply_labels(self): ...
    def limit(self, limit): ...
    def offset(self, offset): ...
    def order_by(self, *clauses): ...
    def group_by(self, *clauses): ...
    def append_order_by(self, *clauses): ...
    def append_group_by(self, *clauses): ...

class CompoundSelect(GenerativeSelect):
    __visit_name__ = ...  # type: str
    UNION = ...  # type: Any
    UNION_ALL = ...  # type: Any
    EXCEPT = ...  # type: Any
    EXCEPT_ALL = ...  # type: Any
    INTERSECT = ...  # type: Any
    INTERSECT_ALL = ...  # type: Any
    keyword = ...  # type: Any
    selects = ...  # type: Any
    def __init__(self, keyword, *selects, **kwargs) -> None: ...
    def self_group(self, against: Optional[Any] = ...): ...
    def is_derived_from(self, fromclause): ...
    def get_children(self, column_collections: bool = ..., **kwargs): ...
    def bind(self): ...

class Select(HasPrefixes, HasSuffixes, GenerativeSelect):
    __visit_name__ = ...  # type: str
    def __init__(self, columns: Optional[Any] = ..., whereclause: Optional[Any] = ..., from_obj: Optional[Any] = ..., distinct: bool = ..., having: Optional[Any] = ..., correlate: bool = ..., prefixes: Optional[Any] = ..., suffixes: Optional[Any] = ..., **kwargs) -> None: ...
    @property
    def froms(self): ...
    def with_statement_hint(self, text, dialect_name: str = ...): ...
    def with_hint(self, selectable, text, dialect_name: str = ...): ...
    @property
    def type(self): ...
    @property
    def locate_all_froms(self): ...
    @property
    def inner_columns(self): ...
    def is_derived_from(self, fromclause): ...
    def get_children(self, column_collections: bool = ..., **kwargs): ...
    def column(self, column): ...
    def reduce_columns(self, only_synonyms: bool = ...): ...
    def with_only_columns(self, columns): ...
    def where(self, whereclause): ...
    def having(self, having): ...
    def distinct(self, *expr): ...
    def select_from(self, fromclause): ...
    def correlate(self, *fromclauses): ...
    def correlate_except(self, *fromclauses): ...
    def append_correlation(self, fromclause): ...
    def append_column(self, column): ...
    def append_prefix(self, clause): ...
    def append_whereclause(self, whereclause): ...
    def append_having(self, having): ...
    def append_from(self, fromclause): ...
    def self_group(self, against: Optional[Any] = ...): ...
    def union(self, other, **kwargs): ...
    def union_all(self, other, **kwargs): ...
    def except_(self, other, **kwargs): ...
    def except_all(self, other, **kwargs): ...
    def intersect(self, other, **kwargs): ...
    def intersect_all(self, other, **kwargs): ...
    def bind(self): ...

class ScalarSelect(Generative, Grouping):
    element = ...  # type: Any
    type = ...  # type: Any
    def __init__(self, element) -> None: ...
    @property
    def columns(self): ...
    c = ...  # type: Any
    def where(self, crit): ...
    def self_group(self, **kwargs): ...

class Exists(UnaryExpression):
    __visit_name__ = ...  # type: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def select(self, whereclause: Optional[Any] = ..., **params): ...
    def correlate(self, *fromclause): ...
    def correlate_except(self, *fromclause): ...
    def select_from(self, clause): ...
    def where(self, clause): ...

class TextAsFrom(SelectBase):
    __visit_name__ = ...  # type: str
    element = ...  # type: Any
    column_args = ...  # type: Any
    positional = ...  # type: Any
    def __init__(self, text, columns, positional: bool = ...) -> None: ...
    def bindparams(self, *binds, **bind_as_values): ...

class AnnotatedFromClause(Annotated):
    def __init__(self, element, values) -> None: ...

# Stubs for sqlalchemy.orm.util (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional, Text
from ..sql.selectable import FromClause

from .. import exc as sa_exc
from ..sql import expression as expression, operators as operators
from ..sql import util as sql_util
from .interfaces import PropComparator as PropComparator, MapperProperty as MapperProperty
from .base import instance_str as instance_str, state_str as state_str, state_class_str as state_class_str, attribute_str as attribute_str, state_attribute_str as state_attribute_str, object_mapper as object_mapper, object_state as object_state
from .base import class_mapper as class_mapper
from .base import InspectionAttr as InspectionAttr
from .path_registry import PathRegistry as PathRegistry


all_cascades = ...  # type: Any

class CascadeOptions(frozenset):
    save_update = ...  # type: Any
    delete = ...  # type: Any
    refresh_expire = ...  # type: Any
    merge = ...  # type: Any
    expunge = ...  # type: Any
    delete_orphan = ...  # type: Any
    def __new__(cls, value_list): ...
    @classmethod
    def from_string(cls, arg): ...

def polymorphic_union(table_map, typecolname, aliasname: str = ..., cast_nulls: bool = ...): ...
def identity_key(*args, **kwargs): ...

class ORMAdapter(sql_util.ColumnAdapter):
    mapper = ...  # type: Any
    aliased_class = ...  # type: Any
    def __init__(self, entity, equivalents: Optional[Any] = ..., adapt_required: bool = ..., chain_to: Optional[Any] = ..., allow_label_resolve: bool = ..., anonymize_labels: bool = ...) -> None: ...

class AliasedClass(object):
    __name__ = ...  # type: Any
    def __init__(self, cls: Any, alias: Optional[FromClause] = ..., name: Optional[Text] = ..., flat: bool = ..., adapt_on_names: bool = ..., with_polymorphic_mappers: Any = ..., with_polymorphic_discriminator: Optional[Any] = ..., base_alias: Optional[Any] = ..., use_mapper_path: bool = ...) -> None: ...
    def __getattr__(self, key): ...

class AliasedInsp(InspectionAttr):
    entity = ...  # type: Any
    mapper = ...  # type: Any
    selectable = ...  # type: Any
    name = ...  # type: Any
    with_polymorphic_mappers = ...  # type: Any
    polymorphic_on = ...  # type: Any
    def __init__(self, entity, mapper, selectable, name, with_polymorphic_mappers, polymorphic_on, _base_alias, _use_mapper_path, adapt_on_names) -> None: ...
    is_aliased_class = ...  # type: bool
    @property
    def class_(self): ...

def aliased(element: Any, alias: Optional[FromClause] = ..., name: Optional[Text] = ..., flat: bool = ..., adapt_on_names: bool = ...) -> AliasedClass: ...
def with_polymorphic(base, classes, selectable: bool = ..., flat: bool = ..., polymorphic_on: Optional[Any] = ..., aliased: bool = ..., innerjoin: bool = ..., _use_mapper_path: bool = ..., _existing_alias: Optional[Any] = ...): ...

class _ORMJoin(expression.Join):
    __visit_name__ = ...  # type: Any
    onclause = ...  # type: Any
    def __init__(self, left, right, onclause: Optional[Any] = ..., isouter: bool = ..., full: bool = ..., _left_memo: Optional[Any] = ..., _right_memo: Optional[Any] = ...) -> None: ...
    def join(self, right, onclause: Optional[Any] = ..., isouter: bool = ..., full: bool = ..., join_to_left: Optional[Any] = ...): ...
    def outerjoin(self, right, onclause: Optional[Any] = ..., full: bool = ..., join_to_left: Optional[Any] = ...): ...

def join(left, right, onclause: Optional[Any] = ..., isouter: bool = ..., full: bool = ..., join_to_left: Optional[Any] = ...): ...
def outerjoin(left, right, onclause: Optional[Any] = ..., full: bool = ..., join_to_left: Optional[Any] = ...): ...
def with_parent(instance, prop): ...
def has_identity(object): ...
def was_deleted(object): ...
def randomize_unitofwork(): ...

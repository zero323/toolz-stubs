from typing import Any, Optional

def merge(*dicts: Any, **kwargs: Any): ...
def merge_with(func: Any, *dicts: Any, **kwargs: Any): ...
def valmap(func: Any, d: Any, factory: Any = ...): ...
def keymap(func: Any, d: Any, factory: Any = ...): ...
def itemmap(func: Any, d: Any, factory: Any = ...): ...
def valfilter(predicate: Any, d: Any, factory: Any = ...): ...
def keyfilter(predicate: Any, d: Any, factory: Any = ...): ...
def itemfilter(predicate: Any, d: Any, factory: Any = ...): ...
def assoc(d: Any, key: Any, value: Any, factory: Any = ...): ...
def dissoc(d: Any, *keys: Any, **kwargs: Any): ...
def assoc_in(d: Any, keys: Any, value: Any, factory: Any = ...): ...
def update_in(d: Any, keys: Any, func: Any, default: Optional[Any] = ..., factory: Any = ...): ...
def get_in(keys: Any, coll: Any, default: Optional[Any] = ..., no_default: bool = ...): ...
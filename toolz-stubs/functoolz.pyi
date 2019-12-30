from typing import Any, Optional

def identity(x: Any): ...
def apply(*func_and_args: Any, **kwargs: Any): ...
def thread_first(val: Any, *forms: Any): ...
def thread_last(val: Any, *forms: Any): ...

class InstanceProperty(property):
    classval: Any = ...
    def __init__(self, fget: Optional[Any] = ..., fset: Optional[Any] = ..., fdel: Optional[Any] = ..., doc: Optional[Any] = ..., classval: Optional[Any] = ...) -> None: ...
    def __get__(self, obj: Any, type: Optional[Any] = ...): ...
    def __reduce__(self): ...

class curry:
    __doc__: Any = ...
    __name__: Any = ...
    __module__: Any = ...
    __qualname__: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def func(self): ...
    def __signature__(self): ...
    def args(self): ...
    def keywords(self): ...
    def func_name(self): ...
    def __hash__(self) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __call__(self, *args: Any, **kwargs: Any): ...
    def bind(self, *args: Any, **kwargs: Any): ...
    def call(self, *args: Any, **kwargs: Any): ...
    def __get__(self, instance: Any, owner: Any): ...
    def __reduce__(self): ...

def memoize(func: Any, cache: Optional[Any] = ..., key: Optional[Any] = ...): ...

class Compose:
    first: Any = ...
    funcs: Any = ...
    def __init__(self, funcs: Any) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any): ...
    def __doc__(self): ...
    @property
    def __name__(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...
    def __get__(self, obj: Any, objtype: Optional[Any] = ...): ...
    def __signature__(self): ...
    __wrapped__: Any = ...

def compose(*funcs: Any): ...
def compose_left(*funcs: Any): ...
def pipe(data: Any, *funcs: Any): ...
def complement(func: Any): ...

class juxt:
    funcs: Any = ...
    def __init__(self, *funcs: Any) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any): ...

def do(func: Any, x: Any): ...
def flip(func: Any, a: Any, b: Any): ...

class excepts:
    exc: Any = ...
    func: Any = ...
    handler: Any = ...
    def __init__(self, exc: Any, func: Any, handler: Any = ...) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any): ...
    def __doc__(self): ...
    @property
    def __name__(self): ...

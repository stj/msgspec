from typing import Any, Type, TypeVar, Generic, Optional, Callable, Union, overload

T = TypeVar("T")

enc_hook_sig = Optional[Callable[[Any], Any]]
ext_hook_sig = Optional[Callable[[int, memoryview], Any]]
dec_hook_sig = Optional[Callable[[Type, Any], Any]]

class Ext:
    code: int
    data: Union[bytes, bytearray, memoryview]
    def __init__(
        self, code: int, data: Union[bytes, bytearray, memoryview]
    ) -> None: ...

class Decoder(Generic[T]):
    @overload
    def __init__(
        self: Decoder[Any],
        dec_hook: dec_hook_sig = None,
        ext_hook: ext_hook_sig = None,
    ) -> None: ...
    @overload
    def __init__(
        self: Decoder[T],
        type: Type[T] = ...,
        dec_hook: dec_hook_sig = None,
        ext_hook: ext_hook_sig = None,
    ) -> None: ...
    def decode(self, data: bytes) -> T: ...

class Encoder:
    def __init__(
        self,
        *,
        enc_hook: enc_hook_sig = None,
        write_buffer_size: int = ...,
    ): ...
    def encode(self, obj: Any) -> bytes: ...

@overload
def decode(buf: bytes, ext_hook: ext_hook_sig = None) -> Any: ...
@overload
def decode(
    buf: bytes,
    *,
    type: Type[T] = ...,
    dec_hook: dec_hook_sig = None,
    ext_hook: ext_hook_sig = None,
) -> T: ...
def encode(obj: Any, *, enc_hook: enc_hook_sig = None) -> bytes: ...

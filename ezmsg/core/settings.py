
from abc import ABC, ABCMeta
from dataclasses import dataclass

from typing import (
    Dict,
    Tuple,
    Any,
    Type,
)

# All settings classes are dataclasses
# https://rednafi.github.io/digressions/python/2020/06/26/python-metaclasses.html
#  see -- #avoiding-dataclass-decorator-with-metaclasses


class SettingsMeta(ABCMeta):

    def __new__(
        cls, name: str, bases: Tuple[type, ...], classdict: Dict[str, Any], **kwargs: Any
    ) -> Type["Settings"]:

        new_cls = super().__new__(cls, name, bases, classdict)
        return dataclass(unsafe_hash=True, frozen=True)(new_cls)  # type: ignore


class Settings(ABC, metaclass=SettingsMeta):
    ...

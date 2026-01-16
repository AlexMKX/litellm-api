from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="IndexCreateLiteLLMParams")



@_attrs_define
class IndexCreateLiteLLMParams:
    """ 
        Attributes:
            vector_store_index (str):
            vector_store_name (str):
     """

    vector_store_index: str
    vector_store_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        vector_store_index = self.vector_store_index

        vector_store_name = self.vector_store_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "vector_store_index": vector_store_index,
            "vector_store_name": vector_store_name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vector_store_index = d.pop("vector_store_index")

        vector_store_name = d.pop("vector_store_name")

        index_create_lite_llm_params = cls(
            vector_store_index=vector_store_index,
            vector_store_name=vector_store_name,
        )


        index_create_lite_llm_params.additional_properties = d
        return index_create_lite_llm_params

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

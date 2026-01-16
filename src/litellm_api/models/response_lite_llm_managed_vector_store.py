from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.lite_llm_managed_vector_stores_table import LiteLLMManagedVectorStoresTable





T = TypeVar("T", bound="ResponseLiteLLMManagedVectorStore")



@_attrs_define
class ResponseLiteLLMManagedVectorStore:
    """ 
        Attributes:
            vector_store (LiteLLMManagedVectorStoresTable | Unset):
     """

    vector_store: LiteLLMManagedVectorStoresTable | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.lite_llm_managed_vector_stores_table import LiteLLMManagedVectorStoresTable
        vector_store: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vector_store, Unset):
            vector_store = self.vector_store.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if vector_store is not UNSET:
            field_dict["vector_store"] = vector_store

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lite_llm_managed_vector_stores_table import LiteLLMManagedVectorStoresTable
        d = dict(src_dict)
        _vector_store = d.pop("vector_store", UNSET)
        vector_store: LiteLLMManagedVectorStoresTable | Unset
        if isinstance(_vector_store,  Unset):
            vector_store = UNSET
        else:
            vector_store = LiteLLMManagedVectorStoresTable.from_dict(_vector_store)




        response_lite_llm_managed_vector_store = cls(
            vector_store=vector_store,
        )


        response_lite_llm_managed_vector_store.additional_properties = d
        return response_lite_llm_managed_vector_store

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

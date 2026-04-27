from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.lite_llm_memory_row import LiteLLMMemoryRow





T = TypeVar("T", bound="MemoryListResponse")



@_attrs_define
class MemoryListResponse:
    """ 
        Attributes:
            memories (list[LiteLLMMemoryRow]):
            total (int):
     """

    memories: list[LiteLLMMemoryRow]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.lite_llm_memory_row import LiteLLMMemoryRow
        memories = []
        for memories_item_data in self.memories:
            memories_item = memories_item_data.to_dict()
            memories.append(memories_item)



        total = self.total


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "memories": memories,
            "total": total,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lite_llm_memory_row import LiteLLMMemoryRow
        d = dict(src_dict)
        memories = []
        _memories = d.pop("memories")
        for memories_item_data in (_memories):
            memories_item = LiteLLMMemoryRow.from_dict(memories_item_data)



            memories.append(memories_item)


        total = d.pop("total")

        memory_list_response = cls(
            memories=memories,
            total=total,
        )


        memory_list_response.additional_properties = d
        return memory_list_response

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

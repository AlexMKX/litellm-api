from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.prompt_spec import PromptSpec





T = TypeVar("T", bound="ListPromptsResponse")



@_attrs_define
class ListPromptsResponse:
    """ 
        Attributes:
            prompts (list[PromptSpec]):
     """

    prompts: list[PromptSpec]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.prompt_spec import PromptSpec
        prompts = []
        for prompts_item_data in self.prompts:
            prompts_item = prompts_item_data.to_dict()
            prompts.append(prompts_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "prompts": prompts,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prompt_spec import PromptSpec
        d = dict(src_dict)
        prompts = []
        _prompts = d.pop("prompts")
        for prompts_item_data in (_prompts):
            prompts_item = PromptSpec.from_dict(prompts_item_data)



            prompts.append(prompts_item)


        list_prompts_response = cls(
            prompts=prompts,
        )


        list_prompts_response.additional_properties = d
        return list_prompts_response

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

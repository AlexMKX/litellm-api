from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.prompt_tokens_details import PromptTokensDetails





T = TypeVar("T", bound="TokenCountDetailsResponse")



@_attrs_define
class TokenCountDetailsResponse:
    """ Response structure for token count details with modality breakdown.

    Example:
        {'totalTokens': 12, 'promptTokensDetails': [{'modality': 'TEXT', 'tokenCount': 12}]}

        Attributes:
            total_tokens (int):
            prompt_tokens_details (list[PromptTokensDetails]):
     """

    total_tokens: int
    prompt_tokens_details: list[PromptTokensDetails]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.prompt_tokens_details import PromptTokensDetails
        total_tokens = self.total_tokens

        prompt_tokens_details = []
        for prompt_tokens_details_item_data in self.prompt_tokens_details:
            prompt_tokens_details_item = prompt_tokens_details_item_data.to_dict()
            prompt_tokens_details.append(prompt_tokens_details_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "totalTokens": total_tokens,
            "promptTokensDetails": prompt_tokens_details,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prompt_tokens_details import PromptTokensDetails
        d = dict(src_dict)
        total_tokens = d.pop("totalTokens")

        prompt_tokens_details = []
        _prompt_tokens_details = d.pop("promptTokensDetails")
        for prompt_tokens_details_item_data in (_prompt_tokens_details):
            prompt_tokens_details_item = PromptTokensDetails.from_dict(prompt_tokens_details_item_data)



            prompt_tokens_details.append(prompt_tokens_details_item)


        token_count_details_response = cls(
            total_tokens=total_tokens,
            prompt_tokens_details=prompt_tokens_details,
        )


        token_count_details_response.additional_properties = d
        return token_count_details_response

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

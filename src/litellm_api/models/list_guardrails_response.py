from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.guardrail_info_response import GuardrailInfoResponse





T = TypeVar("T", bound="ListGuardrailsResponse")



@_attrs_define
class ListGuardrailsResponse:
    """ 
        Attributes:
            guardrails (list[GuardrailInfoResponse]):
     """

    guardrails: list[GuardrailInfoResponse]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.guardrail_info_response import GuardrailInfoResponse
        guardrails = []
        for guardrails_item_data in self.guardrails:
            guardrails_item = guardrails_item_data.to_dict()
            guardrails.append(guardrails_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "guardrails": guardrails,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.guardrail_info_response import GuardrailInfoResponse
        d = dict(src_dict)
        guardrails = []
        _guardrails = d.pop("guardrails")
        for guardrails_item_data in (_guardrails):
            guardrails_item = GuardrailInfoResponse.from_dict(guardrails_item_data)



            guardrails.append(guardrails_item)


        list_guardrails_response = cls(
            guardrails=guardrails,
        )


        list_guardrails_response.additional_properties = d
        return list_guardrails_response

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

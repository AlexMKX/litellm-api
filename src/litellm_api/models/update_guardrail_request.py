from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.guardrail import Guardrail





T = TypeVar("T", bound="UpdateGuardrailRequest")



@_attrs_define
class UpdateGuardrailRequest:
    """ 
        Attributes:
            guardrail (Guardrail):
     """

    guardrail: Guardrail
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.guardrail import Guardrail
        guardrail = self.guardrail.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "guardrail": guardrail,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.guardrail import Guardrail
        d = dict(src_dict)
        guardrail = Guardrail.from_dict(d.pop("guardrail"))




        update_guardrail_request = cls(
            guardrail=guardrail,
        )


        update_guardrail_request.additional_properties = d
        return update_guardrail_request

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

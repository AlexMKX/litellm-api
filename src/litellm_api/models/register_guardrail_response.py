from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="RegisterGuardrailResponse")



@_attrs_define
class RegisterGuardrailResponse:
    """ 
        Attributes:
            guardrail_id (str):
            guardrail_name (str):
            status (str):
            submitted_at (datetime.datetime | None | Unset):
     """

    guardrail_id: str
    guardrail_name: str
    status: str
    submitted_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        guardrail_id = self.guardrail_id

        guardrail_name = self.guardrail_name

        status = self.status

        submitted_at: None | str | Unset
        if isinstance(self.submitted_at, Unset):
            submitted_at = UNSET
        elif isinstance(self.submitted_at, datetime.datetime):
            submitted_at = self.submitted_at.isoformat()
        else:
            submitted_at = self.submitted_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "guardrail_id": guardrail_id,
            "guardrail_name": guardrail_name,
            "status": status,
        })
        if submitted_at is not UNSET:
            field_dict["submitted_at"] = submitted_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        guardrail_id = d.pop("guardrail_id")

        guardrail_name = d.pop("guardrail_name")

        status = d.pop("status")

        def _parse_submitted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                submitted_at_type_0 = isoparse(data)



                return submitted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        submitted_at = _parse_submitted_at(d.pop("submitted_at", UNSET))


        register_guardrail_response = cls(
            guardrail_id=guardrail_id,
            guardrail_name=guardrail_name,
            status=status,
            submitted_at=submitted_at,
        )


        register_guardrail_response.additional_properties = d
        return register_guardrail_response

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

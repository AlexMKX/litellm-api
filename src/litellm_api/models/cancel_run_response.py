from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Literal, cast






T = TypeVar("T", bound="CancelRunResponse")



@_attrs_define
class CancelRunResponse:
    """ Response from cancelling a run

        Attributes:
            id (str):
            status (Literal['cancelled']):
            object_ (str | Unset):  Default: 'eval.run'.
     """

    id: str
    status: Literal['cancelled']
    object_: str | Unset = 'eval.run'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status

        object_ = self.object_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "status": status,
        })
        if object_ is not UNSET:
            field_dict["object"] = object_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        status = cast(Literal['cancelled'] , d.pop("status"))
        if status != 'cancelled':
            raise ValueError(f"status must match const 'cancelled', got '{status}'")

        object_ = d.pop("object", UNSET)

        cancel_run_response = cls(
            id=id,
            status=status,
            object_=object_,
        )


        cancel_run_response.additional_properties = d
        return cancel_run_response

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PolicyVersionCreateRequest")



@_attrs_define
class PolicyVersionCreateRequest:
    """ Request body for creating a new policy version (draft).

        Attributes:
            source_policy_id (None | str | Unset): Policy ID to clone from. If None, clone from current production version.
     """

    source_policy_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        source_policy_id: None | str | Unset
        if isinstance(self.source_policy_id, Unset):
            source_policy_id = UNSET
        else:
            source_policy_id = self.source_policy_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if source_policy_id is not UNSET:
            field_dict["source_policy_id"] = source_policy_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_source_policy_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_policy_id = _parse_source_policy_id(d.pop("source_policy_id", UNSET))


        policy_version_create_request = cls(
            source_policy_id=source_policy_id,
        )


        policy_version_create_request.additional_properties = d
        return policy_version_create_request

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SCIMFeature")



@_attrs_define
class SCIMFeature:
    """ 
        Attributes:
            supported (bool):
            max_operations (int | None | Unset):
            max_payload_size (int | None | Unset):
            max_results (int | None | Unset):
     """

    supported: bool
    max_operations: int | None | Unset = UNSET
    max_payload_size: int | None | Unset = UNSET
    max_results: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        supported = self.supported

        max_operations: int | None | Unset
        if isinstance(self.max_operations, Unset):
            max_operations = UNSET
        else:
            max_operations = self.max_operations

        max_payload_size: int | None | Unset
        if isinstance(self.max_payload_size, Unset):
            max_payload_size = UNSET
        else:
            max_payload_size = self.max_payload_size

        max_results: int | None | Unset
        if isinstance(self.max_results, Unset):
            max_results = UNSET
        else:
            max_results = self.max_results


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "supported": supported,
        })
        if max_operations is not UNSET:
            field_dict["maxOperations"] = max_operations
        if max_payload_size is not UNSET:
            field_dict["maxPayloadSize"] = max_payload_size
        if max_results is not UNSET:
            field_dict["maxResults"] = max_results

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        supported = d.pop("supported")

        def _parse_max_operations(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_operations = _parse_max_operations(d.pop("maxOperations", UNSET))


        def _parse_max_payload_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_payload_size = _parse_max_payload_size(d.pop("maxPayloadSize", UNSET))


        def _parse_max_results(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_results = _parse_max_results(d.pop("maxResults", UNSET))


        scim_feature = cls(
            supported=supported,
            max_operations=max_operations,
            max_payload_size=max_payload_size,
            max_results=max_results,
        )


        scim_feature.additional_properties = d
        return scim_feature

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

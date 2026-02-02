from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.failed_key_update_key_info_type_0 import FailedKeyUpdateKeyInfoType0





T = TypeVar("T", bound="FailedKeyUpdate")



@_attrs_define
class FailedKeyUpdate:
    """ Failed key update with reason

        Attributes:
            key (str):
            failed_reason (str):
            key_info (FailedKeyUpdateKeyInfoType0 | None | Unset):
     """

    key: str
    failed_reason: str
    key_info: FailedKeyUpdateKeyInfoType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.failed_key_update_key_info_type_0 import FailedKeyUpdateKeyInfoType0
        key = self.key

        failed_reason = self.failed_reason

        key_info: dict[str, Any] | None | Unset
        if isinstance(self.key_info, Unset):
            key_info = UNSET
        elif isinstance(self.key_info, FailedKeyUpdateKeyInfoType0):
            key_info = self.key_info.to_dict()
        else:
            key_info = self.key_info


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "key": key,
            "failed_reason": failed_reason,
        })
        if key_info is not UNSET:
            field_dict["key_info"] = key_info

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.failed_key_update_key_info_type_0 import FailedKeyUpdateKeyInfoType0
        d = dict(src_dict)
        key = d.pop("key")

        failed_reason = d.pop("failed_reason")

        def _parse_key_info(data: object) -> FailedKeyUpdateKeyInfoType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                key_info_type_0 = FailedKeyUpdateKeyInfoType0.from_dict(data)



                return key_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FailedKeyUpdateKeyInfoType0 | None | Unset, data)

        key_info = _parse_key_info(d.pop("key_info", UNSET))


        failed_key_update = cls(
            key=key,
            failed_reason=failed_reason,
            key_info=key_info,
        )


        failed_key_update.additional_properties = d
        return failed_key_update

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

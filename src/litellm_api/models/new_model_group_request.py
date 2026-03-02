from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="NewModelGroupRequest")



@_attrs_define
class NewModelGroupRequest:
    """ 
        Attributes:
            access_group (str):
            model_names (list[str] | None | Unset):
            model_ids (list[str] | None | Unset):
     """

    access_group: str
    model_names: list[str] | None | Unset = UNSET
    model_ids: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        access_group = self.access_group

        model_names: list[str] | None | Unset
        if isinstance(self.model_names, Unset):
            model_names = UNSET
        elif isinstance(self.model_names, list):
            model_names = self.model_names


        else:
            model_names = self.model_names

        model_ids: list[str] | None | Unset
        if isinstance(self.model_ids, Unset):
            model_ids = UNSET
        elif isinstance(self.model_ids, list):
            model_ids = self.model_ids


        else:
            model_ids = self.model_ids


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "access_group": access_group,
        })
        if model_names is not UNSET:
            field_dict["model_names"] = model_names
        if model_ids is not UNSET:
            field_dict["model_ids"] = model_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_group = d.pop("access_group")

        def _parse_model_names(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                model_names_type_0 = cast(list[str], data)

                return model_names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        model_names = _parse_model_names(d.pop("model_names", UNSET))


        def _parse_model_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                model_ids_type_0 = cast(list[str], data)

                return model_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        model_ids = _parse_model_ids(d.pop("model_ids", UNSET))


        new_model_group_request = cls(
            access_group=access_group,
            model_names=model_names,
            model_ids=model_ids,
        )


        new_model_group_request.additional_properties = d
        return new_model_group_request

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

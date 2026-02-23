from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RunDeleteResponse")



@_attrs_define
class RunDeleteResponse:
    """ Response from deleting a run

        Attributes:
            run_id (str):
            object_ (None | str | Unset):  Default: 'eval.run.deleted'.
            deleted (bool | None | Unset):  Default: True.
     """

    run_id: str
    object_: None | str | Unset = 'eval.run.deleted'
    deleted: bool | None | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        object_: None | str | Unset
        if isinstance(self.object_, Unset):
            object_ = UNSET
        else:
            object_ = self.object_

        deleted: bool | None | Unset
        if isinstance(self.deleted, Unset):
            deleted = UNSET
        else:
            deleted = self.deleted


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "run_id": run_id,
        })
        if object_ is not UNSET:
            field_dict["object"] = object_
        if deleted is not UNSET:
            field_dict["deleted"] = deleted

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        run_id = d.pop("run_id")

        def _parse_object_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_ = _parse_object_(d.pop("object", UNSET))


        def _parse_deleted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        deleted = _parse_deleted(d.pop("deleted", UNSET))


        run_delete_response = cls(
            run_id=run_id,
            object_=object_,
            deleted=deleted,
        )


        run_delete_response.additional_properties = d
        return run_delete_response

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="DeleteEvalResponse")



@_attrs_define
class DeleteEvalResponse:
    """ Response from deleting an evaluation

        Attributes:
            eval_id (str):
            deleted (bool):
            object_ (str | Unset):  Default: 'eval.deleted'.
     """

    eval_id: str
    deleted: bool
    object_: str | Unset = 'eval.deleted'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        eval_id = self.eval_id

        deleted = self.deleted

        object_ = self.object_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "eval_id": eval_id,
            "deleted": deleted,
        })
        if object_ is not UNSET:
            field_dict["object"] = object_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        eval_id = d.pop("eval_id")

        deleted = d.pop("deleted")

        object_ = d.pop("object", UNSET)

        delete_eval_response = cls(
            eval_id=eval_id,
            deleted=deleted,
            object_=object_,
        )


        delete_eval_response.additional_properties = d
        return delete_eval_response

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

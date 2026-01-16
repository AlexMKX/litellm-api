from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="UpdatePublicModelGroupsRequest")



@_attrs_define
class UpdatePublicModelGroupsRequest:
    """ Request model for updating public model groups

        Attributes:
            model_groups (list[str]): List of model group names to make public
     """

    model_groups: list[str]





    def to_dict(self) -> dict[str, Any]:
        model_groups = self.model_groups




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "model_groups": model_groups,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model_groups = cast(list[str], d.pop("model_groups"))


        update_public_model_groups_request = cls(
            model_groups=model_groups,
        )

        return update_public_model_groups_request


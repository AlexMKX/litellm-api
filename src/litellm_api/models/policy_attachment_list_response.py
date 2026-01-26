from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.policy_attachment_db_response import PolicyAttachmentDBResponse





T = TypeVar("T", bound="PolicyAttachmentListResponse")



@_attrs_define
class PolicyAttachmentListResponse:
    """ Response for listing policy attachments.

        Attributes:
            attachments (list[PolicyAttachmentDBResponse] | Unset): List of policy attachments.
            total_count (int | Unset): Total number of attachments. Default: 0.
     """

    attachments: list[PolicyAttachmentDBResponse] | Unset = UNSET
    total_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.policy_attachment_db_response import PolicyAttachmentDBResponse
        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)



        total_count = self.total_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.policy_attachment_db_response import PolicyAttachmentDBResponse
        d = dict(src_dict)
        _attachments = d.pop("attachments", UNSET)
        attachments: list[PolicyAttachmentDBResponse] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = PolicyAttachmentDBResponse.from_dict(attachments_item_data)



                attachments.append(attachments_item)


        total_count = d.pop("total_count", UNSET)

        policy_attachment_list_response = cls(
            attachments=attachments,
            total_count=total_count,
        )


        policy_attachment_list_response.additional_properties = d
        return policy_attachment_list_response

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

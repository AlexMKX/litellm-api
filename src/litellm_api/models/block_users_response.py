from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.lite_llm_end_user_table import LiteLLMEndUserTable





T = TypeVar("T", bound="BlockUsersResponse")



@_attrs_define
class BlockUsersResponse:
    """ 
        Attributes:
            blocked_users (list[LiteLLMEndUserTable]):
     """

    blocked_users: list[LiteLLMEndUserTable]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.lite_llm_end_user_table import LiteLLMEndUserTable
        blocked_users = []
        for blocked_users_item_data in self.blocked_users:
            blocked_users_item = blocked_users_item_data.to_dict()
            blocked_users.append(blocked_users_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "blocked_users": blocked_users,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lite_llm_end_user_table import LiteLLMEndUserTable
        d = dict(src_dict)
        blocked_users = []
        _blocked_users = d.pop("blocked_users")
        for blocked_users_item_data in (_blocked_users):
            blocked_users_item = LiteLLMEndUserTable.from_dict(blocked_users_item_data)



            blocked_users.append(blocked_users_item)


        block_users_response = cls(
            blocked_users=blocked_users,
        )


        block_users_response.additional_properties = d
        return block_users_response

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

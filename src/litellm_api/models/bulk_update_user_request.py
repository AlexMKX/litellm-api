from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_user_request import UpdateUserRequest
  from ..models.update_user_request_no_user_i_dor_email import UpdateUserRequestNoUserIDorEmail





T = TypeVar("T", bound="BulkUpdateUserRequest")



@_attrs_define
class BulkUpdateUserRequest:
    """ Request for bulk user updates

        Attributes:
            users (list[UpdateUserRequest] | None | Unset):
            all_users (bool | None | Unset):  Default: False.
            user_updates (None | Unset | UpdateUserRequestNoUserIDorEmail):
     """

    users: list[UpdateUserRequest] | None | Unset = UNSET
    all_users: bool | None | Unset = False
    user_updates: None | Unset | UpdateUserRequestNoUserIDorEmail = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_user_request_no_user_i_dor_email import UpdateUserRequestNoUserIDorEmail
        from ..models.update_user_request import UpdateUserRequest
        users: list[dict[str, Any]] | None | Unset
        if isinstance(self.users, Unset):
            users = UNSET
        elif isinstance(self.users, list):
            users = []
            for users_type_0_item_data in self.users:
                users_type_0_item = users_type_0_item_data.to_dict()
                users.append(users_type_0_item)


        else:
            users = self.users

        all_users: bool | None | Unset
        if isinstance(self.all_users, Unset):
            all_users = UNSET
        else:
            all_users = self.all_users

        user_updates: dict[str, Any] | None | Unset
        if isinstance(self.user_updates, Unset):
            user_updates = UNSET
        elif isinstance(self.user_updates, UpdateUserRequestNoUserIDorEmail):
            user_updates = self.user_updates.to_dict()
        else:
            user_updates = self.user_updates


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if users is not UNSET:
            field_dict["users"] = users
        if all_users is not UNSET:
            field_dict["all_users"] = all_users
        if user_updates is not UNSET:
            field_dict["user_updates"] = user_updates

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_user_request import UpdateUserRequest
        from ..models.update_user_request_no_user_i_dor_email import UpdateUserRequestNoUserIDorEmail
        d = dict(src_dict)
        def _parse_users(data: object) -> list[UpdateUserRequest] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                users_type_0 = []
                _users_type_0 = data
                for users_type_0_item_data in (_users_type_0):
                    users_type_0_item = UpdateUserRequest.from_dict(users_type_0_item_data)



                    users_type_0.append(users_type_0_item)

                return users_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UpdateUserRequest] | None | Unset, data)

        users = _parse_users(d.pop("users", UNSET))


        def _parse_all_users(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        all_users = _parse_all_users(d.pop("all_users", UNSET))


        def _parse_user_updates(data: object) -> None | Unset | UpdateUserRequestNoUserIDorEmail:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_updates_type_0 = UpdateUserRequestNoUserIDorEmail.from_dict(data)



                return user_updates_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateUserRequestNoUserIDorEmail, data)

        user_updates = _parse_user_updates(d.pop("user_updates", UNSET))


        bulk_update_user_request = cls(
            users=users,
            all_users=all_users,
            user_updates=user_updates,
        )


        bulk_update_user_request.additional_properties = d
        return bulk_update_user_request

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

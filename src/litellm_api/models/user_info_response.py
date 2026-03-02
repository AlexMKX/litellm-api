from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.base_model import BaseModel
  from ..models.user_info_response_user_info_type_0 import UserInfoResponseUserInfoType0





T = TypeVar("T", bound="UserInfoResponse")



@_attrs_define
class UserInfoResponse:
    """ 
        Attributes:
            user_id (None | str):
            user_info (BaseModel | None | UserInfoResponseUserInfoType0):
            keys (list[Any]):
            teams (list[Any]):
     """

    user_id: None | str
    user_info: BaseModel | None | UserInfoResponseUserInfoType0
    keys: list[Any]
    teams: list[Any]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.base_model import BaseModel
        from ..models.user_info_response_user_info_type_0 import UserInfoResponseUserInfoType0
        user_id: None | str
        user_id = self.user_id

        user_info: dict[str, Any] | None
        if isinstance(self.user_info, UserInfoResponseUserInfoType0):
            user_info = self.user_info.to_dict()
        elif isinstance(self.user_info, BaseModel):
            user_info = self.user_info.to_dict()
        else:
            user_info = self.user_info

        keys = self.keys



        teams = self.teams




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "user_id": user_id,
            "user_info": user_info,
            "keys": keys,
            "teams": teams,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_model import BaseModel
        from ..models.user_info_response_user_info_type_0 import UserInfoResponseUserInfoType0
        d = dict(src_dict)
        def _parse_user_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        user_id = _parse_user_id(d.pop("user_id"))


        def _parse_user_info(data: object) -> BaseModel | None | UserInfoResponseUserInfoType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_info_type_0 = UserInfoResponseUserInfoType0.from_dict(data)



                return user_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_info_type_1 = BaseModel.from_dict(data)



                return user_info_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BaseModel | None | UserInfoResponseUserInfoType0, data)

        user_info = _parse_user_info(d.pop("user_info"))


        keys = cast(list[Any], d.pop("keys"))


        teams = cast(list[Any], d.pop("teams"))


        user_info_response = cls(
            user_id=user_id,
            user_info=user_info,
            keys=keys,
            teams=teams,
        )


        user_info_response.additional_properties = d
        return user_info_response

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.add_team_callback_callback_type_type_0 import AddTeamCallbackCallbackTypeType0
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.add_team_callback_callback_vars import AddTeamCallbackCallbackVars





T = TypeVar("T", bound="AddTeamCallback")



@_attrs_define
class AddTeamCallback:
    """ 
        Attributes:
            callback_name (str):
            callback_vars (AddTeamCallbackCallbackVars):
            callback_type (AddTeamCallbackCallbackTypeType0 | None | Unset):  Default:
                AddTeamCallbackCallbackTypeType0.SUCCESS_AND_FAILURE.
     """

    callback_name: str
    callback_vars: AddTeamCallbackCallbackVars
    callback_type: AddTeamCallbackCallbackTypeType0 | None | Unset = AddTeamCallbackCallbackTypeType0.SUCCESS_AND_FAILURE
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.add_team_callback_callback_vars import AddTeamCallbackCallbackVars
        callback_name = self.callback_name

        callback_vars = self.callback_vars.to_dict()

        callback_type: None | str | Unset
        if isinstance(self.callback_type, Unset):
            callback_type = UNSET
        elif isinstance(self.callback_type, AddTeamCallbackCallbackTypeType0):
            callback_type = self.callback_type.value
        else:
            callback_type = self.callback_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "callback_name": callback_name,
            "callback_vars": callback_vars,
        })
        if callback_type is not UNSET:
            field_dict["callback_type"] = callback_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_team_callback_callback_vars import AddTeamCallbackCallbackVars
        d = dict(src_dict)
        callback_name = d.pop("callback_name")

        callback_vars = AddTeamCallbackCallbackVars.from_dict(d.pop("callback_vars"))




        def _parse_callback_type(data: object) -> AddTeamCallbackCallbackTypeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                callback_type_type_0 = AddTeamCallbackCallbackTypeType0(data)



                return callback_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AddTeamCallbackCallbackTypeType0 | None | Unset, data)

        callback_type = _parse_callback_type(d.pop("callback_type", UNSET))


        add_team_callback = cls(
            callback_name=callback_name,
            callback_vars=callback_vars,
            callback_type=callback_type,
        )


        add_team_callback.additional_properties = d
        return add_team_callback

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

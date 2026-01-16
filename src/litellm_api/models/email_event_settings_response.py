from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.email_event_settings import EmailEventSettings





T = TypeVar("T", bound="EmailEventSettingsResponse")



@_attrs_define
class EmailEventSettingsResponse:
    """ 
        Attributes:
            settings (list[EmailEventSettings]):
     """

    settings: list[EmailEventSettings]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.email_event_settings import EmailEventSettings
        settings = []
        for settings_item_data in self.settings:
            settings_item = settings_item_data.to_dict()
            settings.append(settings_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "settings": settings,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.email_event_settings import EmailEventSettings
        d = dict(src_dict)
        settings = []
        _settings = d.pop("settings")
        for settings_item_data in (_settings):
            settings_item = EmailEventSettings.from_dict(settings_item_data)



            settings.append(settings_item)


        email_event_settings_response = cls(
            settings=settings,
        )


        email_event_settings_response.additional_properties = d
        return email_event_settings_response

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.plugin_list_item import PluginListItem





T = TypeVar("T", bound="ListPluginsResponse")



@_attrs_define
class ListPluginsResponse:
    """ Response from listing plugins.

        Attributes:
            plugins (list[PluginListItem]):
            count (int):
     """

    plugins: list[PluginListItem]
    count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.plugin_list_item import PluginListItem
        plugins = []
        for plugins_item_data in self.plugins:
            plugins_item = plugins_item_data.to_dict()
            plugins.append(plugins_item)



        count = self.count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "plugins": plugins,
            "count": count,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plugin_list_item import PluginListItem
        d = dict(src_dict)
        plugins = []
        _plugins = d.pop("plugins")
        for plugins_item_data in (_plugins):
            plugins_item = PluginListItem.from_dict(plugins_item_data)



            plugins.append(plugins_item)


        count = d.pop("count")

        list_plugins_response = cls(
            plugins=plugins,
            count=count,
        )


        list_plugins_response.additional_properties = d
        return list_plugins_response

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.content_filter_category_config_action import ContentFilterCategoryConfigAction
from ..models.content_filter_category_config_severity_threshold import ContentFilterCategoryConfigSeverityThreshold
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ContentFilterCategoryConfig")



@_attrs_define
class ContentFilterCategoryConfig:
    """ category: "harmful_self_harm"
                  enabled: true
                  action: "BLOCK"
                  severity_threshold: "medium"
                  category_file: "/path/to/custom_file.yaml"  # optional override

        Attributes:
            category (str): The category to detect
            action (ContentFilterCategoryConfigAction): The action to take when the category is detected
            enabled (bool | Unset): Whether the category is enabled Default: True.
            severity_threshold (ContentFilterCategoryConfigSeverityThreshold | Unset): The severity threshold to detect the
                category Default: ContentFilterCategoryConfigSeverityThreshold.MEDIUM.
            category_file (None | str | Unset): Optional override. Use your own category file instead of the default one.
     """

    category: str
    action: ContentFilterCategoryConfigAction
    enabled: bool | Unset = True
    severity_threshold: ContentFilterCategoryConfigSeverityThreshold | Unset = ContentFilterCategoryConfigSeverityThreshold.MEDIUM
    category_file: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        category = self.category

        action = self.action.value

        enabled = self.enabled

        severity_threshold: str | Unset = UNSET
        if not isinstance(self.severity_threshold, Unset):
            severity_threshold = self.severity_threshold.value


        category_file: None | str | Unset
        if isinstance(self.category_file, Unset):
            category_file = UNSET
        else:
            category_file = self.category_file


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "category": category,
            "action": action,
        })
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if severity_threshold is not UNSET:
            field_dict["severity_threshold"] = severity_threshold
        if category_file is not UNSET:
            field_dict["category_file"] = category_file

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category")

        action = ContentFilterCategoryConfigAction(d.pop("action"))




        enabled = d.pop("enabled", UNSET)

        _severity_threshold = d.pop("severity_threshold", UNSET)
        severity_threshold: ContentFilterCategoryConfigSeverityThreshold | Unset
        if isinstance(_severity_threshold,  Unset):
            severity_threshold = UNSET
        else:
            severity_threshold = ContentFilterCategoryConfigSeverityThreshold(_severity_threshold)




        def _parse_category_file(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_file = _parse_category_file(d.pop("category_file", UNSET))


        content_filter_category_config = cls(
            category=category,
            action=action,
            enabled=enabled,
            severity_threshold=severity_threshold,
            category_file=category_file,
        )


        content_filter_category_config.additional_properties = d
        return content_filter_category_config

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

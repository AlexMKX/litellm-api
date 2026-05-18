from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.content_filter_action import ContentFilterAction
from ..models.content_filter_pattern_pattern_type import ContentFilterPatternPatternType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ContentFilterPattern")



@_attrs_define
class ContentFilterPattern:
    """ Represents a content filter pattern (prebuilt or custom regex)

        Attributes:
            action (ContentFilterAction): Action to take when content filter detects a match
            pattern_type (ContentFilterPatternPatternType): Type of pattern: 'prebuilt' for predefined patterns or 'regex'
                for custom
            name (None | str | Unset): Name for this pattern (used in logging and error messages)
            pattern (None | str | Unset): Custom regex pattern. Required if pattern_type is 'regex'
            pattern_name (None | str | Unset): Name of prebuilt pattern (e.g., 'us_ssn', 'credit_card'). Required if
                pattern_type is 'prebuilt'
     """

    action: ContentFilterAction
    pattern_type: ContentFilterPatternPatternType
    name: None | str | Unset = UNSET
    pattern: None | str | Unset = UNSET
    pattern_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        pattern_type = self.pattern_type.value

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        pattern: None | str | Unset
        if isinstance(self.pattern, Unset):
            pattern = UNSET
        else:
            pattern = self.pattern

        pattern_name: None | str | Unset
        if isinstance(self.pattern_name, Unset):
            pattern_name = UNSET
        else:
            pattern_name = self.pattern_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "action": action,
            "pattern_type": pattern_type,
        })
        if name is not UNSET:
            field_dict["name"] = name
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if pattern_name is not UNSET:
            field_dict["pattern_name"] = pattern_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = ContentFilterAction(d.pop("action"))




        pattern_type = ContentFilterPatternPatternType(d.pop("pattern_type"))




        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_pattern(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pattern = _parse_pattern(d.pop("pattern", UNSET))


        def _parse_pattern_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pattern_name = _parse_pattern_name(d.pop("pattern_name", UNSET))


        content_filter_pattern = cls(
            action=action,
            pattern_type=pattern_type,
            name=name,
            pattern=pattern,
            pattern_name=pattern_name,
        )


        content_filter_pattern.additional_properties = d
        return content_filter_pattern

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

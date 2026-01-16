from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.agent_credential_field_field_type import AgentCredentialFieldFieldType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AgentCredentialField")



@_attrs_define
class AgentCredentialField:
    """ 
        Attributes:
            key (str):
            label (str):
            placeholder (None | str | Unset):
            tooltip (None | str | Unset):
            required (bool | Unset):  Default: False.
            field_type (AgentCredentialFieldFieldType | Unset):  Default: AgentCredentialFieldFieldType.TEXT.
            options (list[str] | None | Unset):
            default_value (None | str | Unset):
            include_in_litellm_params (bool | None | Unset):
     """

    key: str
    label: str
    placeholder: None | str | Unset = UNSET
    tooltip: None | str | Unset = UNSET
    required: bool | Unset = False
    field_type: AgentCredentialFieldFieldType | Unset = AgentCredentialFieldFieldType.TEXT
    options: list[str] | None | Unset = UNSET
    default_value: None | str | Unset = UNSET
    include_in_litellm_params: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        key = self.key

        label = self.label

        placeholder: None | str | Unset
        if isinstance(self.placeholder, Unset):
            placeholder = UNSET
        else:
            placeholder = self.placeholder

        tooltip: None | str | Unset
        if isinstance(self.tooltip, Unset):
            tooltip = UNSET
        else:
            tooltip = self.tooltip

        required = self.required

        field_type: str | Unset = UNSET
        if not isinstance(self.field_type, Unset):
            field_type = self.field_type.value


        options: list[str] | None | Unset
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, list):
            options = self.options


        else:
            options = self.options

        default_value: None | str | Unset
        if isinstance(self.default_value, Unset):
            default_value = UNSET
        else:
            default_value = self.default_value

        include_in_litellm_params: bool | None | Unset
        if isinstance(self.include_in_litellm_params, Unset):
            include_in_litellm_params = UNSET
        else:
            include_in_litellm_params = self.include_in_litellm_params


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "key": key,
            "label": label,
        })
        if placeholder is not UNSET:
            field_dict["placeholder"] = placeholder
        if tooltip is not UNSET:
            field_dict["tooltip"] = tooltip
        if required is not UNSET:
            field_dict["required"] = required
        if field_type is not UNSET:
            field_dict["field_type"] = field_type
        if options is not UNSET:
            field_dict["options"] = options
        if default_value is not UNSET:
            field_dict["default_value"] = default_value
        if include_in_litellm_params is not UNSET:
            field_dict["include_in_litellm_params"] = include_in_litellm_params

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        label = d.pop("label")

        def _parse_placeholder(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        placeholder = _parse_placeholder(d.pop("placeholder", UNSET))


        def _parse_tooltip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tooltip = _parse_tooltip(d.pop("tooltip", UNSET))


        required = d.pop("required", UNSET)

        _field_type = d.pop("field_type", UNSET)
        field_type: AgentCredentialFieldFieldType | Unset
        if isinstance(_field_type,  Unset):
            field_type = UNSET
        else:
            field_type = AgentCredentialFieldFieldType(_field_type)




        def _parse_options(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                options_type_0 = cast(list[str], data)

                return options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        options = _parse_options(d.pop("options", UNSET))


        def _parse_default_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_value = _parse_default_value(d.pop("default_value", UNSET))


        def _parse_include_in_litellm_params(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_in_litellm_params = _parse_include_in_litellm_params(d.pop("include_in_litellm_params", UNSET))


        agent_credential_field = cls(
            key=key,
            label=label,
            placeholder=placeholder,
            tooltip=tooltip,
            required=required,
            field_type=field_type,
            options=options,
            default_value=default_value,
            include_in_litellm_params=include_in_litellm_params,
        )


        agent_credential_field.additional_properties = d
        return agent_credential_field

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

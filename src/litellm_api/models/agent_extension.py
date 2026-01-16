from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.agent_extension_params_type_0 import AgentExtensionParamsType0





T = TypeVar("T", bound="AgentExtension")



@_attrs_define
class AgentExtension:
    """ A declaration of a protocol extension supported by an Agent.

        Attributes:
            uri (str | Unset):
            description (None | str | Unset):
            required (bool | None | Unset):
            params (AgentExtensionParamsType0 | None | Unset):
     """

    uri: str | Unset = UNSET
    description: None | str | Unset = UNSET
    required: bool | None | Unset = UNSET
    params: AgentExtensionParamsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_extension_params_type_0 import AgentExtensionParamsType0
        uri = self.uri

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        required: bool | None | Unset
        if isinstance(self.required, Unset):
            required = UNSET
        else:
            required = self.required

        params: dict[str, Any] | None | Unset
        if isinstance(self.params, Unset):
            params = UNSET
        elif isinstance(self.params, AgentExtensionParamsType0):
            params = self.params.to_dict()
        else:
            params = self.params


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if uri is not UNSET:
            field_dict["uri"] = uri
        if description is not UNSET:
            field_dict["description"] = description
        if required is not UNSET:
            field_dict["required"] = required
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_extension_params_type_0 import AgentExtensionParamsType0
        d = dict(src_dict)
        uri = d.pop("uri", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_required(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        required = _parse_required(d.pop("required", UNSET))


        def _parse_params(data: object) -> AgentExtensionParamsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                params_type_0 = AgentExtensionParamsType0.from_dict(data)



                return params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentExtensionParamsType0 | None | Unset, data)

        params = _parse_params(d.pop("params", UNSET))


        agent_extension = cls(
            uri=uri,
            description=description,
            required=required,
            params=params,
        )


        agent_extension.additional_properties = d
        return agent_extension

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

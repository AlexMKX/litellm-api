from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.agent_create_info_litellm_params_template_type_0 import AgentCreateInfoLitellmParamsTemplateType0
  from ..models.agent_credential_field import AgentCredentialField





T = TypeVar("T", bound="AgentCreateInfo")



@_attrs_define
class AgentCreateInfo:
    """ 
        Attributes:
            agent_type (str):
            agent_type_display_name (str):
            credential_fields (list[AgentCredentialField]):
            description (None | str | Unset):
            logo_url (None | str | Unset):
            litellm_params_template (AgentCreateInfoLitellmParamsTemplateType0 | None | Unset):
            model_template (None | str | Unset):
     """

    agent_type: str
    agent_type_display_name: str
    credential_fields: list[AgentCredentialField]
    description: None | str | Unset = UNSET
    logo_url: None | str | Unset = UNSET
    litellm_params_template: AgentCreateInfoLitellmParamsTemplateType0 | None | Unset = UNSET
    model_template: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_create_info_litellm_params_template_type_0 import AgentCreateInfoLitellmParamsTemplateType0
        from ..models.agent_credential_field import AgentCredentialField
        agent_type = self.agent_type

        agent_type_display_name = self.agent_type_display_name

        credential_fields = []
        for credential_fields_item_data in self.credential_fields:
            credential_fields_item = credential_fields_item_data.to_dict()
            credential_fields.append(credential_fields_item)



        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        litellm_params_template: dict[str, Any] | None | Unset
        if isinstance(self.litellm_params_template, Unset):
            litellm_params_template = UNSET
        elif isinstance(self.litellm_params_template, AgentCreateInfoLitellmParamsTemplateType0):
            litellm_params_template = self.litellm_params_template.to_dict()
        else:
            litellm_params_template = self.litellm_params_template

        model_template: None | str | Unset
        if isinstance(self.model_template, Unset):
            model_template = UNSET
        else:
            model_template = self.model_template


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "agent_type": agent_type,
            "agent_type_display_name": agent_type_display_name,
            "credential_fields": credential_fields,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if litellm_params_template is not UNSET:
            field_dict["litellm_params_template"] = litellm_params_template
        if model_template is not UNSET:
            field_dict["model_template"] = model_template

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_create_info_litellm_params_template_type_0 import AgentCreateInfoLitellmParamsTemplateType0
        from ..models.agent_credential_field import AgentCredentialField
        d = dict(src_dict)
        agent_type = d.pop("agent_type")

        agent_type_display_name = d.pop("agent_type_display_name")

        credential_fields = []
        _credential_fields = d.pop("credential_fields")
        for credential_fields_item_data in (_credential_fields):
            credential_fields_item = AgentCredentialField.from_dict(credential_fields_item_data)



            credential_fields.append(credential_fields_item)


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))


        def _parse_litellm_params_template(data: object) -> AgentCreateInfoLitellmParamsTemplateType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                litellm_params_template_type_0 = AgentCreateInfoLitellmParamsTemplateType0.from_dict(data)



                return litellm_params_template_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentCreateInfoLitellmParamsTemplateType0 | None | Unset, data)

        litellm_params_template = _parse_litellm_params_template(d.pop("litellm_params_template", UNSET))


        def _parse_model_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_template = _parse_model_template(d.pop("model_template", UNSET))


        agent_create_info = cls(
            agent_type=agent_type,
            agent_type_display_name=agent_type_display_name,
            credential_fields=credential_fields,
            description=description,
            logo_url=logo_url,
            litellm_params_template=litellm_params_template,
            model_template=model_template,
        )


        agent_create_info.additional_properties = d
        return agent_create_info

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

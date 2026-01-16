from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.provider_credential_field import ProviderCredentialField





T = TypeVar("T", bound="ProviderCreateInfo")



@_attrs_define
class ProviderCreateInfo:
    """ 
        Attributes:
            provider (str):
            provider_display_name (str):
            litellm_provider (str):
            credential_fields (list[ProviderCredentialField]):
            default_model_placeholder (None | str | Unset):
     """

    provider: str
    provider_display_name: str
    litellm_provider: str
    credential_fields: list[ProviderCredentialField]
    default_model_placeholder: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.provider_credential_field import ProviderCredentialField
        provider = self.provider

        provider_display_name = self.provider_display_name

        litellm_provider = self.litellm_provider

        credential_fields = []
        for credential_fields_item_data in self.credential_fields:
            credential_fields_item = credential_fields_item_data.to_dict()
            credential_fields.append(credential_fields_item)



        default_model_placeholder: None | str | Unset
        if isinstance(self.default_model_placeholder, Unset):
            default_model_placeholder = UNSET
        else:
            default_model_placeholder = self.default_model_placeholder


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "provider": provider,
            "provider_display_name": provider_display_name,
            "litellm_provider": litellm_provider,
            "credential_fields": credential_fields,
        })
        if default_model_placeholder is not UNSET:
            field_dict["default_model_placeholder"] = default_model_placeholder

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_credential_field import ProviderCredentialField
        d = dict(src_dict)
        provider = d.pop("provider")

        provider_display_name = d.pop("provider_display_name")

        litellm_provider = d.pop("litellm_provider")

        credential_fields = []
        _credential_fields = d.pop("credential_fields")
        for credential_fields_item_data in (_credential_fields):
            credential_fields_item = ProviderCredentialField.from_dict(credential_fields_item_data)



            credential_fields.append(credential_fields_item)


        def _parse_default_model_placeholder(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_model_placeholder = _parse_default_model_placeholder(d.pop("default_model_placeholder", UNSET))


        provider_create_info = cls(
            provider=provider,
            provider_display_name=provider_display_name,
            litellm_provider=litellm_provider,
            credential_fields=credential_fields,
            default_model_placeholder=default_model_placeholder,
        )


        provider_create_info.additional_properties = d
        return provider_create_info

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

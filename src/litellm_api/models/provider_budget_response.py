from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.provider_budget_response_providers import ProviderBudgetResponseProviders





T = TypeVar("T", bound="ProviderBudgetResponse")



@_attrs_define
class ProviderBudgetResponse:
    """ Complete provider budget configuration and status.
    Maps provider names to their budget configs.

        Attributes:
            providers (ProviderBudgetResponseProviders | Unset):
     """

    providers: ProviderBudgetResponseProviders | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.provider_budget_response_providers import ProviderBudgetResponseProviders
        providers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.providers, Unset):
            providers = self.providers.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if providers is not UNSET:
            field_dict["providers"] = providers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_budget_response_providers import ProviderBudgetResponseProviders
        d = dict(src_dict)
        _providers = d.pop("providers", UNSET)
        providers: ProviderBudgetResponseProviders | Unset
        if isinstance(_providers,  Unset):
            providers = UNSET
        else:
            providers = ProviderBudgetResponseProviders.from_dict(_providers)




        provider_budget_response = cls(
            providers=providers,
        )


        provider_budget_response.additional_properties = d
        return provider_budget_response

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

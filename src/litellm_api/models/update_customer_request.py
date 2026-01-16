from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_customer_request_allowed_model_region_type_0 import UpdateCustomerRequestAllowedModelRegionType0
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateCustomerRequest")



@_attrs_define
class UpdateCustomerRequest:
    """ Update a Customer, use this to update customer budgets etc

        Attributes:
            user_id (str):
            alias (None | str | Unset):
            blocked (bool | Unset):  Default: False.
            max_budget (float | None | Unset):
            budget_id (None | str | Unset):
            allowed_model_region (None | Unset | UpdateCustomerRequestAllowedModelRegionType0):
            default_model (None | str | Unset):
     """

    user_id: str
    alias: None | str | Unset = UNSET
    blocked: bool | Unset = False
    max_budget: float | None | Unset = UNSET
    budget_id: None | str | Unset = UNSET
    allowed_model_region: None | Unset | UpdateCustomerRequestAllowedModelRegionType0 = UNSET
    default_model: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        alias: None | str | Unset
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias

        blocked = self.blocked

        max_budget: float | None | Unset
        if isinstance(self.max_budget, Unset):
            max_budget = UNSET
        else:
            max_budget = self.max_budget

        budget_id: None | str | Unset
        if isinstance(self.budget_id, Unset):
            budget_id = UNSET
        else:
            budget_id = self.budget_id

        allowed_model_region: None | str | Unset
        if isinstance(self.allowed_model_region, Unset):
            allowed_model_region = UNSET
        elif isinstance(self.allowed_model_region, UpdateCustomerRequestAllowedModelRegionType0):
            allowed_model_region = self.allowed_model_region.value
        else:
            allowed_model_region = self.allowed_model_region

        default_model: None | str | Unset
        if isinstance(self.default_model, Unset):
            default_model = UNSET
        else:
            default_model = self.default_model


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "user_id": user_id,
        })
        if alias is not UNSET:
            field_dict["alias"] = alias
        if blocked is not UNSET:
            field_dict["blocked"] = blocked
        if max_budget is not UNSET:
            field_dict["max_budget"] = max_budget
        if budget_id is not UNSET:
            field_dict["budget_id"] = budget_id
        if allowed_model_region is not UNSET:
            field_dict["allowed_model_region"] = allowed_model_region
        if default_model is not UNSET:
            field_dict["default_model"] = default_model

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("user_id")

        def _parse_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alias = _parse_alias(d.pop("alias", UNSET))


        blocked = d.pop("blocked", UNSET)

        def _parse_max_budget(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_budget = _parse_max_budget(d.pop("max_budget", UNSET))


        def _parse_budget_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        budget_id = _parse_budget_id(d.pop("budget_id", UNSET))


        def _parse_allowed_model_region(data: object) -> None | Unset | UpdateCustomerRequestAllowedModelRegionType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                allowed_model_region_type_0 = UpdateCustomerRequestAllowedModelRegionType0(data)



                return allowed_model_region_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateCustomerRequestAllowedModelRegionType0, data)

        allowed_model_region = _parse_allowed_model_region(d.pop("allowed_model_region", UNSET))


        def _parse_default_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_model = _parse_default_model(d.pop("default_model", UNSET))


        update_customer_request = cls(
            user_id=user_id,
            alias=alias,
            blocked=blocked,
            max_budget=max_budget,
            budget_id=budget_id,
            allowed_model_region=allowed_model_region,
            default_model=default_model,
        )


        update_customer_request.additional_properties = d
        return update_customer_request

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

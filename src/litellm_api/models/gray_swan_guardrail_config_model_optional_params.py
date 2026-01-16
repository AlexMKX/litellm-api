from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.gray_swan_guardrail_config_model_optional_params_categories_type_0 import GraySwanGuardrailConfigModelOptionalParamsCategoriesType0





T = TypeVar("T", bound="GraySwanGuardrailConfigModelOptionalParams")



@_attrs_define
class GraySwanGuardrailConfigModelOptionalParams:
    """ Optional parameters for the Gray Swan guardrail.

        Attributes:
            on_flagged_action (None | str | Unset): Action when a violation is detected: 'block' rejects the call (400
                error), 'monitor' logs only, 'passthrough' replaces response content with violation message (200 status).
                Default: 'passthrough'.
            violation_threshold (float | None | Unset): Threshold between 0 and 1 at which Gray Swan violations trigger the
                configured action. Default: 0.5.
            reasoning_mode (None | str | Unset): Gray Swan reasoning mode override. Accepted values: 'off', 'hybrid',
                'thinking'.
            policy_id (None | str | Unset): Gray Swan policy identifier to apply during monitoring.
            categories (GraySwanGuardrailConfigModelOptionalParamsCategoriesType0 | None | Unset): Default Gray Swan
                category definitions to send with each request.
     """

    on_flagged_action: None | str | Unset = 'passthrough'
    violation_threshold: float | None | Unset = 0.5
    reasoning_mode: None | str | Unset = UNSET
    policy_id: None | str | Unset = UNSET
    categories: GraySwanGuardrailConfigModelOptionalParamsCategoriesType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.gray_swan_guardrail_config_model_optional_params_categories_type_0 import GraySwanGuardrailConfigModelOptionalParamsCategoriesType0
        on_flagged_action: None | str | Unset
        if isinstance(self.on_flagged_action, Unset):
            on_flagged_action = UNSET
        else:
            on_flagged_action = self.on_flagged_action

        violation_threshold: float | None | Unset
        if isinstance(self.violation_threshold, Unset):
            violation_threshold = UNSET
        else:
            violation_threshold = self.violation_threshold

        reasoning_mode: None | str | Unset
        if isinstance(self.reasoning_mode, Unset):
            reasoning_mode = UNSET
        else:
            reasoning_mode = self.reasoning_mode

        policy_id: None | str | Unset
        if isinstance(self.policy_id, Unset):
            policy_id = UNSET
        else:
            policy_id = self.policy_id

        categories: dict[str, Any] | None | Unset
        if isinstance(self.categories, Unset):
            categories = UNSET
        elif isinstance(self.categories, GraySwanGuardrailConfigModelOptionalParamsCategoriesType0):
            categories = self.categories.to_dict()
        else:
            categories = self.categories


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if on_flagged_action is not UNSET:
            field_dict["on_flagged_action"] = on_flagged_action
        if violation_threshold is not UNSET:
            field_dict["violation_threshold"] = violation_threshold
        if reasoning_mode is not UNSET:
            field_dict["reasoning_mode"] = reasoning_mode
        if policy_id is not UNSET:
            field_dict["policy_id"] = policy_id
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gray_swan_guardrail_config_model_optional_params_categories_type_0 import GraySwanGuardrailConfigModelOptionalParamsCategoriesType0
        d = dict(src_dict)
        def _parse_on_flagged_action(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        on_flagged_action = _parse_on_flagged_action(d.pop("on_flagged_action", UNSET))


        def _parse_violation_threshold(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        violation_threshold = _parse_violation_threshold(d.pop("violation_threshold", UNSET))


        def _parse_reasoning_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reasoning_mode = _parse_reasoning_mode(d.pop("reasoning_mode", UNSET))


        def _parse_policy_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        policy_id = _parse_policy_id(d.pop("policy_id", UNSET))


        def _parse_categories(data: object) -> GraySwanGuardrailConfigModelOptionalParamsCategoriesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                categories_type_0 = GraySwanGuardrailConfigModelOptionalParamsCategoriesType0.from_dict(data)



                return categories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GraySwanGuardrailConfigModelOptionalParamsCategoriesType0 | None | Unset, data)

        categories = _parse_categories(d.pop("categories", UNSET))


        gray_swan_guardrail_config_model_optional_params = cls(
            on_flagged_action=on_flagged_action,
            violation_threshold=violation_threshold,
            reasoning_mode=reasoning_mode,
            policy_id=policy_id,
            categories=categories,
        )


        gray_swan_guardrail_config_model_optional_params.additional_properties = d
        return gray_swan_guardrail_config_model_optional_params

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

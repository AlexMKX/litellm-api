from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.policy_condition_request import PolicyConditionRequest
  from ..models.policy_update_request_pipeline_type_0 import PolicyUpdateRequestPipelineType0





T = TypeVar("T", bound="PolicyUpdateRequest")



@_attrs_define
class PolicyUpdateRequest:
    """ Request body for updating a policy.

        Attributes:
            condition (None | PolicyConditionRequest | Unset): Condition for when this policy applies.
            description (None | str | Unset): Human-readable description of the policy.
            guardrails_add (list[str] | None | Unset): List of guardrail names to add.
            guardrails_remove (list[str] | None | Unset): List of guardrail names to remove (from inherited).
            inherit (None | str | Unset): Name of parent policy to inherit from.
            pipeline (None | PolicyUpdateRequestPipelineType0 | Unset): Optional guardrail pipeline for ordered execution.
                Contains 'mode' and 'steps'.
            policy_name (None | str | Unset): New name for the policy.
     """

    condition: None | PolicyConditionRequest | Unset = UNSET
    description: None | str | Unset = UNSET
    guardrails_add: list[str] | None | Unset = UNSET
    guardrails_remove: list[str] | None | Unset = UNSET
    inherit: None | str | Unset = UNSET
    pipeline: None | PolicyUpdateRequestPipelineType0 | Unset = UNSET
    policy_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.policy_condition_request import PolicyConditionRequest
        from ..models.policy_update_request_pipeline_type_0 import PolicyUpdateRequestPipelineType0
        condition: dict[str, Any] | None | Unset
        if isinstance(self.condition, Unset):
            condition = UNSET
        elif isinstance(self.condition, PolicyConditionRequest):
            condition = self.condition.to_dict()
        else:
            condition = self.condition

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        guardrails_add: list[str] | None | Unset
        if isinstance(self.guardrails_add, Unset):
            guardrails_add = UNSET
        elif isinstance(self.guardrails_add, list):
            guardrails_add = self.guardrails_add


        else:
            guardrails_add = self.guardrails_add

        guardrails_remove: list[str] | None | Unset
        if isinstance(self.guardrails_remove, Unset):
            guardrails_remove = UNSET
        elif isinstance(self.guardrails_remove, list):
            guardrails_remove = self.guardrails_remove


        else:
            guardrails_remove = self.guardrails_remove

        inherit: None | str | Unset
        if isinstance(self.inherit, Unset):
            inherit = UNSET
        else:
            inherit = self.inherit

        pipeline: dict[str, Any] | None | Unset
        if isinstance(self.pipeline, Unset):
            pipeline = UNSET
        elif isinstance(self.pipeline, PolicyUpdateRequestPipelineType0):
            pipeline = self.pipeline.to_dict()
        else:
            pipeline = self.pipeline

        policy_name: None | str | Unset
        if isinstance(self.policy_name, Unset):
            policy_name = UNSET
        else:
            policy_name = self.policy_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if condition is not UNSET:
            field_dict["condition"] = condition
        if description is not UNSET:
            field_dict["description"] = description
        if guardrails_add is not UNSET:
            field_dict["guardrails_add"] = guardrails_add
        if guardrails_remove is not UNSET:
            field_dict["guardrails_remove"] = guardrails_remove
        if inherit is not UNSET:
            field_dict["inherit"] = inherit
        if pipeline is not UNSET:
            field_dict["pipeline"] = pipeline
        if policy_name is not UNSET:
            field_dict["policy_name"] = policy_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.policy_condition_request import PolicyConditionRequest
        from ..models.policy_update_request_pipeline_type_0 import PolicyUpdateRequestPipelineType0
        d = dict(src_dict)
        def _parse_condition(data: object) -> None | PolicyConditionRequest | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                condition_type_0 = PolicyConditionRequest.from_dict(data)



                return condition_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PolicyConditionRequest | Unset, data)

        condition = _parse_condition(d.pop("condition", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_guardrails_add(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                guardrails_add_type_0 = cast(list[str], data)

                return guardrails_add_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        guardrails_add = _parse_guardrails_add(d.pop("guardrails_add", UNSET))


        def _parse_guardrails_remove(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                guardrails_remove_type_0 = cast(list[str], data)

                return guardrails_remove_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        guardrails_remove = _parse_guardrails_remove(d.pop("guardrails_remove", UNSET))


        def _parse_inherit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        inherit = _parse_inherit(d.pop("inherit", UNSET))


        def _parse_pipeline(data: object) -> None | PolicyUpdateRequestPipelineType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pipeline_type_0 = PolicyUpdateRequestPipelineType0.from_dict(data)



                return pipeline_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PolicyUpdateRequestPipelineType0 | Unset, data)

        pipeline = _parse_pipeline(d.pop("pipeline", UNSET))


        def _parse_policy_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        policy_name = _parse_policy_name(d.pop("policy_name", UNSET))


        policy_update_request = cls(
            condition=condition,
            description=description,
            guardrails_add=guardrails_add,
            guardrails_remove=guardrails_remove,
            inherit=inherit,
            pipeline=pipeline,
            policy_name=policy_name,
        )


        policy_update_request.additional_properties = d
        return policy_update_request

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

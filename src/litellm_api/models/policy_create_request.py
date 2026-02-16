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
  from ..models.policy_create_request_pipeline_type_0 import PolicyCreateRequestPipelineType0





T = TypeVar("T", bound="PolicyCreateRequest")



@_attrs_define
class PolicyCreateRequest:
    """ Request body for creating a new policy.

        Attributes:
            policy_name (str): Unique name for the policy.
            inherit (None | str | Unset): Name of parent policy to inherit from.
            description (None | str | Unset): Human-readable description of the policy.
            guardrails_add (list[str] | None | Unset): List of guardrail names to add.
            guardrails_remove (list[str] | None | Unset): List of guardrail names to remove (from inherited).
            condition (None | PolicyConditionRequest | Unset): Condition for when this policy applies.
            pipeline (None | PolicyCreateRequestPipelineType0 | Unset): Optional guardrail pipeline for ordered execution.
                Contains 'mode' and 'steps'.
     """

    policy_name: str
    inherit: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    guardrails_add: list[str] | None | Unset = UNSET
    guardrails_remove: list[str] | None | Unset = UNSET
    condition: None | PolicyConditionRequest | Unset = UNSET
    pipeline: None | PolicyCreateRequestPipelineType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.policy_condition_request import PolicyConditionRequest
        from ..models.policy_create_request_pipeline_type_0 import PolicyCreateRequestPipelineType0
        policy_name = self.policy_name

        inherit: None | str | Unset
        if isinstance(self.inherit, Unset):
            inherit = UNSET
        else:
            inherit = self.inherit

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

        condition: dict[str, Any] | None | Unset
        if isinstance(self.condition, Unset):
            condition = UNSET
        elif isinstance(self.condition, PolicyConditionRequest):
            condition = self.condition.to_dict()
        else:
            condition = self.condition

        pipeline: dict[str, Any] | None | Unset
        if isinstance(self.pipeline, Unset):
            pipeline = UNSET
        elif isinstance(self.pipeline, PolicyCreateRequestPipelineType0):
            pipeline = self.pipeline.to_dict()
        else:
            pipeline = self.pipeline


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "policy_name": policy_name,
        })
        if inherit is not UNSET:
            field_dict["inherit"] = inherit
        if description is not UNSET:
            field_dict["description"] = description
        if guardrails_add is not UNSET:
            field_dict["guardrails_add"] = guardrails_add
        if guardrails_remove is not UNSET:
            field_dict["guardrails_remove"] = guardrails_remove
        if condition is not UNSET:
            field_dict["condition"] = condition
        if pipeline is not UNSET:
            field_dict["pipeline"] = pipeline

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.policy_condition_request import PolicyConditionRequest
        from ..models.policy_create_request_pipeline_type_0 import PolicyCreateRequestPipelineType0
        d = dict(src_dict)
        policy_name = d.pop("policy_name")

        def _parse_inherit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        inherit = _parse_inherit(d.pop("inherit", UNSET))


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


        def _parse_pipeline(data: object) -> None | PolicyCreateRequestPipelineType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pipeline_type_0 = PolicyCreateRequestPipelineType0.from_dict(data)



                return pipeline_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PolicyCreateRequestPipelineType0 | Unset, data)

        pipeline = _parse_pipeline(d.pop("pipeline", UNSET))


        policy_create_request = cls(
            policy_name=policy_name,
            inherit=inherit,
            description=description,
            guardrails_add=guardrails_add,
            guardrails_remove=guardrails_remove,
            condition=condition,
            pipeline=pipeline,
        )


        policy_create_request.additional_properties = d
        return policy_create_request

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

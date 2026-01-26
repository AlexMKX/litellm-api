from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.policy_guardrails_response import PolicyGuardrailsResponse
  from ..models.policy_scope_response import PolicyScopeResponse





T = TypeVar("T", bound="PolicyInfoResponse")



@_attrs_define
class PolicyInfoResponse:
    """ Response for /policy/info/{policy_name} endpoint.

        Attributes:
            policy_name (str):
            scope (PolicyScopeResponse): Scope configuration for a policy.
            guardrails (PolicyGuardrailsResponse): Guardrails configuration for a policy.
            resolved_guardrails (list[str]):
            inheritance_chain (list[str]):
            inherit (None | str | Unset):
     """

    policy_name: str
    scope: PolicyScopeResponse
    guardrails: PolicyGuardrailsResponse
    resolved_guardrails: list[str]
    inheritance_chain: list[str]
    inherit: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.policy_scope_response import PolicyScopeResponse
        from ..models.policy_guardrails_response import PolicyGuardrailsResponse
        policy_name = self.policy_name

        scope = self.scope.to_dict()

        guardrails = self.guardrails.to_dict()

        resolved_guardrails = self.resolved_guardrails



        inheritance_chain = self.inheritance_chain



        inherit: None | str | Unset
        if isinstance(self.inherit, Unset):
            inherit = UNSET
        else:
            inherit = self.inherit


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "policy_name": policy_name,
            "scope": scope,
            "guardrails": guardrails,
            "resolved_guardrails": resolved_guardrails,
            "inheritance_chain": inheritance_chain,
        })
        if inherit is not UNSET:
            field_dict["inherit"] = inherit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.policy_guardrails_response import PolicyGuardrailsResponse
        from ..models.policy_scope_response import PolicyScopeResponse
        d = dict(src_dict)
        policy_name = d.pop("policy_name")

        scope = PolicyScopeResponse.from_dict(d.pop("scope"))




        guardrails = PolicyGuardrailsResponse.from_dict(d.pop("guardrails"))




        resolved_guardrails = cast(list[str], d.pop("resolved_guardrails"))


        inheritance_chain = cast(list[str], d.pop("inheritance_chain"))


        def _parse_inherit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        inherit = _parse_inherit(d.pop("inherit", UNSET))


        policy_info_response = cls(
            policy_name=policy_name,
            scope=scope,
            guardrails=guardrails,
            resolved_guardrails=resolved_guardrails,
            inheritance_chain=inheritance_chain,
            inherit=inherit,
        )


        policy_info_response.additional_properties = d
        return policy_info_response

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

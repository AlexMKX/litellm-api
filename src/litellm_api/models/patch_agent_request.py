from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.agent_card import AgentCard
  from ..models.agent_object_permission import AgentObjectPermission
  from ..models.patch_agent_request_litellm_params import PatchAgentRequestLitellmParams





T = TypeVar("T", bound="PatchAgentRequest")



@_attrs_define
class PatchAgentRequest:
    """ 
        Attributes:
            agent_name (str | Unset):
            agent_card_params (AgentCard | Unset): The AgentCard is a self-describing manifest for an agent.
                It provides essential metadata including the agent's identity, capabilities,
                skills, supported communication methods, and security requirements.
            litellm_params (PatchAgentRequestLitellmParams | Unset):
            object_permission (AgentObjectPermission | Unset):
     """

    agent_name: str | Unset = UNSET
    agent_card_params: AgentCard | Unset = UNSET
    litellm_params: PatchAgentRequestLitellmParams | Unset = UNSET
    object_permission: AgentObjectPermission | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_card import AgentCard
        from ..models.agent_object_permission import AgentObjectPermission
        from ..models.patch_agent_request_litellm_params import PatchAgentRequestLitellmParams
        agent_name = self.agent_name

        agent_card_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.agent_card_params, Unset):
            agent_card_params = self.agent_card_params.to_dict()

        litellm_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.litellm_params, Unset):
            litellm_params = self.litellm_params.to_dict()

        object_permission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.object_permission, Unset):
            object_permission = self.object_permission.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if agent_name is not UNSET:
            field_dict["agent_name"] = agent_name
        if agent_card_params is not UNSET:
            field_dict["agent_card_params"] = agent_card_params
        if litellm_params is not UNSET:
            field_dict["litellm_params"] = litellm_params
        if object_permission is not UNSET:
            field_dict["object_permission"] = object_permission

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_card import AgentCard
        from ..models.agent_object_permission import AgentObjectPermission
        from ..models.patch_agent_request_litellm_params import PatchAgentRequestLitellmParams
        d = dict(src_dict)
        agent_name = d.pop("agent_name", UNSET)

        _agent_card_params = d.pop("agent_card_params", UNSET)
        agent_card_params: AgentCard | Unset
        if isinstance(_agent_card_params,  Unset):
            agent_card_params = UNSET
        else:
            agent_card_params = AgentCard.from_dict(_agent_card_params)




        _litellm_params = d.pop("litellm_params", UNSET)
        litellm_params: PatchAgentRequestLitellmParams | Unset
        if isinstance(_litellm_params,  Unset):
            litellm_params = UNSET
        else:
            litellm_params = PatchAgentRequestLitellmParams.from_dict(_litellm_params)




        _object_permission = d.pop("object_permission", UNSET)
        object_permission: AgentObjectPermission | Unset
        if isinstance(_object_permission,  Unset):
            object_permission = UNSET
        else:
            object_permission = AgentObjectPermission.from_dict(_object_permission)




        patch_agent_request = cls(
            agent_name=agent_name,
            agent_card_params=agent_card_params,
            litellm_params=litellm_params,
            object_permission=object_permission,
        )


        patch_agent_request.additional_properties = d
        return patch_agent_request

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

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
  from ..models.agent_config_litellm_params import AgentConfigLitellmParams





T = TypeVar("T", bound="AgentConfig")



@_attrs_define
class AgentConfig:
    """ 
        Attributes:
            agent_name (str):
            agent_card_params (AgentCard): The AgentCard is a self-describing manifest for an agent.
                It provides essential metadata including the agent's identity, capabilities,
                skills, supported communication methods, and security requirements.
            litellm_params (AgentConfigLitellmParams | Unset):
     """

    agent_name: str
    agent_card_params: AgentCard
    litellm_params: AgentConfigLitellmParams | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_config_litellm_params import AgentConfigLitellmParams
        from ..models.agent_card import AgentCard
        agent_name = self.agent_name

        agent_card_params = self.agent_card_params.to_dict()

        litellm_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.litellm_params, Unset):
            litellm_params = self.litellm_params.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "agent_name": agent_name,
            "agent_card_params": agent_card_params,
        })
        if litellm_params is not UNSET:
            field_dict["litellm_params"] = litellm_params

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_card import AgentCard
        from ..models.agent_config_litellm_params import AgentConfigLitellmParams
        d = dict(src_dict)
        agent_name = d.pop("agent_name")

        agent_card_params = AgentCard.from_dict(d.pop("agent_card_params"))




        _litellm_params = d.pop("litellm_params", UNSET)
        litellm_params: AgentConfigLitellmParams | Unset
        if isinstance(_litellm_params,  Unset):
            litellm_params = UNSET
        else:
            litellm_params = AgentConfigLitellmParams.from_dict(_litellm_params)




        agent_config = cls(
            agent_name=agent_name,
            agent_card_params=agent_card_params,
            litellm_params=litellm_params,
        )


        agent_config.additional_properties = d
        return agent_config

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

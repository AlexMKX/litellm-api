from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.agent_response_agent_card_params import AgentResponseAgentCardParams
  from ..models.agent_response_litellm_params_type_0 import AgentResponseLitellmParamsType0





T = TypeVar("T", bound="AgentResponse")



@_attrs_define
class AgentResponse:
    """ 
        Attributes:
            agent_id (str):
            agent_name (str):
            agent_card_params (AgentResponseAgentCardParams):
            litellm_params (AgentResponseLitellmParamsType0 | None | Unset):
            created_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | None | Unset):
            created_by (None | str | Unset):
            updated_by (None | str | Unset):
     """

    agent_id: str
    agent_name: str
    agent_card_params: AgentResponseAgentCardParams
    litellm_params: AgentResponseLitellmParamsType0 | None | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    created_by: None | str | Unset = UNSET
    updated_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_response_litellm_params_type_0 import AgentResponseLitellmParamsType0
        from ..models.agent_response_agent_card_params import AgentResponseAgentCardParams
        agent_id = self.agent_id

        agent_name = self.agent_name

        agent_card_params = self.agent_card_params.to_dict()

        litellm_params: dict[str, Any] | None | Unset
        if isinstance(self.litellm_params, Unset):
            litellm_params = UNSET
        elif isinstance(self.litellm_params, AgentResponseLitellmParamsType0):
            litellm_params = self.litellm_params.to_dict()
        else:
            litellm_params = self.litellm_params

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        updated_by: None | str | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = self.updated_by


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "agent_id": agent_id,
            "agent_name": agent_name,
            "agent_card_params": agent_card_params,
        })
        if litellm_params is not UNSET:
            field_dict["litellm_params"] = litellm_params
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_response_agent_card_params import AgentResponseAgentCardParams
        from ..models.agent_response_litellm_params_type_0 import AgentResponseLitellmParamsType0
        d = dict(src_dict)
        agent_id = d.pop("agent_id")

        agent_name = d.pop("agent_name")

        agent_card_params = AgentResponseAgentCardParams.from_dict(d.pop("agent_card_params"))




        def _parse_litellm_params(data: object) -> AgentResponseLitellmParamsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                litellm_params_type_0 = AgentResponseLitellmParamsType0.from_dict(data)



                return litellm_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentResponseLitellmParamsType0 | None | Unset, data)

        litellm_params = _parse_litellm_params(d.pop("litellm_params", UNSET))


        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)



                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))


        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)



                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))


        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))


        def _parse_updated_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))


        agent_response = cls(
            agent_id=agent_id,
            agent_name=agent_name,
            agent_card_params=agent_card_params,
            litellm_params=litellm_params,
            created_at=created_at,
            updated_at=updated_at,
            created_by=created_by,
            updated_by=updated_by,
        )


        agent_response.additional_properties = d
        return agent_response

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

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
  from ..models.agent_config_static_headers_type_0 import AgentConfigStaticHeadersType0
  from ..models.agent_object_permission import AgentObjectPermission





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
            object_permission (AgentObjectPermission | Unset):
            tpm_limit (int | None | Unset):
            rpm_limit (int | None | Unset):
            session_tpm_limit (int | None | Unset):
            session_rpm_limit (int | None | Unset):
            static_headers (AgentConfigStaticHeadersType0 | None | Unset):
            extra_headers (list[str] | None | Unset):
     """

    agent_name: str
    agent_card_params: AgentCard
    litellm_params: AgentConfigLitellmParams | Unset = UNSET
    object_permission: AgentObjectPermission | Unset = UNSET
    tpm_limit: int | None | Unset = UNSET
    rpm_limit: int | None | Unset = UNSET
    session_tpm_limit: int | None | Unset = UNSET
    session_rpm_limit: int | None | Unset = UNSET
    static_headers: AgentConfigStaticHeadersType0 | None | Unset = UNSET
    extra_headers: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_card import AgentCard
        from ..models.agent_config_litellm_params import AgentConfigLitellmParams
        from ..models.agent_config_static_headers_type_0 import AgentConfigStaticHeadersType0
        from ..models.agent_object_permission import AgentObjectPermission
        agent_name = self.agent_name

        agent_card_params = self.agent_card_params.to_dict()

        litellm_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.litellm_params, Unset):
            litellm_params = self.litellm_params.to_dict()

        object_permission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.object_permission, Unset):
            object_permission = self.object_permission.to_dict()

        tpm_limit: int | None | Unset
        if isinstance(self.tpm_limit, Unset):
            tpm_limit = UNSET
        else:
            tpm_limit = self.tpm_limit

        rpm_limit: int | None | Unset
        if isinstance(self.rpm_limit, Unset):
            rpm_limit = UNSET
        else:
            rpm_limit = self.rpm_limit

        session_tpm_limit: int | None | Unset
        if isinstance(self.session_tpm_limit, Unset):
            session_tpm_limit = UNSET
        else:
            session_tpm_limit = self.session_tpm_limit

        session_rpm_limit: int | None | Unset
        if isinstance(self.session_rpm_limit, Unset):
            session_rpm_limit = UNSET
        else:
            session_rpm_limit = self.session_rpm_limit

        static_headers: dict[str, Any] | None | Unset
        if isinstance(self.static_headers, Unset):
            static_headers = UNSET
        elif isinstance(self.static_headers, AgentConfigStaticHeadersType0):
            static_headers = self.static_headers.to_dict()
        else:
            static_headers = self.static_headers

        extra_headers: list[str] | None | Unset
        if isinstance(self.extra_headers, Unset):
            extra_headers = UNSET
        elif isinstance(self.extra_headers, list):
            extra_headers = self.extra_headers


        else:
            extra_headers = self.extra_headers


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "agent_name": agent_name,
            "agent_card_params": agent_card_params,
        })
        if litellm_params is not UNSET:
            field_dict["litellm_params"] = litellm_params
        if object_permission is not UNSET:
            field_dict["object_permission"] = object_permission
        if tpm_limit is not UNSET:
            field_dict["tpm_limit"] = tpm_limit
        if rpm_limit is not UNSET:
            field_dict["rpm_limit"] = rpm_limit
        if session_tpm_limit is not UNSET:
            field_dict["session_tpm_limit"] = session_tpm_limit
        if session_rpm_limit is not UNSET:
            field_dict["session_rpm_limit"] = session_rpm_limit
        if static_headers is not UNSET:
            field_dict["static_headers"] = static_headers
        if extra_headers is not UNSET:
            field_dict["extra_headers"] = extra_headers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_card import AgentCard
        from ..models.agent_config_litellm_params import AgentConfigLitellmParams
        from ..models.agent_config_static_headers_type_0 import AgentConfigStaticHeadersType0
        from ..models.agent_object_permission import AgentObjectPermission
        d = dict(src_dict)
        agent_name = d.pop("agent_name")

        agent_card_params = AgentCard.from_dict(d.pop("agent_card_params"))




        _litellm_params = d.pop("litellm_params", UNSET)
        litellm_params: AgentConfigLitellmParams | Unset
        if isinstance(_litellm_params,  Unset):
            litellm_params = UNSET
        else:
            litellm_params = AgentConfigLitellmParams.from_dict(_litellm_params)




        _object_permission = d.pop("object_permission", UNSET)
        object_permission: AgentObjectPermission | Unset
        if isinstance(_object_permission,  Unset):
            object_permission = UNSET
        else:
            object_permission = AgentObjectPermission.from_dict(_object_permission)




        def _parse_tpm_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tpm_limit = _parse_tpm_limit(d.pop("tpm_limit", UNSET))


        def _parse_rpm_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rpm_limit = _parse_rpm_limit(d.pop("rpm_limit", UNSET))


        def _parse_session_tpm_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        session_tpm_limit = _parse_session_tpm_limit(d.pop("session_tpm_limit", UNSET))


        def _parse_session_rpm_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        session_rpm_limit = _parse_session_rpm_limit(d.pop("session_rpm_limit", UNSET))


        def _parse_static_headers(data: object) -> AgentConfigStaticHeadersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                static_headers_type_0 = AgentConfigStaticHeadersType0.from_dict(data)



                return static_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentConfigStaticHeadersType0 | None | Unset, data)

        static_headers = _parse_static_headers(d.pop("static_headers", UNSET))


        def _parse_extra_headers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                extra_headers_type_0 = cast(list[str], data)

                return extra_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        extra_headers = _parse_extra_headers(d.pop("extra_headers", UNSET))


        agent_config = cls(
            agent_name=agent_name,
            agent_card_params=agent_card_params,
            litellm_params=litellm_params,
            object_permission=object_permission,
            tpm_limit=tpm_limit,
            rpm_limit=rpm_limit,
            session_tpm_limit=session_tpm_limit,
            session_rpm_limit=session_rpm_limit,
            static_headers=static_headers,
            extra_headers=extra_headers,
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

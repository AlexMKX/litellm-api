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
  from ..models.agent_response_object_permission_type_0 import AgentResponseObjectPermissionType0
  from ..models.agent_response_static_headers_type_0 import AgentResponseStaticHeadersType0





T = TypeVar("T", bound="AgentResponse")



@_attrs_define
class AgentResponse:
    """ 
        Attributes:
            agent_id (str):
            agent_name (str):
            agent_card_params (AgentResponseAgentCardParams):
            litellm_params (AgentResponseLitellmParamsType0 | None | Unset):
            object_permission (AgentResponseObjectPermissionType0 | None | Unset):
            spend (float | None | Unset):
            tpm_limit (int | None | Unset):
            rpm_limit (int | None | Unset):
            session_tpm_limit (int | None | Unset):
            session_rpm_limit (int | None | Unset):
            static_headers (AgentResponseStaticHeadersType0 | None | Unset):
            extra_headers (list[str] | None | Unset):
            created_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | None | Unset):
            created_by (None | str | Unset):
            updated_by (None | str | Unset):
     """

    agent_id: str
    agent_name: str
    agent_card_params: AgentResponseAgentCardParams
    litellm_params: AgentResponseLitellmParamsType0 | None | Unset = UNSET
    object_permission: AgentResponseObjectPermissionType0 | None | Unset = UNSET
    spend: float | None | Unset = UNSET
    tpm_limit: int | None | Unset = UNSET
    rpm_limit: int | None | Unset = UNSET
    session_tpm_limit: int | None | Unset = UNSET
    session_rpm_limit: int | None | Unset = UNSET
    static_headers: AgentResponseStaticHeadersType0 | None | Unset = UNSET
    extra_headers: list[str] | None | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    created_by: None | str | Unset = UNSET
    updated_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_response_agent_card_params import AgentResponseAgentCardParams
        from ..models.agent_response_litellm_params_type_0 import AgentResponseLitellmParamsType0
        from ..models.agent_response_object_permission_type_0 import AgentResponseObjectPermissionType0
        from ..models.agent_response_static_headers_type_0 import AgentResponseStaticHeadersType0
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

        object_permission: dict[str, Any] | None | Unset
        if isinstance(self.object_permission, Unset):
            object_permission = UNSET
        elif isinstance(self.object_permission, AgentResponseObjectPermissionType0):
            object_permission = self.object_permission.to_dict()
        else:
            object_permission = self.object_permission

        spend: float | None | Unset
        if isinstance(self.spend, Unset):
            spend = UNSET
        else:
            spend = self.spend

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
        elif isinstance(self.static_headers, AgentResponseStaticHeadersType0):
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
        if object_permission is not UNSET:
            field_dict["object_permission"] = object_permission
        if spend is not UNSET:
            field_dict["spend"] = spend
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
        from ..models.agent_response_object_permission_type_0 import AgentResponseObjectPermissionType0
        from ..models.agent_response_static_headers_type_0 import AgentResponseStaticHeadersType0
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


        def _parse_object_permission(data: object) -> AgentResponseObjectPermissionType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                object_permission_type_0 = AgentResponseObjectPermissionType0.from_dict(data)



                return object_permission_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentResponseObjectPermissionType0 | None | Unset, data)

        object_permission = _parse_object_permission(d.pop("object_permission", UNSET))


        def _parse_spend(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        spend = _parse_spend(d.pop("spend", UNSET))


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


        def _parse_static_headers(data: object) -> AgentResponseStaticHeadersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                static_headers_type_0 = AgentResponseStaticHeadersType0.from_dict(data)



                return static_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentResponseStaticHeadersType0 | None | Unset, data)

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
            object_permission=object_permission,
            spend=spend,
            tpm_limit=tpm_limit,
            rpm_limit=rpm_limit,
            session_tpm_limit=session_tpm_limit,
            session_rpm_limit=session_rpm_limit,
            static_headers=static_headers,
            extra_headers=extra_headers,
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

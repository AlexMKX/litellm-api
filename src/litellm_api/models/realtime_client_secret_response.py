from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.realtime_client_secret_response_session_type_0 import RealtimeClientSecretResponseSessionType0





T = TypeVar("T", bound="RealtimeClientSecretResponse")



@_attrs_define
class RealtimeClientSecretResponse:
    """ Response from POST /v1/realtime/client_secrets.

    Both the top-level `value` and `session.client_secret.value`
    will contain the encrypted token instead of the raw ephemeral key.
    The `session` field is kept as a raw dict so unknown fields pass through.

        Attributes:
            value (str):
            expires_at (int | None | Unset):
            session (None | RealtimeClientSecretResponseSessionType0 | Unset):
     """

    value: str
    expires_at: int | None | Unset = UNSET
    session: None | RealtimeClientSecretResponseSessionType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.realtime_client_secret_response_session_type_0 import RealtimeClientSecretResponseSessionType0
        value = self.value

        expires_at: int | None | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = self.expires_at

        session: dict[str, Any] | None | Unset
        if isinstance(self.session, Unset):
            session = UNSET
        elif isinstance(self.session, RealtimeClientSecretResponseSessionType0):
            session = self.session.to_dict()
        else:
            session = self.session


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "value": value,
        })
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if session is not UNSET:
            field_dict["session"] = session

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.realtime_client_secret_response_session_type_0 import RealtimeClientSecretResponseSessionType0
        d = dict(src_dict)
        value = d.pop("value")

        def _parse_expires_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))


        def _parse_session(data: object) -> None | RealtimeClientSecretResponseSessionType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                session_type_0 = RealtimeClientSecretResponseSessionType0.from_dict(data)



                return session_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RealtimeClientSecretResponseSessionType0 | Unset, data)

        session = _parse_session(d.pop("session", UNSET))


        realtime_client_secret_response = cls(
            value=value,
            expires_at=expires_at,
            session=session,
        )


        realtime_client_secret_response.additional_properties = d
        return realtime_client_secret_response

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

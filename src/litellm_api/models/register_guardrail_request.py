from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.register_guardrail_request_guardrail_info_type_0 import RegisterGuardrailRequestGuardrailInfoType0
  from ..models.register_guardrail_request_litellm_params import RegisterGuardrailRequestLitellmParams





T = TypeVar("T", bound="RegisterGuardrailRequest")



@_attrs_define
class RegisterGuardrailRequest:
    """ Request body for POST /guardrails/register. Follows Generic Guardrail API config.

        Attributes:
            guardrail_name (str):
            litellm_params (RegisterGuardrailRequestLitellmParams):
            guardrail_info (None | RegisterGuardrailRequestGuardrailInfoType0 | Unset):
            team_id (None | str | Unset):
     """

    guardrail_name: str
    litellm_params: RegisterGuardrailRequestLitellmParams
    guardrail_info: None | RegisterGuardrailRequestGuardrailInfoType0 | Unset = UNSET
    team_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.register_guardrail_request_guardrail_info_type_0 import RegisterGuardrailRequestGuardrailInfoType0
        from ..models.register_guardrail_request_litellm_params import RegisterGuardrailRequestLitellmParams
        guardrail_name = self.guardrail_name

        litellm_params = self.litellm_params.to_dict()

        guardrail_info: dict[str, Any] | None | Unset
        if isinstance(self.guardrail_info, Unset):
            guardrail_info = UNSET
        elif isinstance(self.guardrail_info, RegisterGuardrailRequestGuardrailInfoType0):
            guardrail_info = self.guardrail_info.to_dict()
        else:
            guardrail_info = self.guardrail_info

        team_id: None | str | Unset
        if isinstance(self.team_id, Unset):
            team_id = UNSET
        else:
            team_id = self.team_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "guardrail_name": guardrail_name,
            "litellm_params": litellm_params,
        })
        if guardrail_info is not UNSET:
            field_dict["guardrail_info"] = guardrail_info
        if team_id is not UNSET:
            field_dict["team_id"] = team_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.register_guardrail_request_guardrail_info_type_0 import RegisterGuardrailRequestGuardrailInfoType0
        from ..models.register_guardrail_request_litellm_params import RegisterGuardrailRequestLitellmParams
        d = dict(src_dict)
        guardrail_name = d.pop("guardrail_name")

        litellm_params = RegisterGuardrailRequestLitellmParams.from_dict(d.pop("litellm_params"))




        def _parse_guardrail_info(data: object) -> None | RegisterGuardrailRequestGuardrailInfoType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                guardrail_info_type_0 = RegisterGuardrailRequestGuardrailInfoType0.from_dict(data)



                return guardrail_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RegisterGuardrailRequestGuardrailInfoType0 | Unset, data)

        guardrail_info = _parse_guardrail_info(d.pop("guardrail_info", UNSET))


        def _parse_team_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        team_id = _parse_team_id(d.pop("team_id", UNSET))


        register_guardrail_request = cls(
            guardrail_name=guardrail_name,
            litellm_params=litellm_params,
            guardrail_info=guardrail_info,
            team_id=team_id,
        )


        register_guardrail_request.additional_properties = d
        return register_guardrail_request

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

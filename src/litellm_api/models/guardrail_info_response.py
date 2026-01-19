from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.guardraildefinitionlocation import GUARDRAILDEFINITIONLOCATION
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.base_litellm_params import BaseLitellmParams
  from ..models.guardrail_info_response_guardrail_info_type_0 import GuardrailInfoResponseGuardrailInfoType0





T = TypeVar("T", bound="GuardrailInfoResponse")



@_attrs_define
class GuardrailInfoResponse:
    """ 
        Attributes:
            guardrail_name (str):
            guardrail_id (None | str | Unset):
            litellm_params (BaseLitellmParams | None | Unset):
            guardrail_info (GuardrailInfoResponseGuardrailInfoType0 | None | Unset):
            created_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | None | Unset):
            guardrail_definition_location (GUARDRAILDEFINITIONLOCATION | Unset):
     """

    guardrail_name: str
    guardrail_id: None | str | Unset = UNSET
    litellm_params: BaseLitellmParams | None | Unset = UNSET
    guardrail_info: GuardrailInfoResponseGuardrailInfoType0 | None | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    guardrail_definition_location: GUARDRAILDEFINITIONLOCATION | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.guardrail_info_response_guardrail_info_type_0 import GuardrailInfoResponseGuardrailInfoType0
        from ..models.base_litellm_params import BaseLitellmParams
        guardrail_name = self.guardrail_name

        guardrail_id: None | str | Unset
        if isinstance(self.guardrail_id, Unset):
            guardrail_id = UNSET
        else:
            guardrail_id = self.guardrail_id

        litellm_params: dict[str, Any] | None | Unset
        if isinstance(self.litellm_params, Unset):
            litellm_params = UNSET
        elif isinstance(self.litellm_params, BaseLitellmParams):
            litellm_params = self.litellm_params.to_dict()
        else:
            litellm_params = self.litellm_params

        guardrail_info: dict[str, Any] | None | Unset
        if isinstance(self.guardrail_info, Unset):
            guardrail_info = UNSET
        elif isinstance(self.guardrail_info, GuardrailInfoResponseGuardrailInfoType0):
            guardrail_info = self.guardrail_info.to_dict()
        else:
            guardrail_info = self.guardrail_info

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

        guardrail_definition_location: str | Unset = UNSET
        if not isinstance(self.guardrail_definition_location, Unset):
            guardrail_definition_location = self.guardrail_definition_location.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "guardrail_name": guardrail_name,
        })
        if guardrail_id is not UNSET:
            field_dict["guardrail_id"] = guardrail_id
        if litellm_params is not UNSET:
            field_dict["litellm_params"] = litellm_params
        if guardrail_info is not UNSET:
            field_dict["guardrail_info"] = guardrail_info
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if guardrail_definition_location is not UNSET:
            field_dict["guardrail_definition_location"] = guardrail_definition_location

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_litellm_params import BaseLitellmParams
        from ..models.guardrail_info_response_guardrail_info_type_0 import GuardrailInfoResponseGuardrailInfoType0
        d = dict(src_dict)
        guardrail_name = d.pop("guardrail_name")

        def _parse_guardrail_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guardrail_id = _parse_guardrail_id(d.pop("guardrail_id", UNSET))


        def _parse_litellm_params(data: object) -> BaseLitellmParams | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                litellm_params_type_0 = BaseLitellmParams.from_dict(data)



                return litellm_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BaseLitellmParams | None | Unset, data)

        litellm_params = _parse_litellm_params(d.pop("litellm_params", UNSET))


        def _parse_guardrail_info(data: object) -> GuardrailInfoResponseGuardrailInfoType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                guardrail_info_type_0 = GuardrailInfoResponseGuardrailInfoType0.from_dict(data)



                return guardrail_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GuardrailInfoResponseGuardrailInfoType0 | None | Unset, data)

        guardrail_info = _parse_guardrail_info(d.pop("guardrail_info", UNSET))


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


        _guardrail_definition_location = d.pop("guardrail_definition_location", UNSET)
        guardrail_definition_location: GUARDRAILDEFINITIONLOCATION | Unset
        if isinstance(_guardrail_definition_location,  Unset):
            guardrail_definition_location = UNSET
        else:
            guardrail_definition_location = GUARDRAILDEFINITIONLOCATION(_guardrail_definition_location)




        guardrail_info_response = cls(
            guardrail_name=guardrail_name,
            guardrail_id=guardrail_id,
            litellm_params=litellm_params,
            guardrail_info=guardrail_info,
            created_at=created_at,
            updated_at=updated_at,
            guardrail_definition_location=guardrail_definition_location,
        )


        guardrail_info_response.additional_properties = d
        return guardrail_info_response

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

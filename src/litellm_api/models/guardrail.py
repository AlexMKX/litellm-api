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
  from ..models.guardrail_guardrail_info_type_0 import GuardrailGuardrailInfoType0
  from ..models.litellm_params import LitellmParams





T = TypeVar("T", bound="Guardrail")



@_attrs_define
class Guardrail:
    """ 
        Attributes:
            guardrail_name (str):
            litellm_params (LitellmParams):
            guardrail_id (None | str | Unset):
            guardrail_info (GuardrailGuardrailInfoType0 | None | Unset):
            created_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | None | Unset):
     """

    guardrail_name: str
    litellm_params: LitellmParams
    guardrail_id: None | str | Unset = UNSET
    guardrail_info: GuardrailGuardrailInfoType0 | None | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.litellm_params import LitellmParams
        from ..models.guardrail_guardrail_info_type_0 import GuardrailGuardrailInfoType0
        guardrail_name = self.guardrail_name

        litellm_params = self.litellm_params.to_dict()

        guardrail_id: None | str | Unset
        if isinstance(self.guardrail_id, Unset):
            guardrail_id = UNSET
        else:
            guardrail_id = self.guardrail_id

        guardrail_info: dict[str, Any] | None | Unset
        if isinstance(self.guardrail_info, Unset):
            guardrail_info = UNSET
        elif isinstance(self.guardrail_info, GuardrailGuardrailInfoType0):
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


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "guardrail_name": guardrail_name,
            "litellm_params": litellm_params,
        })
        if guardrail_id is not UNSET:
            field_dict["guardrail_id"] = guardrail_id
        if guardrail_info is not UNSET:
            field_dict["guardrail_info"] = guardrail_info
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.guardrail_guardrail_info_type_0 import GuardrailGuardrailInfoType0
        from ..models.litellm_params import LitellmParams
        d = dict(src_dict)
        guardrail_name = d.pop("guardrail_name")

        litellm_params = LitellmParams.from_dict(d.pop("litellm_params"))




        def _parse_guardrail_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guardrail_id = _parse_guardrail_id(d.pop("guardrail_id", UNSET))


        def _parse_guardrail_info(data: object) -> GuardrailGuardrailInfoType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                guardrail_info_type_0 = GuardrailGuardrailInfoType0.from_dict(data)



                return guardrail_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GuardrailGuardrailInfoType0 | None | Unset, data)

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


        guardrail = cls(
            guardrail_name=guardrail_name,
            litellm_params=litellm_params,
            guardrail_id=guardrail_id,
            guardrail_info=guardrail_info,
            created_at=created_at,
            updated_at=updated_at,
        )


        guardrail.additional_properties = d
        return guardrail

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

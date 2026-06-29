from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.lite_llm_proxy_model_table_litellm_params import LiteLLMProxyModelTableLitellmParams
  from ..models.lite_llm_proxy_model_table_model_info_type_0 import LiteLLMProxyModelTableModelInfoType0





T = TypeVar("T", bound="LiteLLMProxyModelTable")



@_attrs_define
class LiteLLMProxyModelTable:
    """ 
        Attributes:
            model_id (str):
            model_name (str):
            litellm_params (LiteLLMProxyModelTableLitellmParams):
            model_info (LiteLLMProxyModelTableModelInfoType0 | None | Unset):
            blocked (bool | Unset):  Default: False.
            created_at (datetime.datetime | None | Unset):
            created_by (None | str | Unset):
            updated_at (datetime.datetime | None | Unset):
            updated_by (None | str | Unset):
     """

    model_id: str
    model_name: str
    litellm_params: LiteLLMProxyModelTableLitellmParams
    model_info: LiteLLMProxyModelTableModelInfoType0 | None | Unset = UNSET
    blocked: bool | Unset = False
    created_at: datetime.datetime | None | Unset = UNSET
    created_by: None | str | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    updated_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.lite_llm_proxy_model_table_litellm_params import LiteLLMProxyModelTableLitellmParams
        from ..models.lite_llm_proxy_model_table_model_info_type_0 import LiteLLMProxyModelTableModelInfoType0
        model_id = self.model_id

        model_name = self.model_name

        litellm_params = self.litellm_params.to_dict()

        model_info: dict[str, Any] | None | Unset
        if isinstance(self.model_info, Unset):
            model_info = UNSET
        elif isinstance(self.model_info, LiteLLMProxyModelTableModelInfoType0):
            model_info = self.model_info.to_dict()
        else:
            model_info = self.model_info

        blocked = self.blocked

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        updated_by: None | str | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = self.updated_by


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "model_id": model_id,
            "model_name": model_name,
            "litellm_params": litellm_params,
        })
        if model_info is not UNSET:
            field_dict["model_info"] = model_info
        if blocked is not UNSET:
            field_dict["blocked"] = blocked
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lite_llm_proxy_model_table_litellm_params import LiteLLMProxyModelTableLitellmParams
        from ..models.lite_llm_proxy_model_table_model_info_type_0 import LiteLLMProxyModelTableModelInfoType0
        d = dict(src_dict)
        model_id = d.pop("model_id")

        model_name = d.pop("model_name")

        litellm_params = LiteLLMProxyModelTableLitellmParams.from_dict(d.pop("litellm_params"))




        def _parse_model_info(data: object) -> LiteLLMProxyModelTableModelInfoType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_info_type_0 = LiteLLMProxyModelTableModelInfoType0.from_dict(data)



                return model_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMProxyModelTableModelInfoType0 | None | Unset, data)

        model_info = _parse_model_info(d.pop("model_info", UNSET))


        blocked = d.pop("blocked", UNSET)

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)



                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))


        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))


        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)



                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))


        def _parse_updated_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))


        lite_llm_proxy_model_table = cls(
            model_id=model_id,
            model_name=model_name,
            litellm_params=litellm_params,
            model_info=model_info,
            blocked=blocked,
            created_at=created_at,
            created_by=created_by,
            updated_at=updated_at,
            updated_by=updated_by,
        )


        lite_llm_proxy_model_table.additional_properties = d
        return lite_llm_proxy_model_table

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

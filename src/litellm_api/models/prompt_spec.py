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
  from ..models.prompt_info import PromptInfo
  from ..models.prompt_lite_llm_params import PromptLiteLLMParams





T = TypeVar("T", bound="PromptSpec")



@_attrs_define
class PromptSpec:
    """ 
        Attributes:
            prompt_id (str):
            litellm_params (PromptLiteLLMParams):
            prompt_info (PromptInfo):
            created_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | None | Unset):
            version (int | None | Unset):
     """

    prompt_id: str
    litellm_params: PromptLiteLLMParams
    prompt_info: PromptInfo
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    version: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.prompt_info import PromptInfo
        from ..models.prompt_lite_llm_params import PromptLiteLLMParams
        prompt_id = self.prompt_id

        litellm_params = self.litellm_params.to_dict()

        prompt_info = self.prompt_info.to_dict()

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

        version: int | None | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "prompt_id": prompt_id,
            "litellm_params": litellm_params,
            "prompt_info": prompt_info,
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prompt_info import PromptInfo
        from ..models.prompt_lite_llm_params import PromptLiteLLMParams
        d = dict(src_dict)
        prompt_id = d.pop("prompt_id")

        litellm_params = PromptLiteLLMParams.from_dict(d.pop("litellm_params"))




        prompt_info = PromptInfo.from_dict(d.pop("prompt_info"))




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


        def _parse_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        version = _parse_version(d.pop("version", UNSET))


        prompt_spec = cls(
            prompt_id=prompt_id,
            litellm_params=litellm_params,
            prompt_info=prompt_info,
            created_at=created_at,
            updated_at=updated_at,
            version=version,
        )


        prompt_spec.additional_properties = d
        return prompt_spec

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

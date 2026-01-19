from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.base_litellm_params import BaseLitellmParams
  from ..models.patch_guardrail_request_guardrail_info_type_0 import PatchGuardrailRequestGuardrailInfoType0





T = TypeVar("T", bound="PatchGuardrailRequest")



@_attrs_define
class PatchGuardrailRequest:
    """ 
        Attributes:
            guardrail_name (None | str | Unset):
            litellm_params (BaseLitellmParams | None | Unset):
            guardrail_info (None | PatchGuardrailRequestGuardrailInfoType0 | Unset):
     """

    guardrail_name: None | str | Unset = UNSET
    litellm_params: BaseLitellmParams | None | Unset = UNSET
    guardrail_info: None | PatchGuardrailRequestGuardrailInfoType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.patch_guardrail_request_guardrail_info_type_0 import PatchGuardrailRequestGuardrailInfoType0
        from ..models.base_litellm_params import BaseLitellmParams
        guardrail_name: None | str | Unset
        if isinstance(self.guardrail_name, Unset):
            guardrail_name = UNSET
        else:
            guardrail_name = self.guardrail_name

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
        elif isinstance(self.guardrail_info, PatchGuardrailRequestGuardrailInfoType0):
            guardrail_info = self.guardrail_info.to_dict()
        else:
            guardrail_info = self.guardrail_info


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if guardrail_name is not UNSET:
            field_dict["guardrail_name"] = guardrail_name
        if litellm_params is not UNSET:
            field_dict["litellm_params"] = litellm_params
        if guardrail_info is not UNSET:
            field_dict["guardrail_info"] = guardrail_info

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_litellm_params import BaseLitellmParams
        from ..models.patch_guardrail_request_guardrail_info_type_0 import PatchGuardrailRequestGuardrailInfoType0
        d = dict(src_dict)
        def _parse_guardrail_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guardrail_name = _parse_guardrail_name(d.pop("guardrail_name", UNSET))


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


        def _parse_guardrail_info(data: object) -> None | PatchGuardrailRequestGuardrailInfoType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                guardrail_info_type_0 = PatchGuardrailRequestGuardrailInfoType0.from_dict(data)



                return guardrail_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatchGuardrailRequestGuardrailInfoType0 | Unset, data)

        guardrail_info = _parse_guardrail_info(d.pop("guardrail_info", UNSET))


        patch_guardrail_request = cls(
            guardrail_name=guardrail_name,
            litellm_params=litellm_params,
            guardrail_info=guardrail_info,
        )


        patch_guardrail_request.additional_properties = d
        return patch_guardrail_request

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

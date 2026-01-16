from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.body_test_model_connection_health_test_connection_post_mode_type_0 import BodyTestModelConnectionHealthTestConnectionPostModeType0
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.body_test_model_connection_health_test_connection_post_litellm_params import BodyTestModelConnectionHealthTestConnectionPostLitellmParams
  from ..models.body_test_model_connection_health_test_connection_post_model_info import BodyTestModelConnectionHealthTestConnectionPostModelInfo





T = TypeVar("T", bound="BodyTestModelConnectionHealthTestConnectionPost")



@_attrs_define
class BodyTestModelConnectionHealthTestConnectionPost:
    """ 
        Attributes:
            mode (BodyTestModelConnectionHealthTestConnectionPostModeType0 | None | Unset): The mode to test the model with
                Default: BodyTestModelConnectionHealthTestConnectionPostModeType0.CHAT.
            litellm_params (BodyTestModelConnectionHealthTestConnectionPostLitellmParams | Unset): Parameters for
                litellm.completion, litellm.embedding for the health check
            model_info (BodyTestModelConnectionHealthTestConnectionPostModelInfo | Unset): Model info for the health check
     """

    mode: BodyTestModelConnectionHealthTestConnectionPostModeType0 | None | Unset = BodyTestModelConnectionHealthTestConnectionPostModeType0.CHAT
    litellm_params: BodyTestModelConnectionHealthTestConnectionPostLitellmParams | Unset = UNSET
    model_info: BodyTestModelConnectionHealthTestConnectionPostModelInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.body_test_model_connection_health_test_connection_post_litellm_params import BodyTestModelConnectionHealthTestConnectionPostLitellmParams
        from ..models.body_test_model_connection_health_test_connection_post_model_info import BodyTestModelConnectionHealthTestConnectionPostModelInfo
        mode: None | str | Unset
        if isinstance(self.mode, Unset):
            mode = UNSET
        elif isinstance(self.mode, BodyTestModelConnectionHealthTestConnectionPostModeType0):
            mode = self.mode.value
        else:
            mode = self.mode

        litellm_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.litellm_params, Unset):
            litellm_params = self.litellm_params.to_dict()

        model_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.model_info, Unset):
            model_info = self.model_info.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if mode is not UNSET:
            field_dict["mode"] = mode
        if litellm_params is not UNSET:
            field_dict["litellm_params"] = litellm_params
        if model_info is not UNSET:
            field_dict["model_info"] = model_info

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.body_test_model_connection_health_test_connection_post_litellm_params import BodyTestModelConnectionHealthTestConnectionPostLitellmParams
        from ..models.body_test_model_connection_health_test_connection_post_model_info import BodyTestModelConnectionHealthTestConnectionPostModelInfo
        d = dict(src_dict)
        def _parse_mode(data: object) -> BodyTestModelConnectionHealthTestConnectionPostModeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_0 = BodyTestModelConnectionHealthTestConnectionPostModeType0(data)



                return mode_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BodyTestModelConnectionHealthTestConnectionPostModeType0 | None | Unset, data)

        mode = _parse_mode(d.pop("mode", UNSET))


        _litellm_params = d.pop("litellm_params", UNSET)
        litellm_params: BodyTestModelConnectionHealthTestConnectionPostLitellmParams | Unset
        if isinstance(_litellm_params,  Unset):
            litellm_params = UNSET
        else:
            litellm_params = BodyTestModelConnectionHealthTestConnectionPostLitellmParams.from_dict(_litellm_params)




        _model_info = d.pop("model_info", UNSET)
        model_info: BodyTestModelConnectionHealthTestConnectionPostModelInfo | Unset
        if isinstance(_model_info,  Unset):
            model_info = UNSET
        else:
            model_info = BodyTestModelConnectionHealthTestConnectionPostModelInfo.from_dict(_model_info)




        body_test_model_connection_health_test_connection_post = cls(
            mode=mode,
            litellm_params=litellm_params,
            model_info=model_info,
        )


        body_test_model_connection_health_test_connection_post.additional_properties = d
        return body_test_model_connection_health_test_connection_post

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

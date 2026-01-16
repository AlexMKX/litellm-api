from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.prompt_spec import PromptSpec
  from ..models.prompt_template_base import PromptTemplateBase





T = TypeVar("T", bound="PromptInfoResponse")



@_attrs_define
class PromptInfoResponse:
    """ 
        Attributes:
            prompt_spec (PromptSpec):
            raw_prompt_template (None | PromptTemplateBase | Unset):
     """

    prompt_spec: PromptSpec
    raw_prompt_template: None | PromptTemplateBase | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.prompt_template_base import PromptTemplateBase
        from ..models.prompt_spec import PromptSpec
        prompt_spec = self.prompt_spec.to_dict()

        raw_prompt_template: dict[str, Any] | None | Unset
        if isinstance(self.raw_prompt_template, Unset):
            raw_prompt_template = UNSET
        elif isinstance(self.raw_prompt_template, PromptTemplateBase):
            raw_prompt_template = self.raw_prompt_template.to_dict()
        else:
            raw_prompt_template = self.raw_prompt_template


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "prompt_spec": prompt_spec,
        })
        if raw_prompt_template is not UNSET:
            field_dict["raw_prompt_template"] = raw_prompt_template

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prompt_spec import PromptSpec
        from ..models.prompt_template_base import PromptTemplateBase
        d = dict(src_dict)
        prompt_spec = PromptSpec.from_dict(d.pop("prompt_spec"))




        def _parse_raw_prompt_template(data: object) -> None | PromptTemplateBase | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                raw_prompt_template_type_0 = PromptTemplateBase.from_dict(data)



                return raw_prompt_template_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PromptTemplateBase | Unset, data)

        raw_prompt_template = _parse_raw_prompt_template(d.pop("raw_prompt_template", UNSET))


        prompt_info_response = cls(
            prompt_spec=prompt_spec,
            raw_prompt_template=raw_prompt_template,
        )


        prompt_info_response.additional_properties = d
        return prompt_info_response

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

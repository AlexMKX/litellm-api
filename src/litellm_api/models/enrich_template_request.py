from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.enrich_template_request_parameters import EnrichTemplateRequestParameters





T = TypeVar("T", bound="EnrichTemplateRequest")



@_attrs_define
class EnrichTemplateRequest:
    """ 
        Attributes:
            template_id (str):
            parameters (EnrichTemplateRequestParameters):
            model (None | str | Unset):
            competitors (list[str] | None | Unset): Optional list of competitor names
            instruction (None | str | Unset): Refinement instruction for modifying the competitor list (e.g. 'add 10 more
                from Asia')
     """

    template_id: str
    parameters: EnrichTemplateRequestParameters
    model: None | str | Unset = UNSET
    competitors: list[str] | None | Unset = UNSET
    instruction: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.enrich_template_request_parameters import EnrichTemplateRequestParameters
        template_id = self.template_id

        parameters = self.parameters.to_dict()

        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        competitors: list[str] | None | Unset
        if isinstance(self.competitors, Unset):
            competitors = UNSET
        elif isinstance(self.competitors, list):
            competitors = self.competitors


        else:
            competitors = self.competitors

        instruction: None | str | Unset
        if isinstance(self.instruction, Unset):
            instruction = UNSET
        else:
            instruction = self.instruction


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "template_id": template_id,
            "parameters": parameters,
        })
        if model is not UNSET:
            field_dict["model"] = model
        if competitors is not UNSET:
            field_dict["competitors"] = competitors
        if instruction is not UNSET:
            field_dict["instruction"] = instruction

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.enrich_template_request_parameters import EnrichTemplateRequestParameters
        d = dict(src_dict)
        template_id = d.pop("template_id")

        parameters = EnrichTemplateRequestParameters.from_dict(d.pop("parameters"))




        def _parse_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))


        def _parse_competitors(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                competitors_type_0 = cast(list[str], data)

                return competitors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        competitors = _parse_competitors(d.pop("competitors", UNSET))


        def _parse_instruction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instruction = _parse_instruction(d.pop("instruction", UNSET))


        enrich_template_request = cls(
            template_id=template_id,
            parameters=parameters,
            model=model,
            competitors=competitors,
            instruction=instruction,
        )


        enrich_template_request.additional_properties = d
        return enrich_template_request

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

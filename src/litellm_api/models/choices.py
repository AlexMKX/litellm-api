from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.choice_logprobs import ChoiceLogprobs
  from ..models.choices_provider_specific_fields_type_0 import ChoicesProviderSpecificFieldsType0
  from ..models.message import Message





T = TypeVar("T", bound="Choices")



@_attrs_define
class Choices:
    """ 
        Attributes:
            finish_reason (str):
            index (int):
            message (Message):
            logprobs (Any | ChoiceLogprobs | None | Unset):
            provider_specific_fields (ChoicesProviderSpecificFieldsType0 | None | Unset):
     """

    finish_reason: str
    index: int
    message: Message
    logprobs: Any | ChoiceLogprobs | None | Unset = UNSET
    provider_specific_fields: ChoicesProviderSpecificFieldsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.message import Message
        from ..models.choices_provider_specific_fields_type_0 import ChoicesProviderSpecificFieldsType0
        from ..models.choice_logprobs import ChoiceLogprobs
        finish_reason = self.finish_reason

        index = self.index

        message = self.message.to_dict()

        logprobs: Any | dict[str, Any] | None | Unset
        if isinstance(self.logprobs, Unset):
            logprobs = UNSET
        elif isinstance(self.logprobs, ChoiceLogprobs):
            logprobs = self.logprobs.to_dict()
        else:
            logprobs = self.logprobs

        provider_specific_fields: dict[str, Any] | None | Unset
        if isinstance(self.provider_specific_fields, Unset):
            provider_specific_fields = UNSET
        elif isinstance(self.provider_specific_fields, ChoicesProviderSpecificFieldsType0):
            provider_specific_fields = self.provider_specific_fields.to_dict()
        else:
            provider_specific_fields = self.provider_specific_fields


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "finish_reason": finish_reason,
            "index": index,
            "message": message,
        })
        if logprobs is not UNSET:
            field_dict["logprobs"] = logprobs
        if provider_specific_fields is not UNSET:
            field_dict["provider_specific_fields"] = provider_specific_fields

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.choice_logprobs import ChoiceLogprobs
        from ..models.choices_provider_specific_fields_type_0 import ChoicesProviderSpecificFieldsType0
        from ..models.message import Message
        d = dict(src_dict)
        finish_reason = d.pop("finish_reason")

        index = d.pop("index")

        message = Message.from_dict(d.pop("message"))




        def _parse_logprobs(data: object) -> Any | ChoiceLogprobs | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                logprobs_type_0 = ChoiceLogprobs.from_dict(data)



                return logprobs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Any | ChoiceLogprobs | None | Unset, data)

        logprobs = _parse_logprobs(d.pop("logprobs", UNSET))


        def _parse_provider_specific_fields(data: object) -> ChoicesProviderSpecificFieldsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_specific_fields_type_0 = ChoicesProviderSpecificFieldsType0.from_dict(data)



                return provider_specific_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChoicesProviderSpecificFieldsType0 | None | Unset, data)

        provider_specific_fields = _parse_provider_specific_fields(d.pop("provider_specific_fields", UNSET))


        choices = cls(
            finish_reason=finish_reason,
            index=index,
            message=message,
            logprobs=logprobs,
            provider_specific_fields=provider_specific_fields,
        )


        choices.additional_properties = d
        return choices

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

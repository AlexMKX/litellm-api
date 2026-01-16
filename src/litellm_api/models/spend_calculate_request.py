from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.spend_calculate_request_completion_response_type_0 import SpendCalculateRequestCompletionResponseType0





T = TypeVar("T", bound="SpendCalculateRequest")



@_attrs_define
class SpendCalculateRequest:
    """ 
        Attributes:
            model (None | str | Unset):
            messages (list[Any] | None | Unset):
            completion_response (None | SpendCalculateRequestCompletionResponseType0 | Unset):
     """

    model: None | str | Unset = UNSET
    messages: list[Any] | None | Unset = UNSET
    completion_response: None | SpendCalculateRequestCompletionResponseType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.spend_calculate_request_completion_response_type_0 import SpendCalculateRequestCompletionResponseType0
        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        messages: list[Any] | None | Unset
        if isinstance(self.messages, Unset):
            messages = UNSET
        elif isinstance(self.messages, list):
            messages = self.messages


        else:
            messages = self.messages

        completion_response: dict[str, Any] | None | Unset
        if isinstance(self.completion_response, Unset):
            completion_response = UNSET
        elif isinstance(self.completion_response, SpendCalculateRequestCompletionResponseType0):
            completion_response = self.completion_response.to_dict()
        else:
            completion_response = self.completion_response


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if model is not UNSET:
            field_dict["model"] = model
        if messages is not UNSET:
            field_dict["messages"] = messages
        if completion_response is not UNSET:
            field_dict["completion_response"] = completion_response

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spend_calculate_request_completion_response_type_0 import SpendCalculateRequestCompletionResponseType0
        d = dict(src_dict)
        def _parse_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))


        def _parse_messages(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                messages_type_0 = cast(list[Any], data)

                return messages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        messages = _parse_messages(d.pop("messages", UNSET))


        def _parse_completion_response(data: object) -> None | SpendCalculateRequestCompletionResponseType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                completion_response_type_0 = SpendCalculateRequestCompletionResponseType0.from_dict(data)



                return completion_response_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SpendCalculateRequestCompletionResponseType0 | Unset, data)

        completion_response = _parse_completion_response(d.pop("completion_response", UNSET))


        spend_calculate_request = cls(
            model=model,
            messages=messages,
            completion_response=completion_response,
        )


        spend_calculate_request.additional_properties = d
        return spend_calculate_request

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

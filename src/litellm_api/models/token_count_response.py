from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.token_count_response_original_response_type_0 import TokenCountResponseOriginalResponseType0





T = TypeVar("T", bound="TokenCountResponse")



@_attrs_define
class TokenCountResponse:
    """ 
        Attributes:
            total_tokens (int):
            request_model (str):
            model_used (str):
            tokenizer_type (str):
            original_response (None | TokenCountResponseOriginalResponseType0 | Unset):
     """

    total_tokens: int
    request_model: str
    model_used: str
    tokenizer_type: str
    original_response: None | TokenCountResponseOriginalResponseType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.token_count_response_original_response_type_0 import TokenCountResponseOriginalResponseType0
        total_tokens = self.total_tokens

        request_model = self.request_model

        model_used = self.model_used

        tokenizer_type = self.tokenizer_type

        original_response: dict[str, Any] | None | Unset
        if isinstance(self.original_response, Unset):
            original_response = UNSET
        elif isinstance(self.original_response, TokenCountResponseOriginalResponseType0):
            original_response = self.original_response.to_dict()
        else:
            original_response = self.original_response


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "total_tokens": total_tokens,
            "request_model": request_model,
            "model_used": model_used,
            "tokenizer_type": tokenizer_type,
        })
        if original_response is not UNSET:
            field_dict["original_response"] = original_response

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.token_count_response_original_response_type_0 import TokenCountResponseOriginalResponseType0
        d = dict(src_dict)
        total_tokens = d.pop("total_tokens")

        request_model = d.pop("request_model")

        model_used = d.pop("model_used")

        tokenizer_type = d.pop("tokenizer_type")

        def _parse_original_response(data: object) -> None | TokenCountResponseOriginalResponseType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                original_response_type_0 = TokenCountResponseOriginalResponseType0.from_dict(data)



                return original_response_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TokenCountResponseOriginalResponseType0 | Unset, data)

        original_response = _parse_original_response(d.pop("original_response", UNSET))


        token_count_response = cls(
            total_tokens=total_tokens,
            request_model=request_model,
            model_used=model_used,
            tokenizer_type=tokenizer_type,
            original_response=original_response,
        )


        token_count_response.additional_properties = d
        return token_count_response

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

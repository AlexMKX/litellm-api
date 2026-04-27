from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.pii_entity_type import PiiEntityType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.apply_guardrail_request_messages_type_0_item import ApplyGuardrailRequestMessagesType0Item





T = TypeVar("T", bound="ApplyGuardrailRequest")



@_attrs_define
class ApplyGuardrailRequest:
    """ 
        Attributes:
            guardrail_name (str):
            text (str):
            language (None | str | Unset):
            entities (list[PiiEntityType] | None | Unset):
            input_type (str | Unset):  Default: 'request'.
            messages (list[ApplyGuardrailRequestMessagesType0Item] | None | Unset):
     """

    guardrail_name: str
    text: str
    language: None | str | Unset = UNSET
    entities: list[PiiEntityType] | None | Unset = UNSET
    input_type: str | Unset = 'request'
    messages: list[ApplyGuardrailRequestMessagesType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.apply_guardrail_request_messages_type_0_item import ApplyGuardrailRequestMessagesType0Item
        guardrail_name = self.guardrail_name

        text = self.text

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        entities: list[str] | None | Unset
        if isinstance(self.entities, Unset):
            entities = UNSET
        elif isinstance(self.entities, list):
            entities = []
            for entities_type_0_item_data in self.entities:
                entities_type_0_item = entities_type_0_item_data.value
                entities.append(entities_type_0_item)


        else:
            entities = self.entities

        input_type = self.input_type

        messages: list[dict[str, Any]] | None | Unset
        if isinstance(self.messages, Unset):
            messages = UNSET
        elif isinstance(self.messages, list):
            messages = []
            for messages_type_0_item_data in self.messages:
                messages_type_0_item = messages_type_0_item_data.to_dict()
                messages.append(messages_type_0_item)


        else:
            messages = self.messages


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "guardrail_name": guardrail_name,
            "text": text,
        })
        if language is not UNSET:
            field_dict["language"] = language
        if entities is not UNSET:
            field_dict["entities"] = entities
        if input_type is not UNSET:
            field_dict["input_type"] = input_type
        if messages is not UNSET:
            field_dict["messages"] = messages

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.apply_guardrail_request_messages_type_0_item import ApplyGuardrailRequestMessagesType0Item
        d = dict(src_dict)
        guardrail_name = d.pop("guardrail_name")

        text = d.pop("text")

        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("language", UNSET))


        def _parse_entities(data: object) -> list[PiiEntityType] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                entities_type_0 = []
                _entities_type_0 = data
                for entities_type_0_item_data in (_entities_type_0):
                    entities_type_0_item = PiiEntityType(entities_type_0_item_data)



                    entities_type_0.append(entities_type_0_item)

                return entities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PiiEntityType] | None | Unset, data)

        entities = _parse_entities(d.pop("entities", UNSET))


        input_type = d.pop("input_type", UNSET)

        def _parse_messages(data: object) -> list[ApplyGuardrailRequestMessagesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                messages_type_0 = []
                _messages_type_0 = data
                for messages_type_0_item_data in (_messages_type_0):
                    messages_type_0_item = ApplyGuardrailRequestMessagesType0Item.from_dict(messages_type_0_item_data)



                    messages_type_0.append(messages_type_0_item)

                return messages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ApplyGuardrailRequestMessagesType0Item] | None | Unset, data)

        messages = _parse_messages(d.pop("messages", UNSET))


        apply_guardrail_request = cls(
            guardrail_name=guardrail_name,
            text=text,
            language=language,
            entities=entities,
            input_type=input_type,
            messages=messages,
        )


        apply_guardrail_request.additional_properties = d
        return apply_guardrail_request

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

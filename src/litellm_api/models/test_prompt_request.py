from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.test_prompt_request_conversation_history_type_0_item import TestPromptRequestConversationHistoryType0Item
  from ..models.test_prompt_request_prompt_variables_type_0 import TestPromptRequestPromptVariablesType0





T = TypeVar("T", bound="TestPromptRequest")



@_attrs_define
class TestPromptRequest:
    """ 
        Attributes:
            dotprompt_content (str):
            prompt_variables (None | TestPromptRequestPromptVariablesType0 | Unset):
            conversation_history (list[TestPromptRequestConversationHistoryType0Item] | None | Unset):
     """

    dotprompt_content: str
    prompt_variables: None | TestPromptRequestPromptVariablesType0 | Unset = UNSET
    conversation_history: list[TestPromptRequestConversationHistoryType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.test_prompt_request_conversation_history_type_0_item import TestPromptRequestConversationHistoryType0Item
        from ..models.test_prompt_request_prompt_variables_type_0 import TestPromptRequestPromptVariablesType0
        dotprompt_content = self.dotprompt_content

        prompt_variables: dict[str, Any] | None | Unset
        if isinstance(self.prompt_variables, Unset):
            prompt_variables = UNSET
        elif isinstance(self.prompt_variables, TestPromptRequestPromptVariablesType0):
            prompt_variables = self.prompt_variables.to_dict()
        else:
            prompt_variables = self.prompt_variables

        conversation_history: list[dict[str, Any]] | None | Unset
        if isinstance(self.conversation_history, Unset):
            conversation_history = UNSET
        elif isinstance(self.conversation_history, list):
            conversation_history = []
            for conversation_history_type_0_item_data in self.conversation_history:
                conversation_history_type_0_item = conversation_history_type_0_item_data.to_dict()
                conversation_history.append(conversation_history_type_0_item)


        else:
            conversation_history = self.conversation_history


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "dotprompt_content": dotprompt_content,
        })
        if prompt_variables is not UNSET:
            field_dict["prompt_variables"] = prompt_variables
        if conversation_history is not UNSET:
            field_dict["conversation_history"] = conversation_history

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_prompt_request_conversation_history_type_0_item import TestPromptRequestConversationHistoryType0Item
        from ..models.test_prompt_request_prompt_variables_type_0 import TestPromptRequestPromptVariablesType0
        d = dict(src_dict)
        dotprompt_content = d.pop("dotprompt_content")

        def _parse_prompt_variables(data: object) -> None | TestPromptRequestPromptVariablesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                prompt_variables_type_0 = TestPromptRequestPromptVariablesType0.from_dict(data)



                return prompt_variables_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TestPromptRequestPromptVariablesType0 | Unset, data)

        prompt_variables = _parse_prompt_variables(d.pop("prompt_variables", UNSET))


        def _parse_conversation_history(data: object) -> list[TestPromptRequestConversationHistoryType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                conversation_history_type_0 = []
                _conversation_history_type_0 = data
                for conversation_history_type_0_item_data in (_conversation_history_type_0):
                    conversation_history_type_0_item = TestPromptRequestConversationHistoryType0Item.from_dict(conversation_history_type_0_item_data)



                    conversation_history_type_0.append(conversation_history_type_0_item)

                return conversation_history_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TestPromptRequestConversationHistoryType0Item] | None | Unset, data)

        conversation_history = _parse_conversation_history(d.pop("conversation_history", UNSET))


        test_prompt_request = cls(
            dotprompt_content=dotprompt_content,
            prompt_variables=prompt_variables,
            conversation_history=conversation_history,
        )


        test_prompt_request.additional_properties = d
        return test_prompt_request

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

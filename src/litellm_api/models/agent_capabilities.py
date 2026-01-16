from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.agent_extension import AgentExtension





T = TypeVar("T", bound="AgentCapabilities")



@_attrs_define
class AgentCapabilities:
    """ Defines optional capabilities supported by an agent.

        Attributes:
            streaming (bool | None | Unset):
            push_notifications (bool | None | Unset):
            state_transition_history (bool | None | Unset):
            extensions (list[AgentExtension] | None | Unset):
     """

    streaming: bool | None | Unset = UNSET
    push_notifications: bool | None | Unset = UNSET
    state_transition_history: bool | None | Unset = UNSET
    extensions: list[AgentExtension] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_extension import AgentExtension
        streaming: bool | None | Unset
        if isinstance(self.streaming, Unset):
            streaming = UNSET
        else:
            streaming = self.streaming

        push_notifications: bool | None | Unset
        if isinstance(self.push_notifications, Unset):
            push_notifications = UNSET
        else:
            push_notifications = self.push_notifications

        state_transition_history: bool | None | Unset
        if isinstance(self.state_transition_history, Unset):
            state_transition_history = UNSET
        else:
            state_transition_history = self.state_transition_history

        extensions: list[dict[str, Any]] | None | Unset
        if isinstance(self.extensions, Unset):
            extensions = UNSET
        elif isinstance(self.extensions, list):
            extensions = []
            for extensions_type_0_item_data in self.extensions:
                extensions_type_0_item = extensions_type_0_item_data.to_dict()
                extensions.append(extensions_type_0_item)


        else:
            extensions = self.extensions


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if streaming is not UNSET:
            field_dict["streaming"] = streaming
        if push_notifications is not UNSET:
            field_dict["pushNotifications"] = push_notifications
        if state_transition_history is not UNSET:
            field_dict["stateTransitionHistory"] = state_transition_history
        if extensions is not UNSET:
            field_dict["extensions"] = extensions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_extension import AgentExtension
        d = dict(src_dict)
        def _parse_streaming(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        streaming = _parse_streaming(d.pop("streaming", UNSET))


        def _parse_push_notifications(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        push_notifications = _parse_push_notifications(d.pop("pushNotifications", UNSET))


        def _parse_state_transition_history(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        state_transition_history = _parse_state_transition_history(d.pop("stateTransitionHistory", UNSET))


        def _parse_extensions(data: object) -> list[AgentExtension] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                extensions_type_0 = []
                _extensions_type_0 = data
                for extensions_type_0_item_data in (_extensions_type_0):
                    extensions_type_0_item = AgentExtension.from_dict(extensions_type_0_item_data)



                    extensions_type_0.append(extensions_type_0_item)

                return extensions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AgentExtension] | None | Unset, data)

        extensions = _parse_extensions(d.pop("extensions", UNSET))


        agent_capabilities = cls(
            streaming=streaming,
            push_notifications=push_notifications,
            state_transition_history=state_transition_history,
            extensions=extensions,
        )


        agent_capabilities.additional_properties = d
        return agent_capabilities

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

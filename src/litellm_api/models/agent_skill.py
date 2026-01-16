from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.agent_skill_security_type_0_item import AgentSkillSecurityType0Item





T = TypeVar("T", bound="AgentSkill")



@_attrs_define
class AgentSkill:
    """ Represents a distinct capability or function that an agent can perform.

        Attributes:
            id (str | Unset):
            name (str | Unset):
            description (str | Unset):
            tags (list[str] | Unset):
            examples (list[str] | None | Unset):
            input_modes (list[str] | None | Unset):
            output_modes (list[str] | None | Unset):
            security (list[AgentSkillSecurityType0Item] | None | Unset):
     """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    examples: list[str] | None | Unset = UNSET
    input_modes: list[str] | None | Unset = UNSET
    output_modes: list[str] | None | Unset = UNSET
    security: list[AgentSkillSecurityType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_skill_security_type_0_item import AgentSkillSecurityType0Item
        id = self.id

        name = self.name

        description = self.description

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags



        examples: list[str] | None | Unset
        if isinstance(self.examples, Unset):
            examples = UNSET
        elif isinstance(self.examples, list):
            examples = self.examples


        else:
            examples = self.examples

        input_modes: list[str] | None | Unset
        if isinstance(self.input_modes, Unset):
            input_modes = UNSET
        elif isinstance(self.input_modes, list):
            input_modes = self.input_modes


        else:
            input_modes = self.input_modes

        output_modes: list[str] | None | Unset
        if isinstance(self.output_modes, Unset):
            output_modes = UNSET
        elif isinstance(self.output_modes, list):
            output_modes = self.output_modes


        else:
            output_modes = self.output_modes

        security: list[dict[str, Any]] | None | Unset
        if isinstance(self.security, Unset):
            security = UNSET
        elif isinstance(self.security, list):
            security = []
            for security_type_0_item_data in self.security:
                security_type_0_item = security_type_0_item_data.to_dict()
                security.append(security_type_0_item)


        else:
            security = self.security


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if examples is not UNSET:
            field_dict["examples"] = examples
        if input_modes is not UNSET:
            field_dict["inputModes"] = input_modes
        if output_modes is not UNSET:
            field_dict["outputModes"] = output_modes
        if security is not UNSET:
            field_dict["security"] = security

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_skill_security_type_0_item import AgentSkillSecurityType0Item
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))


        def _parse_examples(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                examples_type_0 = cast(list[str], data)

                return examples_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        examples = _parse_examples(d.pop("examples", UNSET))


        def _parse_input_modes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                input_modes_type_0 = cast(list[str], data)

                return input_modes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        input_modes = _parse_input_modes(d.pop("inputModes", UNSET))


        def _parse_output_modes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                output_modes_type_0 = cast(list[str], data)

                return output_modes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        output_modes = _parse_output_modes(d.pop("outputModes", UNSET))


        def _parse_security(data: object) -> list[AgentSkillSecurityType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                security_type_0 = []
                _security_type_0 = data
                for security_type_0_item_data in (_security_type_0):
                    security_type_0_item = AgentSkillSecurityType0Item.from_dict(security_type_0_item_data)



                    security_type_0.append(security_type_0_item)

                return security_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AgentSkillSecurityType0Item] | None | Unset, data)

        security = _parse_security(d.pop("security", UNSET))


        agent_skill = cls(
            id=id,
            name=name,
            description=description,
            tags=tags,
            examples=examples,
            input_modes=input_modes,
            output_modes=output_modes,
            security=security,
        )


        agent_skill.additional_properties = d
        return agent_skill

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

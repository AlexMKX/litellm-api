from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="AgentMakePublicResponse")



@_attrs_define
class AgentMakePublicResponse:
    """ 
        Attributes:
            message (str):
            public_agent_groups (list[str]):
            updated_by (str):
     """

    message: str
    public_agent_groups: list[str]
    updated_by: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        message = self.message

        public_agent_groups = self.public_agent_groups



        updated_by = self.updated_by


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "message": message,
            "public_agent_groups": public_agent_groups,
            "updated_by": updated_by,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        public_agent_groups = cast(list[str], d.pop("public_agent_groups"))


        updated_by = d.pop("updated_by")

        agent_make_public_response = cls(
            message=message,
            public_agent_groups=public_agent_groups,
            updated_by=updated_by,
        )


        agent_make_public_response.additional_properties = d
        return agent_make_public_response

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

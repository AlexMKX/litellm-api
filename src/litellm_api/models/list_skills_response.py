from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.skill import Skill





T = TypeVar("T", bound="ListSkillsResponse")



@_attrs_define
class ListSkillsResponse:
    """ Response from listing skills

        Attributes:
            data (list[Skill]):
            next_page (None | str | Unset):
            has_more (bool | Unset):  Default: False.
     """

    data: list[Skill]
    next_page: None | str | Unset = UNSET
    has_more: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.skill import Skill
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)



        next_page: None | str | Unset
        if isinstance(self.next_page, Unset):
            next_page = UNSET
        else:
            next_page = self.next_page

        has_more = self.has_more


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "data": data,
        })
        if next_page is not UNSET:
            field_dict["next_page"] = next_page
        if has_more is not UNSET:
            field_dict["has_more"] = has_more

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.skill import Skill
        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            data_item = Skill.from_dict(data_item_data)



            data.append(data_item)


        def _parse_next_page(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page = _parse_next_page(d.pop("next_page", UNSET))


        has_more = d.pop("has_more", UNSET)

        list_skills_response = cls(
            data=data,
            next_page=next_page,
            has_more=has_more,
        )


        list_skills_response.additional_properties = d
        return list_skills_response

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

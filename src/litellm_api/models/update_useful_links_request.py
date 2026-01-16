from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.update_useful_links_request_useful_links import UpdateUsefulLinksRequestUsefulLinks





T = TypeVar("T", bound="UpdateUsefulLinksRequest")



@_attrs_define
class UpdateUsefulLinksRequest:
    """ 
        Attributes:
            useful_links (UpdateUsefulLinksRequestUsefulLinks):
     """

    useful_links: UpdateUsefulLinksRequestUsefulLinks
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_useful_links_request_useful_links import UpdateUsefulLinksRequestUsefulLinks
        useful_links = self.useful_links.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "useful_links": useful_links,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_useful_links_request_useful_links import UpdateUsefulLinksRequestUsefulLinks
        d = dict(src_dict)
        useful_links = UpdateUsefulLinksRequestUsefulLinks.from_dict(d.pop("useful_links"))




        update_useful_links_request = cls(
            useful_links=useful_links,
        )


        update_useful_links_request.additional_properties = d
        return update_useful_links_request

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

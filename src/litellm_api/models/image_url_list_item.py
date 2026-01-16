from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.image_url_object import ImageURLObject





T = TypeVar("T", bound="ImageURLListItem")



@_attrs_define
class ImageURLListItem:
    """ 
        Attributes:
            image_url (ImageURLObject):
            index (int):
            type_ (Literal['image_url']):
     """

    image_url: ImageURLObject
    index: int
    type_: Literal['image_url']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.image_url_object import ImageURLObject
        image_url = self.image_url.to_dict()

        index = self.index

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "image_url": image_url,
            "index": index,
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_url_object import ImageURLObject
        d = dict(src_dict)
        image_url = ImageURLObject.from_dict(d.pop("image_url"))




        index = d.pop("index")

        type_ = cast(Literal['image_url'] , d.pop("type"))
        if type_ != 'image_url':
            raise ValueError(f"type must match const 'image_url', got '{type_}'")

        image_url_list_item = cls(
            image_url=image_url,
            index=index,
            type_=type_,
        )


        image_url_list_item.additional_properties = d
        return image_url_list_item

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

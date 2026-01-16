from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.user_api_key_auth import UserAPIKeyAuth





T = TypeVar("T", bound="KeyListResponseObject")



@_attrs_define
class KeyListResponseObject:
    """ 
        Attributes:
            keys (list[str | UserAPIKeyAuth] | Unset):
            total_count (int | None | Unset):
            current_page (int | None | Unset):
            total_pages (int | None | Unset):
     """

    keys: list[str | UserAPIKeyAuth] | Unset = UNSET
    total_count: int | None | Unset = UNSET
    current_page: int | None | Unset = UNSET
    total_pages: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.user_api_key_auth import UserAPIKeyAuth
        keys: list[dict[str, Any] | str] | Unset = UNSET
        if not isinstance(self.keys, Unset):
            keys = []
            for keys_item_data in self.keys:
                keys_item: dict[str, Any] | str
                if isinstance(keys_item_data, UserAPIKeyAuth):
                    keys_item = keys_item_data.to_dict()
                else:
                    keys_item = keys_item_data
                keys.append(keys_item)



        total_count: int | None | Unset
        if isinstance(self.total_count, Unset):
            total_count = UNSET
        else:
            total_count = self.total_count

        current_page: int | None | Unset
        if isinstance(self.current_page, Unset):
            current_page = UNSET
        else:
            current_page = self.current_page

        total_pages: int | None | Unset
        if isinstance(self.total_pages, Unset):
            total_pages = UNSET
        else:
            total_pages = self.total_pages


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if keys is not UNSET:
            field_dict["keys"] = keys
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if current_page is not UNSET:
            field_dict["current_page"] = current_page
        if total_pages is not UNSET:
            field_dict["total_pages"] = total_pages

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_api_key_auth import UserAPIKeyAuth
        d = dict(src_dict)
        _keys = d.pop("keys", UNSET)
        keys: list[str | UserAPIKeyAuth] | Unset = UNSET
        if _keys is not UNSET:
            keys = []
            for keys_item_data in _keys:
                def _parse_keys_item(data: object) -> str | UserAPIKeyAuth:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        keys_item_type_1 = UserAPIKeyAuth.from_dict(data)



                        return keys_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(str | UserAPIKeyAuth, data)

                keys_item = _parse_keys_item(keys_item_data)

                keys.append(keys_item)


        def _parse_total_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_count = _parse_total_count(d.pop("total_count", UNSET))


        def _parse_current_page(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        current_page = _parse_current_page(d.pop("current_page", UNSET))


        def _parse_total_pages(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_pages = _parse_total_pages(d.pop("total_pages", UNSET))


        key_list_response_object = cls(
            keys=keys,
            total_count=total_count,
            current_page=current_page,
            total_pages=total_pages,
        )


        key_list_response_object.additional_properties = d
        return key_list_response_object

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

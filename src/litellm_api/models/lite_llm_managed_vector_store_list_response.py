from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.lite_llm_managed_vector_store import LiteLLMManagedVectorStore





T = TypeVar("T", bound="LiteLLMManagedVectorStoreListResponse")



@_attrs_define
class LiteLLMManagedVectorStoreListResponse:
    """ Response format for listing vector stores

        Attributes:
            current_page (int | None | Unset):
            data (list[LiteLLMManagedVectorStore] | Unset):
            object_ (Literal['list'] | Unset):
            total_count (int | None | Unset):
            total_pages (int | None | Unset):
     """

    current_page: int | None | Unset = UNSET
    data: list[LiteLLMManagedVectorStore] | Unset = UNSET
    object_: Literal['list'] | Unset = UNSET
    total_count: int | None | Unset = UNSET
    total_pages: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.lite_llm_managed_vector_store import LiteLLMManagedVectorStore
        current_page: int | None | Unset
        if isinstance(self.current_page, Unset):
            current_page = UNSET
        else:
            current_page = self.current_page

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)



        object_ = self.object_

        total_count: int | None | Unset
        if isinstance(self.total_count, Unset):
            total_count = UNSET
        else:
            total_count = self.total_count

        total_pages: int | None | Unset
        if isinstance(self.total_pages, Unset):
            total_pages = UNSET
        else:
            total_pages = self.total_pages


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if current_page is not UNSET:
            field_dict["current_page"] = current_page
        if data is not UNSET:
            field_dict["data"] = data
        if object_ is not UNSET:
            field_dict["object"] = object_
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if total_pages is not UNSET:
            field_dict["total_pages"] = total_pages

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lite_llm_managed_vector_store import LiteLLMManagedVectorStore
        d = dict(src_dict)
        def _parse_current_page(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        current_page = _parse_current_page(d.pop("current_page", UNSET))


        _data = d.pop("data", UNSET)
        data: list[LiteLLMManagedVectorStore] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = LiteLLMManagedVectorStore.from_dict(data_item_data)



                data.append(data_item)


        object_ = cast(Literal['list'] | Unset , d.pop("object", UNSET))
        if object_ != 'list'and not isinstance(object_, Unset):
            raise ValueError(f"object must match const 'list', got '{object_}'")

        def _parse_total_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_count = _parse_total_count(d.pop("total_count", UNSET))


        def _parse_total_pages(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_pages = _parse_total_pages(d.pop("total_pages", UNSET))


        lite_llm_managed_vector_store_list_response = cls(
            current_page=current_page,
            data=data,
            object_=object_,
            total_count=total_count,
            total_pages=total_pages,
        )


        lite_llm_managed_vector_store_list_response.additional_properties = d
        return lite_llm_managed_vector_store_list_response

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

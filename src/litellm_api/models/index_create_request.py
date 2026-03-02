from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.index_create_lite_llm_params import IndexCreateLiteLLMParams
  from ..models.index_create_request_index_info_type_0 import IndexCreateRequestIndexInfoType0





T = TypeVar("T", bound="IndexCreateRequest")



@_attrs_define
class IndexCreateRequest:
    """ 
        Attributes:
            index_name (str):
            litellm_params (IndexCreateLiteLLMParams):
            index_info (IndexCreateRequestIndexInfoType0 | None | Unset):
     """

    index_name: str
    litellm_params: IndexCreateLiteLLMParams
    index_info: IndexCreateRequestIndexInfoType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.index_create_lite_llm_params import IndexCreateLiteLLMParams
        from ..models.index_create_request_index_info_type_0 import IndexCreateRequestIndexInfoType0
        index_name = self.index_name

        litellm_params = self.litellm_params.to_dict()

        index_info: dict[str, Any] | None | Unset
        if isinstance(self.index_info, Unset):
            index_info = UNSET
        elif isinstance(self.index_info, IndexCreateRequestIndexInfoType0):
            index_info = self.index_info.to_dict()
        else:
            index_info = self.index_info


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "index_name": index_name,
            "litellm_params": litellm_params,
        })
        if index_info is not UNSET:
            field_dict["index_info"] = index_info

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.index_create_lite_llm_params import IndexCreateLiteLLMParams
        from ..models.index_create_request_index_info_type_0 import IndexCreateRequestIndexInfoType0
        d = dict(src_dict)
        index_name = d.pop("index_name")

        litellm_params = IndexCreateLiteLLMParams.from_dict(d.pop("litellm_params"))




        def _parse_index_info(data: object) -> IndexCreateRequestIndexInfoType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                index_info_type_0 = IndexCreateRequestIndexInfoType0.from_dict(data)



                return index_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IndexCreateRequestIndexInfoType0 | None | Unset, data)

        index_info = _parse_index_info(d.pop("index_info", UNSET))


        index_create_request = cls(
            index_name=index_name,
            litellm_params=litellm_params,
            index_info=index_info,
        )


        index_create_request.additional_properties = d
        return index_create_request

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

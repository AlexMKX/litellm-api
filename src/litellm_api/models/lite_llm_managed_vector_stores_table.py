from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.lite_llm_managed_vector_stores_table_litellm_params_type_0 import LiteLLMManagedVectorStoresTableLitellmParamsType0
  from ..models.lite_llm_managed_vector_stores_table_vector_store_metadata_type_0 import LiteLLMManagedVectorStoresTableVectorStoreMetadataType0





T = TypeVar("T", bound="LiteLLMManagedVectorStoresTable")



@_attrs_define
class LiteLLMManagedVectorStoresTable:
    """ 
        Attributes:
            vector_store_id (str):
            custom_llm_provider (str):
            vector_store_name (None | str):
            vector_store_description (None | str):
            vector_store_metadata (LiteLLMManagedVectorStoresTableVectorStoreMetadataType0 | None):
            created_at (datetime.datetime | None):
            updated_at (datetime.datetime | None):
            litellm_credential_name (None | str):
            litellm_params (LiteLLMManagedVectorStoresTableLitellmParamsType0 | None):
     """

    vector_store_id: str
    custom_llm_provider: str
    vector_store_name: None | str
    vector_store_description: None | str
    vector_store_metadata: LiteLLMManagedVectorStoresTableVectorStoreMetadataType0 | None
    created_at: datetime.datetime | None
    updated_at: datetime.datetime | None
    litellm_credential_name: None | str
    litellm_params: LiteLLMManagedVectorStoresTableLitellmParamsType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.lite_llm_managed_vector_stores_table_vector_store_metadata_type_0 import LiteLLMManagedVectorStoresTableVectorStoreMetadataType0
        from ..models.lite_llm_managed_vector_stores_table_litellm_params_type_0 import LiteLLMManagedVectorStoresTableLitellmParamsType0
        vector_store_id = self.vector_store_id

        custom_llm_provider = self.custom_llm_provider

        vector_store_name: None | str
        vector_store_name = self.vector_store_name

        vector_store_description: None | str
        vector_store_description = self.vector_store_description

        vector_store_metadata: dict[str, Any] | None
        if isinstance(self.vector_store_metadata, LiteLLMManagedVectorStoresTableVectorStoreMetadataType0):
            vector_store_metadata = self.vector_store_metadata.to_dict()
        else:
            vector_store_metadata = self.vector_store_metadata

        created_at: None | str
        if isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str
        if isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        litellm_credential_name: None | str
        litellm_credential_name = self.litellm_credential_name

        litellm_params: dict[str, Any] | None
        if isinstance(self.litellm_params, LiteLLMManagedVectorStoresTableLitellmParamsType0):
            litellm_params = self.litellm_params.to_dict()
        else:
            litellm_params = self.litellm_params


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "vector_store_id": vector_store_id,
            "custom_llm_provider": custom_llm_provider,
            "vector_store_name": vector_store_name,
            "vector_store_description": vector_store_description,
            "vector_store_metadata": vector_store_metadata,
            "created_at": created_at,
            "updated_at": updated_at,
            "litellm_credential_name": litellm_credential_name,
            "litellm_params": litellm_params,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lite_llm_managed_vector_stores_table_litellm_params_type_0 import LiteLLMManagedVectorStoresTableLitellmParamsType0
        from ..models.lite_llm_managed_vector_stores_table_vector_store_metadata_type_0 import LiteLLMManagedVectorStoresTableVectorStoreMetadataType0
        d = dict(src_dict)
        vector_store_id = d.pop("vector_store_id")

        custom_llm_provider = d.pop("custom_llm_provider")

        def _parse_vector_store_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        vector_store_name = _parse_vector_store_name(d.pop("vector_store_name"))


        def _parse_vector_store_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        vector_store_description = _parse_vector_store_description(d.pop("vector_store_description"))


        def _parse_vector_store_metadata(data: object) -> LiteLLMManagedVectorStoresTableVectorStoreMetadataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vector_store_metadata_type_0 = LiteLLMManagedVectorStoresTableVectorStoreMetadataType0.from_dict(data)



                return vector_store_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMManagedVectorStoresTableVectorStoreMetadataType0 | None, data)

        vector_store_metadata = _parse_vector_store_metadata(d.pop("vector_store_metadata"))


        def _parse_created_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)



                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        created_at = _parse_created_at(d.pop("created_at"))


        def _parse_updated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)



                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        updated_at = _parse_updated_at(d.pop("updated_at"))


        def _parse_litellm_credential_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        litellm_credential_name = _parse_litellm_credential_name(d.pop("litellm_credential_name"))


        def _parse_litellm_params(data: object) -> LiteLLMManagedVectorStoresTableLitellmParamsType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                litellm_params_type_0 = LiteLLMManagedVectorStoresTableLitellmParamsType0.from_dict(data)



                return litellm_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMManagedVectorStoresTableLitellmParamsType0 | None, data)

        litellm_params = _parse_litellm_params(d.pop("litellm_params"))


        lite_llm_managed_vector_stores_table = cls(
            vector_store_id=vector_store_id,
            custom_llm_provider=custom_llm_provider,
            vector_store_name=vector_store_name,
            vector_store_description=vector_store_description,
            vector_store_metadata=vector_store_metadata,
            created_at=created_at,
            updated_at=updated_at,
            litellm_credential_name=litellm_credential_name,
            litellm_params=litellm_params,
        )


        lite_llm_managed_vector_stores_table.additional_properties = d
        return lite_llm_managed_vector_stores_table

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

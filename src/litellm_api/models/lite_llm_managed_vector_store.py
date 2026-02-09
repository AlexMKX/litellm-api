from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.lite_llm_managed_vector_store_litellm_params_type_0 import LiteLLMManagedVectorStoreLitellmParamsType0
  from ..models.lite_llm_managed_vector_store_vector_store_metadata_type_0 import LiteLLMManagedVectorStoreVectorStoreMetadataType0





T = TypeVar("T", bound="LiteLLMManagedVectorStore")



@_attrs_define
class LiteLLMManagedVectorStore:
    """ LiteLLM managed vector store object - this is is the object stored in the database

        Attributes:
            vector_store_id (str | Unset):
            custom_llm_provider (str | Unset):
            vector_store_name (None | str | Unset):
            vector_store_description (None | str | Unset):
            vector_store_metadata (LiteLLMManagedVectorStoreVectorStoreMetadataType0 | None | str | Unset):
            created_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | None | Unset):
            litellm_credential_name (None | str | Unset):
            litellm_params (LiteLLMManagedVectorStoreLitellmParamsType0 | None | Unset):
            team_id (None | str | Unset):
            user_id (None | str | Unset):
     """

    vector_store_id: str | Unset = UNSET
    custom_llm_provider: str | Unset = UNSET
    vector_store_name: None | str | Unset = UNSET
    vector_store_description: None | str | Unset = UNSET
    vector_store_metadata: LiteLLMManagedVectorStoreVectorStoreMetadataType0 | None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    litellm_credential_name: None | str | Unset = UNSET
    litellm_params: LiteLLMManagedVectorStoreLitellmParamsType0 | None | Unset = UNSET
    team_id: None | str | Unset = UNSET
    user_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.lite_llm_managed_vector_store_litellm_params_type_0 import LiteLLMManagedVectorStoreLitellmParamsType0
        from ..models.lite_llm_managed_vector_store_vector_store_metadata_type_0 import LiteLLMManagedVectorStoreVectorStoreMetadataType0
        vector_store_id = self.vector_store_id

        custom_llm_provider = self.custom_llm_provider

        vector_store_name: None | str | Unset
        if isinstance(self.vector_store_name, Unset):
            vector_store_name = UNSET
        else:
            vector_store_name = self.vector_store_name

        vector_store_description: None | str | Unset
        if isinstance(self.vector_store_description, Unset):
            vector_store_description = UNSET
        else:
            vector_store_description = self.vector_store_description

        vector_store_metadata: dict[str, Any] | None | str | Unset
        if isinstance(self.vector_store_metadata, Unset):
            vector_store_metadata = UNSET
        elif isinstance(self.vector_store_metadata, LiteLLMManagedVectorStoreVectorStoreMetadataType0):
            vector_store_metadata = self.vector_store_metadata.to_dict()
        else:
            vector_store_metadata = self.vector_store_metadata

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        litellm_credential_name: None | str | Unset
        if isinstance(self.litellm_credential_name, Unset):
            litellm_credential_name = UNSET
        else:
            litellm_credential_name = self.litellm_credential_name

        litellm_params: dict[str, Any] | None | Unset
        if isinstance(self.litellm_params, Unset):
            litellm_params = UNSET
        elif isinstance(self.litellm_params, LiteLLMManagedVectorStoreLitellmParamsType0):
            litellm_params = self.litellm_params.to_dict()
        else:
            litellm_params = self.litellm_params

        team_id: None | str | Unset
        if isinstance(self.team_id, Unset):
            team_id = UNSET
        else:
            team_id = self.team_id

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if vector_store_id is not UNSET:
            field_dict["vector_store_id"] = vector_store_id
        if custom_llm_provider is not UNSET:
            field_dict["custom_llm_provider"] = custom_llm_provider
        if vector_store_name is not UNSET:
            field_dict["vector_store_name"] = vector_store_name
        if vector_store_description is not UNSET:
            field_dict["vector_store_description"] = vector_store_description
        if vector_store_metadata is not UNSET:
            field_dict["vector_store_metadata"] = vector_store_metadata
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if litellm_credential_name is not UNSET:
            field_dict["litellm_credential_name"] = litellm_credential_name
        if litellm_params is not UNSET:
            field_dict["litellm_params"] = litellm_params
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lite_llm_managed_vector_store_litellm_params_type_0 import LiteLLMManagedVectorStoreLitellmParamsType0
        from ..models.lite_llm_managed_vector_store_vector_store_metadata_type_0 import LiteLLMManagedVectorStoreVectorStoreMetadataType0
        d = dict(src_dict)
        vector_store_id = d.pop("vector_store_id", UNSET)

        custom_llm_provider = d.pop("custom_llm_provider", UNSET)

        def _parse_vector_store_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vector_store_name = _parse_vector_store_name(d.pop("vector_store_name", UNSET))


        def _parse_vector_store_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vector_store_description = _parse_vector_store_description(d.pop("vector_store_description", UNSET))


        def _parse_vector_store_metadata(data: object) -> LiteLLMManagedVectorStoreVectorStoreMetadataType0 | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vector_store_metadata_type_0 = LiteLLMManagedVectorStoreVectorStoreMetadataType0.from_dict(data)



                return vector_store_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMManagedVectorStoreVectorStoreMetadataType0 | None | str | Unset, data)

        vector_store_metadata = _parse_vector_store_metadata(d.pop("vector_store_metadata", UNSET))


        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)



                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))


        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)



                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))


        def _parse_litellm_credential_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        litellm_credential_name = _parse_litellm_credential_name(d.pop("litellm_credential_name", UNSET))


        def _parse_litellm_params(data: object) -> LiteLLMManagedVectorStoreLitellmParamsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                litellm_params_type_0 = LiteLLMManagedVectorStoreLitellmParamsType0.from_dict(data)



                return litellm_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMManagedVectorStoreLitellmParamsType0 | None | Unset, data)

        litellm_params = _parse_litellm_params(d.pop("litellm_params", UNSET))


        def _parse_team_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        team_id = _parse_team_id(d.pop("team_id", UNSET))


        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))


        lite_llm_managed_vector_store = cls(
            vector_store_id=vector_store_id,
            custom_llm_provider=custom_llm_provider,
            vector_store_name=vector_store_name,
            vector_store_description=vector_store_description,
            vector_store_metadata=vector_store_metadata,
            created_at=created_at,
            updated_at=updated_at,
            litellm_credential_name=litellm_credential_name,
            litellm_params=litellm_params,
            team_id=team_id,
            user_id=user_id,
        )


        lite_llm_managed_vector_store.additional_properties = d
        return lite_llm_managed_vector_store

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

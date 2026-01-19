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
  from ..models.lite_llm_budget_table import LiteLLMBudgetTable
  from ..models.lite_llm_object_permission_table import LiteLLMObjectPermissionTable
  from ..models.lite_llm_user_table import LiteLLMUserTable
  from ..models.new_organization_response_metadata_type_0 import NewOrganizationResponseMetadataType0





T = TypeVar("T", bound="NewOrganizationResponse")



@_attrs_define
class NewOrganizationResponse:
    """ 
        Attributes:
            organization_id (str):
            budget_id (str):
            models (list[str]):
            created_by (str):
            updated_by (str):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            organization_alias (None | str | Unset):
            spend (float | Unset):  Default: 0.0.
            metadata (NewOrganizationResponseMetadataType0 | None | Unset):
            users (list[LiteLLMUserTable] | None | Unset):
            litellm_budget_table (LiteLLMBudgetTable | None | Unset):
            object_permission (LiteLLMObjectPermissionTable | None | Unset):
            object_permission_id (None | str | Unset):
     """

    organization_id: str
    budget_id: str
    models: list[str]
    created_by: str
    updated_by: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    organization_alias: None | str | Unset = UNSET
    spend: float | Unset = 0.0
    metadata: NewOrganizationResponseMetadataType0 | None | Unset = UNSET
    users: list[LiteLLMUserTable] | None | Unset = UNSET
    litellm_budget_table: LiteLLMBudgetTable | None | Unset = UNSET
    object_permission: LiteLLMObjectPermissionTable | None | Unset = UNSET
    object_permission_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.lite_llm_object_permission_table import LiteLLMObjectPermissionTable
        from ..models.lite_llm_user_table import LiteLLMUserTable
        from ..models.new_organization_response_metadata_type_0 import NewOrganizationResponseMetadataType0
        from ..models.lite_llm_budget_table import LiteLLMBudgetTable
        organization_id = self.organization_id

        budget_id = self.budget_id

        models = self.models



        created_by = self.created_by

        updated_by = self.updated_by

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        organization_alias: None | str | Unset
        if isinstance(self.organization_alias, Unset):
            organization_alias = UNSET
        else:
            organization_alias = self.organization_alias

        spend = self.spend

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, NewOrganizationResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        users: list[dict[str, Any]] | None | Unset
        if isinstance(self.users, Unset):
            users = UNSET
        elif isinstance(self.users, list):
            users = []
            for users_type_0_item_data in self.users:
                users_type_0_item = users_type_0_item_data.to_dict()
                users.append(users_type_0_item)


        else:
            users = self.users

        litellm_budget_table: dict[str, Any] | None | Unset
        if isinstance(self.litellm_budget_table, Unset):
            litellm_budget_table = UNSET
        elif isinstance(self.litellm_budget_table, LiteLLMBudgetTable):
            litellm_budget_table = self.litellm_budget_table.to_dict()
        else:
            litellm_budget_table = self.litellm_budget_table

        object_permission: dict[str, Any] | None | Unset
        if isinstance(self.object_permission, Unset):
            object_permission = UNSET
        elif isinstance(self.object_permission, LiteLLMObjectPermissionTable):
            object_permission = self.object_permission.to_dict()
        else:
            object_permission = self.object_permission

        object_permission_id: None | str | Unset
        if isinstance(self.object_permission_id, Unset):
            object_permission_id = UNSET
        else:
            object_permission_id = self.object_permission_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "organization_id": organization_id,
            "budget_id": budget_id,
            "models": models,
            "created_by": created_by,
            "updated_by": updated_by,
            "created_at": created_at,
            "updated_at": updated_at,
        })
        if organization_alias is not UNSET:
            field_dict["organization_alias"] = organization_alias
        if spend is not UNSET:
            field_dict["spend"] = spend
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if users is not UNSET:
            field_dict["users"] = users
        if litellm_budget_table is not UNSET:
            field_dict["litellm_budget_table"] = litellm_budget_table
        if object_permission is not UNSET:
            field_dict["object_permission"] = object_permission
        if object_permission_id is not UNSET:
            field_dict["object_permission_id"] = object_permission_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lite_llm_budget_table import LiteLLMBudgetTable
        from ..models.lite_llm_object_permission_table import LiteLLMObjectPermissionTable
        from ..models.lite_llm_user_table import LiteLLMUserTable
        from ..models.new_organization_response_metadata_type_0 import NewOrganizationResponseMetadataType0
        d = dict(src_dict)
        organization_id = d.pop("organization_id")

        budget_id = d.pop("budget_id")

        models = cast(list[str], d.pop("models"))


        created_by = d.pop("created_by")

        updated_by = d.pop("updated_by")

        created_at = isoparse(d.pop("created_at"))




        updated_at = isoparse(d.pop("updated_at"))




        def _parse_organization_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        organization_alias = _parse_organization_alias(d.pop("organization_alias", UNSET))


        spend = d.pop("spend", UNSET)

        def _parse_metadata(data: object) -> NewOrganizationResponseMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = NewOrganizationResponseMetadataType0.from_dict(data)



                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NewOrganizationResponseMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


        def _parse_users(data: object) -> list[LiteLLMUserTable] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                users_type_0 = []
                _users_type_0 = data
                for users_type_0_item_data in (_users_type_0):
                    users_type_0_item = LiteLLMUserTable.from_dict(users_type_0_item_data)



                    users_type_0.append(users_type_0_item)

                return users_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LiteLLMUserTable] | None | Unset, data)

        users = _parse_users(d.pop("users", UNSET))


        def _parse_litellm_budget_table(data: object) -> LiteLLMBudgetTable | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                litellm_budget_table_type_0 = LiteLLMBudgetTable.from_dict(data)



                return litellm_budget_table_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMBudgetTable | None | Unset, data)

        litellm_budget_table = _parse_litellm_budget_table(d.pop("litellm_budget_table", UNSET))


        def _parse_object_permission(data: object) -> LiteLLMObjectPermissionTable | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                object_permission_type_0 = LiteLLMObjectPermissionTable.from_dict(data)



                return object_permission_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMObjectPermissionTable | None | Unset, data)

        object_permission = _parse_object_permission(d.pop("object_permission", UNSET))


        def _parse_object_permission_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_permission_id = _parse_object_permission_id(d.pop("object_permission_id", UNSET))


        new_organization_response = cls(
            organization_id=organization_id,
            budget_id=budget_id,
            models=models,
            created_by=created_by,
            updated_by=updated_by,
            created_at=created_at,
            updated_at=updated_at,
            organization_alias=organization_alias,
            spend=spend,
            metadata=metadata,
            users=users,
            litellm_budget_table=litellm_budget_table,
            object_permission=object_permission,
            object_permission_id=object_permission_id,
        )


        new_organization_response.additional_properties = d
        return new_organization_response

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

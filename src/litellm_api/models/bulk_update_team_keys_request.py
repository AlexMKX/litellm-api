from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.key_update_fields import KeyUpdateFields





T = TypeVar("T", bound="BulkUpdateTeamKeysRequest")



@_attrs_define
class BulkUpdateTeamKeysRequest:
    """ Apply one update payload to many keys inside a team; provide either `key_ids` or `all_keys_in_team=True`.

        Attributes:
            team_id (str):
            update_fields (KeyUpdateFields): Allowlist of bulk-broadcastable fields for /team/key/bulk_update;
                `extra="forbid"` blocks RBAC/ownership/scope mutations even by team admins.
            key_ids (list[str] | None | Unset):
            all_keys_in_team (bool | Unset):  Default: False.
     """

    team_id: str
    update_fields: KeyUpdateFields
    key_ids: list[str] | None | Unset = UNSET
    all_keys_in_team: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.key_update_fields import KeyUpdateFields
        team_id = self.team_id

        update_fields = self.update_fields.to_dict()

        key_ids: list[str] | None | Unset
        if isinstance(self.key_ids, Unset):
            key_ids = UNSET
        elif isinstance(self.key_ids, list):
            key_ids = self.key_ids


        else:
            key_ids = self.key_ids

        all_keys_in_team = self.all_keys_in_team


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "team_id": team_id,
            "update_fields": update_fields,
        })
        if key_ids is not UNSET:
            field_dict["key_ids"] = key_ids
        if all_keys_in_team is not UNSET:
            field_dict["all_keys_in_team"] = all_keys_in_team

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.key_update_fields import KeyUpdateFields
        d = dict(src_dict)
        team_id = d.pop("team_id")

        update_fields = KeyUpdateFields.from_dict(d.pop("update_fields"))




        def _parse_key_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                key_ids_type_0 = cast(list[str], data)

                return key_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        key_ids = _parse_key_ids(d.pop("key_ids", UNSET))


        all_keys_in_team = d.pop("all_keys_in_team", UNSET)

        bulk_update_team_keys_request = cls(
            team_id=team_id,
            update_fields=update_fields,
            key_ids=key_ids,
            all_keys_in_team=all_keys_in_team,
        )


        bulk_update_team_keys_request.additional_properties = d
        return bulk_update_team_keys_request

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

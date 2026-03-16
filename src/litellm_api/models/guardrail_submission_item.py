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
  from ..models.guardrail_submission_item_guardrail_info_type_0 import GuardrailSubmissionItemGuardrailInfoType0
  from ..models.guardrail_submission_item_litellm_params_type_0 import GuardrailSubmissionItemLitellmParamsType0





T = TypeVar("T", bound="GuardrailSubmissionItem")



@_attrs_define
class GuardrailSubmissionItem:
    """ 
        Attributes:
            guardrail_id (str):
            guardrail_name (str):
            status (str):
            team_id (None | str | Unset):
            team_guardrail (bool | Unset):  Default: False.
            litellm_params (GuardrailSubmissionItemLitellmParamsType0 | None | Unset):
            guardrail_info (GuardrailSubmissionItemGuardrailInfoType0 | None | Unset):
            submitted_by_user_id (None | str | Unset):
            submitted_by_email (None | str | Unset):
            submitted_at (datetime.datetime | None | Unset):
            reviewed_at (datetime.datetime | None | Unset):
            created_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | None | Unset):
     """

    guardrail_id: str
    guardrail_name: str
    status: str
    team_id: None | str | Unset = UNSET
    team_guardrail: bool | Unset = False
    litellm_params: GuardrailSubmissionItemLitellmParamsType0 | None | Unset = UNSET
    guardrail_info: GuardrailSubmissionItemGuardrailInfoType0 | None | Unset = UNSET
    submitted_by_user_id: None | str | Unset = UNSET
    submitted_by_email: None | str | Unset = UNSET
    submitted_at: datetime.datetime | None | Unset = UNSET
    reviewed_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.guardrail_submission_item_guardrail_info_type_0 import GuardrailSubmissionItemGuardrailInfoType0
        from ..models.guardrail_submission_item_litellm_params_type_0 import GuardrailSubmissionItemLitellmParamsType0
        guardrail_id = self.guardrail_id

        guardrail_name = self.guardrail_name

        status = self.status

        team_id: None | str | Unset
        if isinstance(self.team_id, Unset):
            team_id = UNSET
        else:
            team_id = self.team_id

        team_guardrail = self.team_guardrail

        litellm_params: dict[str, Any] | None | Unset
        if isinstance(self.litellm_params, Unset):
            litellm_params = UNSET
        elif isinstance(self.litellm_params, GuardrailSubmissionItemLitellmParamsType0):
            litellm_params = self.litellm_params.to_dict()
        else:
            litellm_params = self.litellm_params

        guardrail_info: dict[str, Any] | None | Unset
        if isinstance(self.guardrail_info, Unset):
            guardrail_info = UNSET
        elif isinstance(self.guardrail_info, GuardrailSubmissionItemGuardrailInfoType0):
            guardrail_info = self.guardrail_info.to_dict()
        else:
            guardrail_info = self.guardrail_info

        submitted_by_user_id: None | str | Unset
        if isinstance(self.submitted_by_user_id, Unset):
            submitted_by_user_id = UNSET
        else:
            submitted_by_user_id = self.submitted_by_user_id

        submitted_by_email: None | str | Unset
        if isinstance(self.submitted_by_email, Unset):
            submitted_by_email = UNSET
        else:
            submitted_by_email = self.submitted_by_email

        submitted_at: None | str | Unset
        if isinstance(self.submitted_at, Unset):
            submitted_at = UNSET
        elif isinstance(self.submitted_at, datetime.datetime):
            submitted_at = self.submitted_at.isoformat()
        else:
            submitted_at = self.submitted_at

        reviewed_at: None | str | Unset
        if isinstance(self.reviewed_at, Unset):
            reviewed_at = UNSET
        elif isinstance(self.reviewed_at, datetime.datetime):
            reviewed_at = self.reviewed_at.isoformat()
        else:
            reviewed_at = self.reviewed_at

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


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "guardrail_id": guardrail_id,
            "guardrail_name": guardrail_name,
            "status": status,
        })
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if team_guardrail is not UNSET:
            field_dict["team_guardrail"] = team_guardrail
        if litellm_params is not UNSET:
            field_dict["litellm_params"] = litellm_params
        if guardrail_info is not UNSET:
            field_dict["guardrail_info"] = guardrail_info
        if submitted_by_user_id is not UNSET:
            field_dict["submitted_by_user_id"] = submitted_by_user_id
        if submitted_by_email is not UNSET:
            field_dict["submitted_by_email"] = submitted_by_email
        if submitted_at is not UNSET:
            field_dict["submitted_at"] = submitted_at
        if reviewed_at is not UNSET:
            field_dict["reviewed_at"] = reviewed_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.guardrail_submission_item_guardrail_info_type_0 import GuardrailSubmissionItemGuardrailInfoType0
        from ..models.guardrail_submission_item_litellm_params_type_0 import GuardrailSubmissionItemLitellmParamsType0
        d = dict(src_dict)
        guardrail_id = d.pop("guardrail_id")

        guardrail_name = d.pop("guardrail_name")

        status = d.pop("status")

        def _parse_team_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        team_id = _parse_team_id(d.pop("team_id", UNSET))


        team_guardrail = d.pop("team_guardrail", UNSET)

        def _parse_litellm_params(data: object) -> GuardrailSubmissionItemLitellmParamsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                litellm_params_type_0 = GuardrailSubmissionItemLitellmParamsType0.from_dict(data)



                return litellm_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GuardrailSubmissionItemLitellmParamsType0 | None | Unset, data)

        litellm_params = _parse_litellm_params(d.pop("litellm_params", UNSET))


        def _parse_guardrail_info(data: object) -> GuardrailSubmissionItemGuardrailInfoType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                guardrail_info_type_0 = GuardrailSubmissionItemGuardrailInfoType0.from_dict(data)



                return guardrail_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GuardrailSubmissionItemGuardrailInfoType0 | None | Unset, data)

        guardrail_info = _parse_guardrail_info(d.pop("guardrail_info", UNSET))


        def _parse_submitted_by_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        submitted_by_user_id = _parse_submitted_by_user_id(d.pop("submitted_by_user_id", UNSET))


        def _parse_submitted_by_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        submitted_by_email = _parse_submitted_by_email(d.pop("submitted_by_email", UNSET))


        def _parse_submitted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                submitted_at_type_0 = isoparse(data)



                return submitted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        submitted_at = _parse_submitted_at(d.pop("submitted_at", UNSET))


        def _parse_reviewed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reviewed_at_type_0 = isoparse(data)



                return reviewed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        reviewed_at = _parse_reviewed_at(d.pop("reviewed_at", UNSET))


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


        guardrail_submission_item = cls(
            guardrail_id=guardrail_id,
            guardrail_name=guardrail_name,
            status=status,
            team_id=team_id,
            team_guardrail=team_guardrail,
            litellm_params=litellm_params,
            guardrail_info=guardrail_info,
            submitted_by_user_id=submitted_by_user_id,
            submitted_by_email=submitted_by_email,
            submitted_at=submitted_at,
            reviewed_at=reviewed_at,
            created_at=created_at,
            updated_at=updated_at,
        )


        guardrail_submission_item.additional_properties = d
        return guardrail_submission_item

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

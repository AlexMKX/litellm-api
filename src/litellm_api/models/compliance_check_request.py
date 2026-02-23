from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.compliance_check_request_guardrail_information_type_0_item import ComplianceCheckRequestGuardrailInformationType0Item





T = TypeVar("T", bound="ComplianceCheckRequest")



@_attrs_define
class ComplianceCheckRequest:
    """ Request payload for compliance check endpoints.

    Mirrors the spend log fields needed for compliance evaluation.

        Attributes:
            request_id (str):
            user_id (None | str | Unset):
            model (None | str | Unset):
            timestamp (None | str | Unset):
            guardrail_information (list[ComplianceCheckRequestGuardrailInformationType0Item] | None | Unset):
     """

    request_id: str
    user_id: None | str | Unset = UNSET
    model: None | str | Unset = UNSET
    timestamp: None | str | Unset = UNSET
    guardrail_information: list[ComplianceCheckRequestGuardrailInformationType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.compliance_check_request_guardrail_information_type_0_item import ComplianceCheckRequestGuardrailInformationType0Item
        request_id = self.request_id

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        timestamp: None | str | Unset
        if isinstance(self.timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = self.timestamp

        guardrail_information: list[dict[str, Any]] | None | Unset
        if isinstance(self.guardrail_information, Unset):
            guardrail_information = UNSET
        elif isinstance(self.guardrail_information, list):
            guardrail_information = []
            for guardrail_information_type_0_item_data in self.guardrail_information:
                guardrail_information_type_0_item = guardrail_information_type_0_item_data.to_dict()
                guardrail_information.append(guardrail_information_type_0_item)


        else:
            guardrail_information = self.guardrail_information


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "request_id": request_id,
        })
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if model is not UNSET:
            field_dict["model"] = model
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if guardrail_information is not UNSET:
            field_dict["guardrail_information"] = guardrail_information

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compliance_check_request_guardrail_information_type_0_item import ComplianceCheckRequestGuardrailInformationType0Item
        d = dict(src_dict)
        request_id = d.pop("request_id")

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))


        def _parse_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))


        def _parse_timestamp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timestamp = _parse_timestamp(d.pop("timestamp", UNSET))


        def _parse_guardrail_information(data: object) -> list[ComplianceCheckRequestGuardrailInformationType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                guardrail_information_type_0 = []
                _guardrail_information_type_0 = data
                for guardrail_information_type_0_item_data in (_guardrail_information_type_0):
                    guardrail_information_type_0_item = ComplianceCheckRequestGuardrailInformationType0Item.from_dict(guardrail_information_type_0_item_data)



                    guardrail_information_type_0.append(guardrail_information_type_0_item)

                return guardrail_information_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ComplianceCheckRequestGuardrailInformationType0Item] | None | Unset, data)

        guardrail_information = _parse_guardrail_information(d.pop("guardrail_information", UNSET))


        compliance_check_request = cls(
            request_id=request_id,
            user_id=user_id,
            model=model,
            timestamp=timestamp,
            guardrail_information=guardrail_information,
        )


        compliance_check_request.additional_properties = d
        return compliance_check_request

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

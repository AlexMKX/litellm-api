from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.workflow_event_create_request_data_type_0 import WorkflowEventCreateRequestDataType0





T = TypeVar("T", bound="WorkflowEventCreateRequest")



@_attrs_define
class WorkflowEventCreateRequest:
    """ 
        Attributes:
            event_type (str):
            step_name (str):
            data (None | Unset | WorkflowEventCreateRequestDataType0):
     """

    event_type: str
    step_name: str
    data: None | Unset | WorkflowEventCreateRequestDataType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_event_create_request_data_type_0 import WorkflowEventCreateRequestDataType0
        event_type = self.event_type

        step_name = self.step_name

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, WorkflowEventCreateRequestDataType0):
            data = self.data.to_dict()
        else:
            data = self.data


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "event_type": event_type,
            "step_name": step_name,
        })
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_event_create_request_data_type_0 import WorkflowEventCreateRequestDataType0
        d = dict(src_dict)
        event_type = d.pop("event_type")

        step_name = d.pop("step_name")

        def _parse_data(data: object) -> None | Unset | WorkflowEventCreateRequestDataType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = WorkflowEventCreateRequestDataType0.from_dict(data)



                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WorkflowEventCreateRequestDataType0, data)

        data = _parse_data(d.pop("data", UNSET))


        workflow_event_create_request = cls(
            event_type=event_type,
            step_name=step_name,
            data=data,
        )


        workflow_event_create_request.additional_properties = d
        return workflow_event_create_request

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

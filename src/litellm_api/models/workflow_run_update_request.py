from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.workflow_run_update_request_status_type_0 import WorkflowRunUpdateRequestStatusType0
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.workflow_run_update_request_metadata_type_0 import WorkflowRunUpdateRequestMetadataType0
  from ..models.workflow_run_update_request_output_type_0 import WorkflowRunUpdateRequestOutputType0





T = TypeVar("T", bound="WorkflowRunUpdateRequest")



@_attrs_define
class WorkflowRunUpdateRequest:
    """ 
        Attributes:
            status (None | Unset | WorkflowRunUpdateRequestStatusType0):
            output (None | Unset | WorkflowRunUpdateRequestOutputType0):
            metadata (None | Unset | WorkflowRunUpdateRequestMetadataType0):
     """

    status: None | Unset | WorkflowRunUpdateRequestStatusType0 = UNSET
    output: None | Unset | WorkflowRunUpdateRequestOutputType0 = UNSET
    metadata: None | Unset | WorkflowRunUpdateRequestMetadataType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_run_update_request_metadata_type_0 import WorkflowRunUpdateRequestMetadataType0
        from ..models.workflow_run_update_request_output_type_0 import WorkflowRunUpdateRequestOutputType0
        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, WorkflowRunUpdateRequestStatusType0):
            status = self.status.value
        else:
            status = self.status

        output: dict[str, Any] | None | Unset
        if isinstance(self.output, Unset):
            output = UNSET
        elif isinstance(self.output, WorkflowRunUpdateRequestOutputType0):
            output = self.output.to_dict()
        else:
            output = self.output

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, WorkflowRunUpdateRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if status is not UNSET:
            field_dict["status"] = status
        if output is not UNSET:
            field_dict["output"] = output
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_run_update_request_metadata_type_0 import WorkflowRunUpdateRequestMetadataType0
        from ..models.workflow_run_update_request_output_type_0 import WorkflowRunUpdateRequestOutputType0
        d = dict(src_dict)
        def _parse_status(data: object) -> None | Unset | WorkflowRunUpdateRequestStatusType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = WorkflowRunUpdateRequestStatusType0(data)



                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WorkflowRunUpdateRequestStatusType0, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_output(data: object) -> None | Unset | WorkflowRunUpdateRequestOutputType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                output_type_0 = WorkflowRunUpdateRequestOutputType0.from_dict(data)



                return output_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WorkflowRunUpdateRequestOutputType0, data)

        output = _parse_output(d.pop("output", UNSET))


        def _parse_metadata(data: object) -> None | Unset | WorkflowRunUpdateRequestMetadataType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = WorkflowRunUpdateRequestMetadataType0.from_dict(data)



                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WorkflowRunUpdateRequestMetadataType0, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


        workflow_run_update_request = cls(
            status=status,
            output=output,
            metadata=metadata,
        )


        workflow_run_update_request.additional_properties = d
        return workflow_run_update_request

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

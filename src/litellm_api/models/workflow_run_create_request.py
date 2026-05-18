from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.workflow_run_create_request_input_type_0 import WorkflowRunCreateRequestInputType0
  from ..models.workflow_run_create_request_metadata_type_0 import WorkflowRunCreateRequestMetadataType0





T = TypeVar("T", bound="WorkflowRunCreateRequest")



@_attrs_define
class WorkflowRunCreateRequest:
    """ 
        Attributes:
            workflow_type (str):
            input_ (None | Unset | WorkflowRunCreateRequestInputType0):
            metadata (None | Unset | WorkflowRunCreateRequestMetadataType0):
     """

    workflow_type: str
    input_: None | Unset | WorkflowRunCreateRequestInputType0 = UNSET
    metadata: None | Unset | WorkflowRunCreateRequestMetadataType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_run_create_request_input_type_0 import WorkflowRunCreateRequestInputType0
        from ..models.workflow_run_create_request_metadata_type_0 import WorkflowRunCreateRequestMetadataType0
        workflow_type = self.workflow_type

        input_: dict[str, Any] | None | Unset
        if isinstance(self.input_, Unset):
            input_ = UNSET
        elif isinstance(self.input_, WorkflowRunCreateRequestInputType0):
            input_ = self.input_.to_dict()
        else:
            input_ = self.input_

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, WorkflowRunCreateRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "workflow_type": workflow_type,
        })
        if input_ is not UNSET:
            field_dict["input"] = input_
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_run_create_request_input_type_0 import WorkflowRunCreateRequestInputType0
        from ..models.workflow_run_create_request_metadata_type_0 import WorkflowRunCreateRequestMetadataType0
        d = dict(src_dict)
        workflow_type = d.pop("workflow_type")

        def _parse_input_(data: object) -> None | Unset | WorkflowRunCreateRequestInputType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                input_type_0 = WorkflowRunCreateRequestInputType0.from_dict(data)



                return input_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WorkflowRunCreateRequestInputType0, data)

        input_ = _parse_input_(d.pop("input", UNSET))


        def _parse_metadata(data: object) -> None | Unset | WorkflowRunCreateRequestMetadataType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = WorkflowRunCreateRequestMetadataType0.from_dict(data)



                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WorkflowRunCreateRequestMetadataType0, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


        workflow_run_create_request = cls(
            workflow_type=workflow_type,
            input_=input_,
            metadata=metadata,
        )


        workflow_run_create_request.additional_properties = d
        return workflow_run_create_request

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.pipeline_test_request_pipeline import PipelineTestRequestPipeline
  from ..models.pipeline_test_request_test_messages_item import PipelineTestRequestTestMessagesItem





T = TypeVar("T", bound="PipelineTestRequest")



@_attrs_define
class PipelineTestRequest:
    """ Request body for testing a guardrail pipeline with sample messages.

        Attributes:
            pipeline (PipelineTestRequestPipeline): Pipeline definition with 'mode' and 'steps'.
            test_messages (list[PipelineTestRequestTestMessagesItem]): Test messages to run through the pipeline, e.g.
                [{'role': 'user', 'content': '...'}].
     """

    pipeline: PipelineTestRequestPipeline
    test_messages: list[PipelineTestRequestTestMessagesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.pipeline_test_request_pipeline import PipelineTestRequestPipeline
        from ..models.pipeline_test_request_test_messages_item import PipelineTestRequestTestMessagesItem
        pipeline = self.pipeline.to_dict()

        test_messages = []
        for test_messages_item_data in self.test_messages:
            test_messages_item = test_messages_item_data.to_dict()
            test_messages.append(test_messages_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "pipeline": pipeline,
            "test_messages": test_messages,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pipeline_test_request_pipeline import PipelineTestRequestPipeline
        from ..models.pipeline_test_request_test_messages_item import PipelineTestRequestTestMessagesItem
        d = dict(src_dict)
        pipeline = PipelineTestRequestPipeline.from_dict(d.pop("pipeline"))




        test_messages = []
        _test_messages = d.pop("test_messages")
        for test_messages_item_data in (_test_messages):
            test_messages_item = PipelineTestRequestTestMessagesItem.from_dict(test_messages_item_data)



            test_messages.append(test_messages_item)


        pipeline_test_request = cls(
            pipeline=pipeline,
            test_messages=test_messages,
        )


        pipeline_test_request.additional_properties = d
        return pipeline_test_request

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

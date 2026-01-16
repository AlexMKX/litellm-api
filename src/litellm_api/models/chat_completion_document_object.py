from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.citations_object import CitationsObject
  from ..models.document_object import DocumentObject





T = TypeVar("T", bound="ChatCompletionDocumentObject")



@_attrs_define
class ChatCompletionDocumentObject:
    """ 
        Attributes:
            type_ (Literal['document']):
            source (DocumentObject):
            title (str):
            context (str):
            citations (CitationsObject | None):
     """

    type_: Literal['document']
    source: DocumentObject
    title: str
    context: str
    citations: CitationsObject | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.citations_object import CitationsObject
        from ..models.document_object import DocumentObject
        type_ = self.type_

        source = self.source.to_dict()

        title = self.title

        context = self.context

        citations: dict[str, Any] | None
        if isinstance(self.citations, CitationsObject):
            citations = self.citations.to_dict()
        else:
            citations = self.citations


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "source": source,
            "title": title,
            "context": context,
            "citations": citations,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.citations_object import CitationsObject
        from ..models.document_object import DocumentObject
        d = dict(src_dict)
        type_ = cast(Literal['document'] , d.pop("type"))
        if type_ != 'document':
            raise ValueError(f"type must match const 'document', got '{type_}'")

        source = DocumentObject.from_dict(d.pop("source"))




        title = d.pop("title")

        context = d.pop("context")

        def _parse_citations(data: object) -> CitationsObject | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                citations_type_0 = CitationsObject.from_dict(data)



                return citations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CitationsObject | None, data)

        citations = _parse_citations(d.pop("citations"))


        chat_completion_document_object = cls(
            type_=type_,
            source=source,
            title=title,
            context=context,
            citations=citations,
        )


        chat_completion_document_object.additional_properties = d
        return chat_completion_document_object

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="MCPSemanticFilterSettings")



@_attrs_define
class MCPSemanticFilterSettings:
    """ Configuration for MCP Semantic Tool Filter

        Attributes:
            enabled (bool | Unset): Enable semantic filtering of MCP tools based on query relevance Default: False.
            embedding_model (str | Unset): Embedding model to use for semantic similarity (e.g., 'text-embedding-3-small',
                'text-embedding-ada-002') Default: 'text-embedding-3-small'.
            top_k (int | Unset): Number of most relevant tools to return Default: 10.
            similarity_threshold (float | Unset): Minimum similarity score for tool inclusion (0.0 to 1.0, where 1.0 = exact
                match) Default: 0.3.
     """

    enabled: bool | Unset = False
    embedding_model: str | Unset = 'text-embedding-3-small'
    top_k: int | Unset = 10
    similarity_threshold: float | Unset = 0.3
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        embedding_model = self.embedding_model

        top_k = self.top_k

        similarity_threshold = self.similarity_threshold


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if embedding_model is not UNSET:
            field_dict["embedding_model"] = embedding_model
        if top_k is not UNSET:
            field_dict["top_k"] = top_k
        if similarity_threshold is not UNSET:
            field_dict["similarity_threshold"] = similarity_threshold

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        embedding_model = d.pop("embedding_model", UNSET)

        top_k = d.pop("top_k", UNSET)

        similarity_threshold = d.pop("similarity_threshold", UNSET)

        mcp_semantic_filter_settings = cls(
            enabled=enabled,
            embedding_model=embedding_model,
            top_k=top_k,
            similarity_threshold=similarity_threshold,
        )


        mcp_semantic_filter_settings.additional_properties = d
        return mcp_semantic_filter_settings

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

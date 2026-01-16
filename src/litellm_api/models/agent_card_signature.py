from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.agent_card_signature_header_type_0 import AgentCardSignatureHeaderType0





T = TypeVar("T", bound="AgentCardSignature")



@_attrs_define
class AgentCardSignature:
    """ Represents a JWS signature of an AgentCard.

        Attributes:
            protected (str | Unset):
            signature (str | Unset):
            header (AgentCardSignatureHeaderType0 | None | Unset):
     """

    protected: str | Unset = UNSET
    signature: str | Unset = UNSET
    header: AgentCardSignatureHeaderType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_card_signature_header_type_0 import AgentCardSignatureHeaderType0
        protected = self.protected

        signature = self.signature

        header: dict[str, Any] | None | Unset
        if isinstance(self.header, Unset):
            header = UNSET
        elif isinstance(self.header, AgentCardSignatureHeaderType0):
            header = self.header.to_dict()
        else:
            header = self.header


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if protected is not UNSET:
            field_dict["protected"] = protected
        if signature is not UNSET:
            field_dict["signature"] = signature
        if header is not UNSET:
            field_dict["header"] = header

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_card_signature_header_type_0 import AgentCardSignatureHeaderType0
        d = dict(src_dict)
        protected = d.pop("protected", UNSET)

        signature = d.pop("signature", UNSET)

        def _parse_header(data: object) -> AgentCardSignatureHeaderType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                header_type_0 = AgentCardSignatureHeaderType0.from_dict(data)



                return header_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentCardSignatureHeaderType0 | None | Unset, data)

        header = _parse_header(d.pop("header", UNSET))


        agent_card_signature = cls(
            protected=protected,
            signature=signature,
            header=header,
        )


        agent_card_signature.additional_properties = d
        return agent_card_signature

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

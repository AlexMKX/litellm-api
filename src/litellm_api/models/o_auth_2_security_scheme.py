from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.o_auth_flows import OAuthFlows





T = TypeVar("T", bound="OAuth2SecurityScheme")



@_attrs_define
class OAuth2SecurityScheme:
    """ Defines a security scheme using OAuth 2.0.

        Attributes:
            type_ (Literal['oauth2']):
            flows (OAuthFlows): Defines the configuration for the supported OAuth 2.0 flows.
            oauth_2_metadata_url (None | str):
            description (None | str | Unset):
     """

    type_: Literal['oauth2']
    flows: OAuthFlows
    oauth_2_metadata_url: None | str
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.o_auth_flows import OAuthFlows
        type_ = self.type_

        flows = self.flows.to_dict()

        oauth_2_metadata_url: None | str
        oauth_2_metadata_url = self.oauth_2_metadata_url

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "flows": flows,
            "oauth2MetadataUrl": oauth_2_metadata_url,
        })
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.o_auth_flows import OAuthFlows
        d = dict(src_dict)
        type_ = cast(Literal['oauth2'] , d.pop("type"))
        if type_ != 'oauth2':
            raise ValueError(f"type must match const 'oauth2', got '{type_}'")

        flows = OAuthFlows.from_dict(d.pop("flows"))




        def _parse_oauth_2_metadata_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        oauth_2_metadata_url = _parse_oauth_2_metadata_url(d.pop("oauth2MetadataUrl"))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        o_auth_2_security_scheme = cls(
            type_=type_,
            flows=flows,
            oauth_2_metadata_url=oauth_2_metadata_url,
            description=description,
        )


        o_auth_2_security_scheme.additional_properties = d
        return o_auth_2_security_scheme

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

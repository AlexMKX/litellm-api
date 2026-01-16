from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.api_key_security_scheme import APIKeySecurityScheme
  from ..models.http_auth_security_scheme import HTTPAuthSecurityScheme
  from ..models.mutual_tls_security_scheme import MutualTLSSecurityScheme
  from ..models.o_auth_2_security_scheme import OAuth2SecurityScheme
  from ..models.open_id_connect_security_scheme import OpenIdConnectSecurityScheme





T = TypeVar("T", bound="AgentCardSecuritySchemesType0")



@_attrs_define
class AgentCardSecuritySchemesType0:
    """ 
     """

    additional_properties: dict[str, APIKeySecurityScheme | HTTPAuthSecurityScheme | MutualTLSSecurityScheme | OAuth2SecurityScheme | OpenIdConnectSecurityScheme] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.mutual_tls_security_scheme import MutualTLSSecurityScheme
        from ..models.http_auth_security_scheme import HTTPAuthSecurityScheme
        from ..models.api_key_security_scheme import APIKeySecurityScheme
        from ..models.o_auth_2_security_scheme import OAuth2SecurityScheme
        from ..models.open_id_connect_security_scheme import OpenIdConnectSecurityScheme
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            
            if isinstance(prop, APIKeySecurityScheme):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, HTTPAuthSecurityScheme):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, OAuth2SecurityScheme):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, OpenIdConnectSecurityScheme):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop.to_dict()



        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key_security_scheme import APIKeySecurityScheme
        from ..models.http_auth_security_scheme import HTTPAuthSecurityScheme
        from ..models.mutual_tls_security_scheme import MutualTLSSecurityScheme
        from ..models.o_auth_2_security_scheme import OAuth2SecurityScheme
        from ..models.open_id_connect_security_scheme import OpenIdConnectSecurityScheme
        d = dict(src_dict)
        agent_card_security_schemes_type_0 = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            def _parse_additional_property(data: object) -> APIKeySecurityScheme | HTTPAuthSecurityScheme | MutualTLSSecurityScheme | OAuth2SecurityScheme | OpenIdConnectSecurityScheme:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_0 = APIKeySecurityScheme.from_dict(data)



                    return additional_property_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_1 = HTTPAuthSecurityScheme.from_dict(data)



                    return additional_property_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_2 = OAuth2SecurityScheme.from_dict(data)



                    return additional_property_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_3 = OpenIdConnectSecurityScheme.from_dict(data)



                    return additional_property_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                additional_property_type_4 = MutualTLSSecurityScheme.from_dict(data)



                return additional_property_type_4

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        agent_card_security_schemes_type_0.additional_properties = additional_properties
        return agent_card_security_schemes_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> APIKeySecurityScheme | HTTPAuthSecurityScheme | MutualTLSSecurityScheme | OAuth2SecurityScheme | OpenIdConnectSecurityScheme:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: APIKeySecurityScheme | HTTPAuthSecurityScheme | MutualTLSSecurityScheme | OAuth2SecurityScheme | OpenIdConnectSecurityScheme) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

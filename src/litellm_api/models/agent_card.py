from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.agent_capabilities import AgentCapabilities
  from ..models.agent_card_security_schemes_type_0 import AgentCardSecuritySchemesType0
  from ..models.agent_card_security_type_0_item import AgentCardSecurityType0Item
  from ..models.agent_card_signature import AgentCardSignature
  from ..models.agent_interface import AgentInterface
  from ..models.agent_provider import AgentProvider
  from ..models.agent_skill import AgentSkill





T = TypeVar("T", bound="AgentCard")



@_attrs_define
class AgentCard:
    """ The AgentCard is a self-describing manifest for an agent.
    It provides essential metadata including the agent's identity, capabilities,
    skills, supported communication methods, and security requirements.

        Attributes:
            protocol_version (str | Unset):
            name (str | Unset):
            description (str | Unset):
            url (str | Unset):
            version (str | Unset):
            capabilities (AgentCapabilities | Unset): Defines optional capabilities supported by an agent.
            default_input_modes (list[str] | Unset):
            default_output_modes (list[str] | Unset):
            skills (list[AgentSkill] | Unset):
            preferred_transport (None | str | Unset):
            additional_interfaces (list[AgentInterface] | None | Unset):
            icon_url (None | str | Unset):
            provider (AgentProvider | None | Unset):
            documentation_url (None | str | Unset):
            security_schemes (AgentCardSecuritySchemesType0 | None | Unset):
            security (list[AgentCardSecurityType0Item] | None | Unset):
            supports_authenticated_extended_card (bool | None | Unset):
            signatures (list[AgentCardSignature] | None | Unset):
     """

    protocol_version: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    url: str | Unset = UNSET
    version: str | Unset = UNSET
    capabilities: AgentCapabilities | Unset = UNSET
    default_input_modes: list[str] | Unset = UNSET
    default_output_modes: list[str] | Unset = UNSET
    skills: list[AgentSkill] | Unset = UNSET
    preferred_transport: None | str | Unset = UNSET
    additional_interfaces: list[AgentInterface] | None | Unset = UNSET
    icon_url: None | str | Unset = UNSET
    provider: AgentProvider | None | Unset = UNSET
    documentation_url: None | str | Unset = UNSET
    security_schemes: AgentCardSecuritySchemesType0 | None | Unset = UNSET
    security: list[AgentCardSecurityType0Item] | None | Unset = UNSET
    supports_authenticated_extended_card: bool | None | Unset = UNSET
    signatures: list[AgentCardSignature] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_skill import AgentSkill
        from ..models.agent_provider import AgentProvider
        from ..models.agent_card_signature import AgentCardSignature
        from ..models.agent_card_security_schemes_type_0 import AgentCardSecuritySchemesType0
        from ..models.agent_capabilities import AgentCapabilities
        from ..models.agent_interface import AgentInterface
        from ..models.agent_card_security_type_0_item import AgentCardSecurityType0Item
        protocol_version = self.protocol_version

        name = self.name

        description = self.description

        url = self.url

        version = self.version

        capabilities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities.to_dict()

        default_input_modes: list[str] | Unset = UNSET
        if not isinstance(self.default_input_modes, Unset):
            default_input_modes = self.default_input_modes



        default_output_modes: list[str] | Unset = UNSET
        if not isinstance(self.default_output_modes, Unset):
            default_output_modes = self.default_output_modes



        skills: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skills, Unset):
            skills = []
            for skills_item_data in self.skills:
                skills_item = skills_item_data.to_dict()
                skills.append(skills_item)



        preferred_transport: None | str | Unset
        if isinstance(self.preferred_transport, Unset):
            preferred_transport = UNSET
        else:
            preferred_transport = self.preferred_transport

        additional_interfaces: list[dict[str, Any]] | None | Unset
        if isinstance(self.additional_interfaces, Unset):
            additional_interfaces = UNSET
        elif isinstance(self.additional_interfaces, list):
            additional_interfaces = []
            for additional_interfaces_type_0_item_data in self.additional_interfaces:
                additional_interfaces_type_0_item = additional_interfaces_type_0_item_data.to_dict()
                additional_interfaces.append(additional_interfaces_type_0_item)


        else:
            additional_interfaces = self.additional_interfaces

        icon_url: None | str | Unset
        if isinstance(self.icon_url, Unset):
            icon_url = UNSET
        else:
            icon_url = self.icon_url

        provider: dict[str, Any] | None | Unset
        if isinstance(self.provider, Unset):
            provider = UNSET
        elif isinstance(self.provider, AgentProvider):
            provider = self.provider.to_dict()
        else:
            provider = self.provider

        documentation_url: None | str | Unset
        if isinstance(self.documentation_url, Unset):
            documentation_url = UNSET
        else:
            documentation_url = self.documentation_url

        security_schemes: dict[str, Any] | None | Unset
        if isinstance(self.security_schemes, Unset):
            security_schemes = UNSET
        elif isinstance(self.security_schemes, AgentCardSecuritySchemesType0):
            security_schemes = self.security_schemes.to_dict()
        else:
            security_schemes = self.security_schemes

        security: list[dict[str, Any]] | None | Unset
        if isinstance(self.security, Unset):
            security = UNSET
        elif isinstance(self.security, list):
            security = []
            for security_type_0_item_data in self.security:
                security_type_0_item = security_type_0_item_data.to_dict()
                security.append(security_type_0_item)


        else:
            security = self.security

        supports_authenticated_extended_card: bool | None | Unset
        if isinstance(self.supports_authenticated_extended_card, Unset):
            supports_authenticated_extended_card = UNSET
        else:
            supports_authenticated_extended_card = self.supports_authenticated_extended_card

        signatures: list[dict[str, Any]] | None | Unset
        if isinstance(self.signatures, Unset):
            signatures = UNSET
        elif isinstance(self.signatures, list):
            signatures = []
            for signatures_type_0_item_data in self.signatures:
                signatures_type_0_item = signatures_type_0_item_data.to_dict()
                signatures.append(signatures_type_0_item)


        else:
            signatures = self.signatures


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if protocol_version is not UNSET:
            field_dict["protocolVersion"] = protocol_version
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if url is not UNSET:
            field_dict["url"] = url
        if version is not UNSET:
            field_dict["version"] = version
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if default_input_modes is not UNSET:
            field_dict["defaultInputModes"] = default_input_modes
        if default_output_modes is not UNSET:
            field_dict["defaultOutputModes"] = default_output_modes
        if skills is not UNSET:
            field_dict["skills"] = skills
        if preferred_transport is not UNSET:
            field_dict["preferredTransport"] = preferred_transport
        if additional_interfaces is not UNSET:
            field_dict["additionalInterfaces"] = additional_interfaces
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url
        if provider is not UNSET:
            field_dict["provider"] = provider
        if documentation_url is not UNSET:
            field_dict["documentationUrl"] = documentation_url
        if security_schemes is not UNSET:
            field_dict["securitySchemes"] = security_schemes
        if security is not UNSET:
            field_dict["security"] = security
        if supports_authenticated_extended_card is not UNSET:
            field_dict["supportsAuthenticatedExtendedCard"] = supports_authenticated_extended_card
        if signatures is not UNSET:
            field_dict["signatures"] = signatures

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_capabilities import AgentCapabilities
        from ..models.agent_card_security_schemes_type_0 import AgentCardSecuritySchemesType0
        from ..models.agent_card_security_type_0_item import AgentCardSecurityType0Item
        from ..models.agent_card_signature import AgentCardSignature
        from ..models.agent_interface import AgentInterface
        from ..models.agent_provider import AgentProvider
        from ..models.agent_skill import AgentSkill
        d = dict(src_dict)
        protocol_version = d.pop("protocolVersion", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        url = d.pop("url", UNSET)

        version = d.pop("version", UNSET)

        _capabilities = d.pop("capabilities", UNSET)
        capabilities: AgentCapabilities | Unset
        if isinstance(_capabilities,  Unset):
            capabilities = UNSET
        else:
            capabilities = AgentCapabilities.from_dict(_capabilities)




        default_input_modes = cast(list[str], d.pop("defaultInputModes", UNSET))


        default_output_modes = cast(list[str], d.pop("defaultOutputModes", UNSET))


        _skills = d.pop("skills", UNSET)
        skills: list[AgentSkill] | Unset = UNSET
        if _skills is not UNSET:
            skills = []
            for skills_item_data in _skills:
                skills_item = AgentSkill.from_dict(skills_item_data)



                skills.append(skills_item)


        def _parse_preferred_transport(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preferred_transport = _parse_preferred_transport(d.pop("preferredTransport", UNSET))


        def _parse_additional_interfaces(data: object) -> list[AgentInterface] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                additional_interfaces_type_0 = []
                _additional_interfaces_type_0 = data
                for additional_interfaces_type_0_item_data in (_additional_interfaces_type_0):
                    additional_interfaces_type_0_item = AgentInterface.from_dict(additional_interfaces_type_0_item_data)



                    additional_interfaces_type_0.append(additional_interfaces_type_0_item)

                return additional_interfaces_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AgentInterface] | None | Unset, data)

        additional_interfaces = _parse_additional_interfaces(d.pop("additionalInterfaces", UNSET))


        def _parse_icon_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon_url = _parse_icon_url(d.pop("iconUrl", UNSET))


        def _parse_provider(data: object) -> AgentProvider | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_type_0 = AgentProvider.from_dict(data)



                return provider_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentProvider | None | Unset, data)

        provider = _parse_provider(d.pop("provider", UNSET))


        def _parse_documentation_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        documentation_url = _parse_documentation_url(d.pop("documentationUrl", UNSET))


        def _parse_security_schemes(data: object) -> AgentCardSecuritySchemesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                security_schemes_type_0 = AgentCardSecuritySchemesType0.from_dict(data)



                return security_schemes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentCardSecuritySchemesType0 | None | Unset, data)

        security_schemes = _parse_security_schemes(d.pop("securitySchemes", UNSET))


        def _parse_security(data: object) -> list[AgentCardSecurityType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                security_type_0 = []
                _security_type_0 = data
                for security_type_0_item_data in (_security_type_0):
                    security_type_0_item = AgentCardSecurityType0Item.from_dict(security_type_0_item_data)



                    security_type_0.append(security_type_0_item)

                return security_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AgentCardSecurityType0Item] | None | Unset, data)

        security = _parse_security(d.pop("security", UNSET))


        def _parse_supports_authenticated_extended_card(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        supports_authenticated_extended_card = _parse_supports_authenticated_extended_card(d.pop("supportsAuthenticatedExtendedCard", UNSET))


        def _parse_signatures(data: object) -> list[AgentCardSignature] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                signatures_type_0 = []
                _signatures_type_0 = data
                for signatures_type_0_item_data in (_signatures_type_0):
                    signatures_type_0_item = AgentCardSignature.from_dict(signatures_type_0_item_data)



                    signatures_type_0.append(signatures_type_0_item)

                return signatures_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AgentCardSignature] | None | Unset, data)

        signatures = _parse_signatures(d.pop("signatures", UNSET))


        agent_card = cls(
            protocol_version=protocol_version,
            name=name,
            description=description,
            url=url,
            version=version,
            capabilities=capabilities,
            default_input_modes=default_input_modes,
            default_output_modes=default_output_modes,
            skills=skills,
            preferred_transport=preferred_transport,
            additional_interfaces=additional_interfaces,
            icon_url=icon_url,
            provider=provider,
            documentation_url=documentation_url,
            security_schemes=security_schemes,
            security=security,
            supports_authenticated_extended_card=supports_authenticated_extended_card,
            signatures=signatures,
        )


        agent_card.additional_properties = d
        return agent_card

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

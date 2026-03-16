from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="HashicorpVaultConfig")



@_attrs_define
class HashicorpVaultConfig:
    """ Configuration for Hashicorp Vault secret manager integration.

        Attributes:
            vault_addr (None | str | Unset): The address of the Vault server (e.g., https://vault.example.com:8200)
            vault_token (None | str | Unset): Token for Vault token-based authentication
            approle_role_id (None | str | Unset): Role ID for Vault AppRole authentication
            approle_secret_id (None | str | Unset): Secret ID for Vault AppRole authentication
            approle_mount_path (None | str | Unset): Mount path for the AppRole auth method (default: approle)
            client_cert (None | str | Unset): Path to the client TLS certificate for Vault
            client_key (None | str | Unset): Path to the client TLS private key for Vault
            vault_cert_role (None | str | Unset): Certificate role name for TLS cert authentication
            vault_namespace (None | str | Unset): Vault namespace (for multi-tenant Vault, sent as X-Vault-Namespace header)
            vault_mount_name (None | str | Unset): KV engine mount name (default: secret)
            vault_path_prefix (None | str | Unset): Optional path prefix for secrets (e.g., myapp ->
                secret/data/myapp/{secret_name})
     """

    vault_addr: None | str | Unset = UNSET
    vault_token: None | str | Unset = UNSET
    approle_role_id: None | str | Unset = UNSET
    approle_secret_id: None | str | Unset = UNSET
    approle_mount_path: None | str | Unset = UNSET
    client_cert: None | str | Unset = UNSET
    client_key: None | str | Unset = UNSET
    vault_cert_role: None | str | Unset = UNSET
    vault_namespace: None | str | Unset = UNSET
    vault_mount_name: None | str | Unset = UNSET
    vault_path_prefix: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        vault_addr: None | str | Unset
        if isinstance(self.vault_addr, Unset):
            vault_addr = UNSET
        else:
            vault_addr = self.vault_addr

        vault_token: None | str | Unset
        if isinstance(self.vault_token, Unset):
            vault_token = UNSET
        else:
            vault_token = self.vault_token

        approle_role_id: None | str | Unset
        if isinstance(self.approle_role_id, Unset):
            approle_role_id = UNSET
        else:
            approle_role_id = self.approle_role_id

        approle_secret_id: None | str | Unset
        if isinstance(self.approle_secret_id, Unset):
            approle_secret_id = UNSET
        else:
            approle_secret_id = self.approle_secret_id

        approle_mount_path: None | str | Unset
        if isinstance(self.approle_mount_path, Unset):
            approle_mount_path = UNSET
        else:
            approle_mount_path = self.approle_mount_path

        client_cert: None | str | Unset
        if isinstance(self.client_cert, Unset):
            client_cert = UNSET
        else:
            client_cert = self.client_cert

        client_key: None | str | Unset
        if isinstance(self.client_key, Unset):
            client_key = UNSET
        else:
            client_key = self.client_key

        vault_cert_role: None | str | Unset
        if isinstance(self.vault_cert_role, Unset):
            vault_cert_role = UNSET
        else:
            vault_cert_role = self.vault_cert_role

        vault_namespace: None | str | Unset
        if isinstance(self.vault_namespace, Unset):
            vault_namespace = UNSET
        else:
            vault_namespace = self.vault_namespace

        vault_mount_name: None | str | Unset
        if isinstance(self.vault_mount_name, Unset):
            vault_mount_name = UNSET
        else:
            vault_mount_name = self.vault_mount_name

        vault_path_prefix: None | str | Unset
        if isinstance(self.vault_path_prefix, Unset):
            vault_path_prefix = UNSET
        else:
            vault_path_prefix = self.vault_path_prefix


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if vault_addr is not UNSET:
            field_dict["vault_addr"] = vault_addr
        if vault_token is not UNSET:
            field_dict["vault_token"] = vault_token
        if approle_role_id is not UNSET:
            field_dict["approle_role_id"] = approle_role_id
        if approle_secret_id is not UNSET:
            field_dict["approle_secret_id"] = approle_secret_id
        if approle_mount_path is not UNSET:
            field_dict["approle_mount_path"] = approle_mount_path
        if client_cert is not UNSET:
            field_dict["client_cert"] = client_cert
        if client_key is not UNSET:
            field_dict["client_key"] = client_key
        if vault_cert_role is not UNSET:
            field_dict["vault_cert_role"] = vault_cert_role
        if vault_namespace is not UNSET:
            field_dict["vault_namespace"] = vault_namespace
        if vault_mount_name is not UNSET:
            field_dict["vault_mount_name"] = vault_mount_name
        if vault_path_prefix is not UNSET:
            field_dict["vault_path_prefix"] = vault_path_prefix

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_vault_addr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vault_addr = _parse_vault_addr(d.pop("vault_addr", UNSET))


        def _parse_vault_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vault_token = _parse_vault_token(d.pop("vault_token", UNSET))


        def _parse_approle_role_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        approle_role_id = _parse_approle_role_id(d.pop("approle_role_id", UNSET))


        def _parse_approle_secret_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        approle_secret_id = _parse_approle_secret_id(d.pop("approle_secret_id", UNSET))


        def _parse_approle_mount_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        approle_mount_path = _parse_approle_mount_path(d.pop("approle_mount_path", UNSET))


        def _parse_client_cert(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_cert = _parse_client_cert(d.pop("client_cert", UNSET))


        def _parse_client_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_key = _parse_client_key(d.pop("client_key", UNSET))


        def _parse_vault_cert_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vault_cert_role = _parse_vault_cert_role(d.pop("vault_cert_role", UNSET))


        def _parse_vault_namespace(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vault_namespace = _parse_vault_namespace(d.pop("vault_namespace", UNSET))


        def _parse_vault_mount_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vault_mount_name = _parse_vault_mount_name(d.pop("vault_mount_name", UNSET))


        def _parse_vault_path_prefix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vault_path_prefix = _parse_vault_path_prefix(d.pop("vault_path_prefix", UNSET))


        hashicorp_vault_config = cls(
            vault_addr=vault_addr,
            vault_token=vault_token,
            approle_role_id=approle_role_id,
            approle_secret_id=approle_secret_id,
            approle_mount_path=approle_mount_path,
            client_cert=client_cert,
            client_key=client_key,
            vault_cert_role=vault_cert_role,
            vault_namespace=vault_namespace,
            vault_mount_name=vault_mount_name,
            vault_path_prefix=vault_path_prefix,
        )


        hashicorp_vault_config.additional_properties = d
        return hashicorp_vault_config

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

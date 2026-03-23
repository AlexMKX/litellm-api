from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.worker_registry_entry import WorkerRegistryEntry





T = TypeVar("T", bound="UiDiscoveryEndpoints")



@_attrs_define
class UiDiscoveryEndpoints:
    """ 
        Attributes:
            server_root_path (str):
            proxy_base_url (None | str):
            auto_redirect_to_sso (bool):
            admin_ui_disabled (bool):
            sso_configured (bool):
            is_control_plane (bool | Unset):  Default: False.
            workers (list[WorkerRegistryEntry] | Unset):
     """

    server_root_path: str
    proxy_base_url: None | str
    auto_redirect_to_sso: bool
    admin_ui_disabled: bool
    sso_configured: bool
    is_control_plane: bool | Unset = False
    workers: list[WorkerRegistryEntry] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.worker_registry_entry import WorkerRegistryEntry
        server_root_path = self.server_root_path

        proxy_base_url: None | str
        proxy_base_url = self.proxy_base_url

        auto_redirect_to_sso = self.auto_redirect_to_sso

        admin_ui_disabled = self.admin_ui_disabled

        sso_configured = self.sso_configured

        is_control_plane = self.is_control_plane

        workers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.workers, Unset):
            workers = []
            for workers_item_data in self.workers:
                workers_item = workers_item_data.to_dict()
                workers.append(workers_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "server_root_path": server_root_path,
            "proxy_base_url": proxy_base_url,
            "auto_redirect_to_sso": auto_redirect_to_sso,
            "admin_ui_disabled": admin_ui_disabled,
            "sso_configured": sso_configured,
        })
        if is_control_plane is not UNSET:
            field_dict["is_control_plane"] = is_control_plane
        if workers is not UNSET:
            field_dict["workers"] = workers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.worker_registry_entry import WorkerRegistryEntry
        d = dict(src_dict)
        server_root_path = d.pop("server_root_path")

        def _parse_proxy_base_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        proxy_base_url = _parse_proxy_base_url(d.pop("proxy_base_url"))


        auto_redirect_to_sso = d.pop("auto_redirect_to_sso")

        admin_ui_disabled = d.pop("admin_ui_disabled")

        sso_configured = d.pop("sso_configured")

        is_control_plane = d.pop("is_control_plane", UNSET)

        _workers = d.pop("workers", UNSET)
        workers: list[WorkerRegistryEntry] | Unset = UNSET
        if _workers is not UNSET:
            workers = []
            for workers_item_data in _workers:
                workers_item = WorkerRegistryEntry.from_dict(workers_item_data)



                workers.append(workers_item)


        ui_discovery_endpoints = cls(
            server_root_path=server_root_path,
            proxy_base_url=proxy_base_url,
            auto_redirect_to_sso=auto_redirect_to_sso,
            admin_ui_disabled=admin_ui_disabled,
            sso_configured=sso_configured,
            is_control_plane=is_control_plane,
            workers=workers,
        )


        ui_discovery_endpoints.additional_properties = d
        return ui_discovery_endpoints

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.scim_feature import SCIMFeature
  from ..models.scim_service_provider_config_authentication_schemes_type_0_item import SCIMServiceProviderConfigAuthenticationSchemesType0Item
  from ..models.scim_service_provider_config_meta_type_0 import SCIMServiceProviderConfigMetaType0





T = TypeVar("T", bound="SCIMServiceProviderConfig")



@_attrs_define
class SCIMServiceProviderConfig:
    """ 
        Attributes:
            schemas (list[str] | Unset):
            patch (SCIMFeature | Unset):
            bulk (SCIMFeature | Unset):
            filter_ (SCIMFeature | Unset):
            change_password (SCIMFeature | Unset):
            sort (SCIMFeature | Unset):
            etag (SCIMFeature | Unset):
            authentication_schemes (list[SCIMServiceProviderConfigAuthenticationSchemesType0Item] | None | Unset):
            meta (None | SCIMServiceProviderConfigMetaType0 | Unset):
     """

    schemas: list[str] | Unset = UNSET
    patch: SCIMFeature | Unset = UNSET
    bulk: SCIMFeature | Unset = UNSET
    filter_: SCIMFeature | Unset = UNSET
    change_password: SCIMFeature | Unset = UNSET
    sort: SCIMFeature | Unset = UNSET
    etag: SCIMFeature | Unset = UNSET
    authentication_schemes: list[SCIMServiceProviderConfigAuthenticationSchemesType0Item] | None | Unset = UNSET
    meta: None | SCIMServiceProviderConfigMetaType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.scim_service_provider_config_authentication_schemes_type_0_item import SCIMServiceProviderConfigAuthenticationSchemesType0Item
        from ..models.scim_service_provider_config_meta_type_0 import SCIMServiceProviderConfigMetaType0
        from ..models.scim_feature import SCIMFeature
        schemas: list[str] | Unset = UNSET
        if not isinstance(self.schemas, Unset):
            schemas = self.schemas



        patch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.patch, Unset):
            patch = self.patch.to_dict()

        bulk: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bulk, Unset):
            bulk = self.bulk.to_dict()

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        change_password: dict[str, Any] | Unset = UNSET
        if not isinstance(self.change_password, Unset):
            change_password = self.change_password.to_dict()

        sort: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort.to_dict()

        etag: dict[str, Any] | Unset = UNSET
        if not isinstance(self.etag, Unset):
            etag = self.etag.to_dict()

        authentication_schemes: list[dict[str, Any]] | None | Unset
        if isinstance(self.authentication_schemes, Unset):
            authentication_schemes = UNSET
        elif isinstance(self.authentication_schemes, list):
            authentication_schemes = []
            for authentication_schemes_type_0_item_data in self.authentication_schemes:
                authentication_schemes_type_0_item = authentication_schemes_type_0_item_data.to_dict()
                authentication_schemes.append(authentication_schemes_type_0_item)


        else:
            authentication_schemes = self.authentication_schemes

        meta: dict[str, Any] | None | Unset
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, SCIMServiceProviderConfigMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if schemas is not UNSET:
            field_dict["schemas"] = schemas
        if patch is not UNSET:
            field_dict["patch"] = patch
        if bulk is not UNSET:
            field_dict["bulk"] = bulk
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if change_password is not UNSET:
            field_dict["changePassword"] = change_password
        if sort is not UNSET:
            field_dict["sort"] = sort
        if etag is not UNSET:
            field_dict["etag"] = etag
        if authentication_schemes is not UNSET:
            field_dict["authenticationSchemes"] = authentication_schemes
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scim_feature import SCIMFeature
        from ..models.scim_service_provider_config_authentication_schemes_type_0_item import SCIMServiceProviderConfigAuthenticationSchemesType0Item
        from ..models.scim_service_provider_config_meta_type_0 import SCIMServiceProviderConfigMetaType0
        d = dict(src_dict)
        schemas = cast(list[str], d.pop("schemas", UNSET))


        _patch = d.pop("patch", UNSET)
        patch: SCIMFeature | Unset
        if isinstance(_patch,  Unset):
            patch = UNSET
        else:
            patch = SCIMFeature.from_dict(_patch)




        _bulk = d.pop("bulk", UNSET)
        bulk: SCIMFeature | Unset
        if isinstance(_bulk,  Unset):
            bulk = UNSET
        else:
            bulk = SCIMFeature.from_dict(_bulk)




        _filter_ = d.pop("filter", UNSET)
        filter_: SCIMFeature | Unset
        if isinstance(_filter_,  Unset):
            filter_ = UNSET
        else:
            filter_ = SCIMFeature.from_dict(_filter_)




        _change_password = d.pop("changePassword", UNSET)
        change_password: SCIMFeature | Unset
        if isinstance(_change_password,  Unset):
            change_password = UNSET
        else:
            change_password = SCIMFeature.from_dict(_change_password)




        _sort = d.pop("sort", UNSET)
        sort: SCIMFeature | Unset
        if isinstance(_sort,  Unset):
            sort = UNSET
        else:
            sort = SCIMFeature.from_dict(_sort)




        _etag = d.pop("etag", UNSET)
        etag: SCIMFeature | Unset
        if isinstance(_etag,  Unset):
            etag = UNSET
        else:
            etag = SCIMFeature.from_dict(_etag)




        def _parse_authentication_schemes(data: object) -> list[SCIMServiceProviderConfigAuthenticationSchemesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                authentication_schemes_type_0 = []
                _authentication_schemes_type_0 = data
                for authentication_schemes_type_0_item_data in (_authentication_schemes_type_0):
                    authentication_schemes_type_0_item = SCIMServiceProviderConfigAuthenticationSchemesType0Item.from_dict(authentication_schemes_type_0_item_data)



                    authentication_schemes_type_0.append(authentication_schemes_type_0_item)

                return authentication_schemes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SCIMServiceProviderConfigAuthenticationSchemesType0Item] | None | Unset, data)

        authentication_schemes = _parse_authentication_schemes(d.pop("authenticationSchemes", UNSET))


        def _parse_meta(data: object) -> None | SCIMServiceProviderConfigMetaType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = SCIMServiceProviderConfigMetaType0.from_dict(data)



                return meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SCIMServiceProviderConfigMetaType0 | Unset, data)

        meta = _parse_meta(d.pop("meta", UNSET))


        scim_service_provider_config = cls(
            schemas=schemas,
            patch=patch,
            bulk=bulk,
            filter_=filter_,
            change_password=change_password,
            sort=sort,
            etag=etag,
            authentication_schemes=authentication_schemes,
            meta=meta,
        )


        scim_service_provider_config.additional_properties = d
        return scim_service_provider_config

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

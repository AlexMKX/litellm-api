from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.pass_through_generic_endpoint_guardrails_type_0 import PassThroughGenericEndpointGuardrailsType0
  from ..models.pass_through_generic_endpoint_headers import PassThroughGenericEndpointHeaders





T = TypeVar("T", bound="PassThroughGenericEndpoint")



@_attrs_define
class PassThroughGenericEndpoint:
    """ 
        Attributes:
            path (str): The route to be added to the LiteLLM Proxy Server.
            target (str): The URL to which requests for this path should be forwarded.
            id (None | str | Unset): Optional unique identifier for the pass-through endpoint. If not provided, endpoints
                will be identified by path for backwards compatibility.
            headers (PassThroughGenericEndpointHeaders | Unset): Key-value pairs of headers to be forwarded with the
                request. You can set any key value pair here and it will be forwarded to your target endpoint
            include_subpath (bool | Unset): If True, requests to subpaths of the path will be forwarded to the target
                endpoint. For example, if the path is /bria and include_subpath is True, requests to /bria/v1/text-to-
                image/base/2.3 will be forwarded to the target endpoint. Default: False.
            cost_per_request (float | Unset): The USD cost per request to the target endpoint. This is used to calculate the
                cost of the request to the target endpoint. Default: 0.0.
            auth (bool | Unset): Whether authentication is required for the pass-through endpoint. If True, requests to the
                endpoint will require a valid LiteLLM API key. Default: False.
            guardrails (None | PassThroughGenericEndpointGuardrailsType0 | Unset): Guardrails configuration for this
                passthrough endpoint. Dict keys are guardrail names, values are optional settings for field targeting. When set,
                all org/team/key level guardrails will also execute. Defaults to None (no guardrails execute).
     """

    path: str
    target: str
    id: None | str | Unset = UNSET
    headers: PassThroughGenericEndpointHeaders | Unset = UNSET
    include_subpath: bool | Unset = False
    cost_per_request: float | Unset = 0.0
    auth: bool | Unset = False
    guardrails: None | PassThroughGenericEndpointGuardrailsType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.pass_through_generic_endpoint_guardrails_type_0 import PassThroughGenericEndpointGuardrailsType0
        from ..models.pass_through_generic_endpoint_headers import PassThroughGenericEndpointHeaders
        path = self.path

        target = self.target

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        include_subpath = self.include_subpath

        cost_per_request = self.cost_per_request

        auth = self.auth

        guardrails: dict[str, Any] | None | Unset
        if isinstance(self.guardrails, Unset):
            guardrails = UNSET
        elif isinstance(self.guardrails, PassThroughGenericEndpointGuardrailsType0):
            guardrails = self.guardrails.to_dict()
        else:
            guardrails = self.guardrails


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "path": path,
            "target": target,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if headers is not UNSET:
            field_dict["headers"] = headers
        if include_subpath is not UNSET:
            field_dict["include_subpath"] = include_subpath
        if cost_per_request is not UNSET:
            field_dict["cost_per_request"] = cost_per_request
        if auth is not UNSET:
            field_dict["auth"] = auth
        if guardrails is not UNSET:
            field_dict["guardrails"] = guardrails

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pass_through_generic_endpoint_guardrails_type_0 import PassThroughGenericEndpointGuardrailsType0
        from ..models.pass_through_generic_endpoint_headers import PassThroughGenericEndpointHeaders
        d = dict(src_dict)
        path = d.pop("path")

        target = d.pop("target")

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        _headers = d.pop("headers", UNSET)
        headers: PassThroughGenericEndpointHeaders | Unset
        if isinstance(_headers,  Unset):
            headers = UNSET
        else:
            headers = PassThroughGenericEndpointHeaders.from_dict(_headers)




        include_subpath = d.pop("include_subpath", UNSET)

        cost_per_request = d.pop("cost_per_request", UNSET)

        auth = d.pop("auth", UNSET)

        def _parse_guardrails(data: object) -> None | PassThroughGenericEndpointGuardrailsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                guardrails_type_0 = PassThroughGenericEndpointGuardrailsType0.from_dict(data)



                return guardrails_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PassThroughGenericEndpointGuardrailsType0 | Unset, data)

        guardrails = _parse_guardrails(d.pop("guardrails", UNSET))


        pass_through_generic_endpoint = cls(
            path=path,
            target=target,
            id=id,
            headers=headers,
            include_subpath=include_subpath,
            cost_per_request=cost_per_request,
            auth=auth,
            guardrails=guardrails,
        )


        pass_through_generic_endpoint.additional_properties = d
        return pass_through_generic_endpoint

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

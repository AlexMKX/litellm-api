from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.breakdown_metrics_api_keys import BreakdownMetricsApiKeys
  from ..models.breakdown_metrics_endpoints import BreakdownMetricsEndpoints
  from ..models.breakdown_metrics_entities import BreakdownMetricsEntities
  from ..models.breakdown_metrics_mcp_servers import BreakdownMetricsMcpServers
  from ..models.breakdown_metrics_model_groups import BreakdownMetricsModelGroups
  from ..models.breakdown_metrics_models import BreakdownMetricsModels
  from ..models.breakdown_metrics_providers import BreakdownMetricsProviders





T = TypeVar("T", bound="BreakdownMetrics")



@_attrs_define
class BreakdownMetrics:
    """ Breakdown of spend by different dimensions

        Attributes:
            mcp_servers (BreakdownMetricsMcpServers | Unset):
            models (BreakdownMetricsModels | Unset):
            model_groups (BreakdownMetricsModelGroups | Unset):
            providers (BreakdownMetricsProviders | Unset):
            endpoints (BreakdownMetricsEndpoints | Unset):
            api_keys (BreakdownMetricsApiKeys | Unset):
            entities (BreakdownMetricsEntities | Unset):
     """

    mcp_servers: BreakdownMetricsMcpServers | Unset = UNSET
    models: BreakdownMetricsModels | Unset = UNSET
    model_groups: BreakdownMetricsModelGroups | Unset = UNSET
    providers: BreakdownMetricsProviders | Unset = UNSET
    endpoints: BreakdownMetricsEndpoints | Unset = UNSET
    api_keys: BreakdownMetricsApiKeys | Unset = UNSET
    entities: BreakdownMetricsEntities | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.breakdown_metrics_providers import BreakdownMetricsProviders
        from ..models.breakdown_metrics_entities import BreakdownMetricsEntities
        from ..models.breakdown_metrics_model_groups import BreakdownMetricsModelGroups
        from ..models.breakdown_metrics_models import BreakdownMetricsModels
        from ..models.breakdown_metrics_endpoints import BreakdownMetricsEndpoints
        from ..models.breakdown_metrics_api_keys import BreakdownMetricsApiKeys
        from ..models.breakdown_metrics_mcp_servers import BreakdownMetricsMcpServers
        mcp_servers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mcp_servers, Unset):
            mcp_servers = self.mcp_servers.to_dict()

        models: dict[str, Any] | Unset = UNSET
        if not isinstance(self.models, Unset):
            models = self.models.to_dict()

        model_groups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.model_groups, Unset):
            model_groups = self.model_groups.to_dict()

        providers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.providers, Unset):
            providers = self.providers.to_dict()

        endpoints: dict[str, Any] | Unset = UNSET
        if not isinstance(self.endpoints, Unset):
            endpoints = self.endpoints.to_dict()

        api_keys: dict[str, Any] | Unset = UNSET
        if not isinstance(self.api_keys, Unset):
            api_keys = self.api_keys.to_dict()

        entities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entities, Unset):
            entities = self.entities.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if mcp_servers is not UNSET:
            field_dict["mcp_servers"] = mcp_servers
        if models is not UNSET:
            field_dict["models"] = models
        if model_groups is not UNSET:
            field_dict["model_groups"] = model_groups
        if providers is not UNSET:
            field_dict["providers"] = providers
        if endpoints is not UNSET:
            field_dict["endpoints"] = endpoints
        if api_keys is not UNSET:
            field_dict["api_keys"] = api_keys
        if entities is not UNSET:
            field_dict["entities"] = entities

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.breakdown_metrics_api_keys import BreakdownMetricsApiKeys
        from ..models.breakdown_metrics_endpoints import BreakdownMetricsEndpoints
        from ..models.breakdown_metrics_entities import BreakdownMetricsEntities
        from ..models.breakdown_metrics_mcp_servers import BreakdownMetricsMcpServers
        from ..models.breakdown_metrics_model_groups import BreakdownMetricsModelGroups
        from ..models.breakdown_metrics_models import BreakdownMetricsModels
        from ..models.breakdown_metrics_providers import BreakdownMetricsProviders
        d = dict(src_dict)
        _mcp_servers = d.pop("mcp_servers", UNSET)
        mcp_servers: BreakdownMetricsMcpServers | Unset
        if isinstance(_mcp_servers,  Unset):
            mcp_servers = UNSET
        else:
            mcp_servers = BreakdownMetricsMcpServers.from_dict(_mcp_servers)




        _models = d.pop("models", UNSET)
        models: BreakdownMetricsModels | Unset
        if isinstance(_models,  Unset):
            models = UNSET
        else:
            models = BreakdownMetricsModels.from_dict(_models)




        _model_groups = d.pop("model_groups", UNSET)
        model_groups: BreakdownMetricsModelGroups | Unset
        if isinstance(_model_groups,  Unset):
            model_groups = UNSET
        else:
            model_groups = BreakdownMetricsModelGroups.from_dict(_model_groups)




        _providers = d.pop("providers", UNSET)
        providers: BreakdownMetricsProviders | Unset
        if isinstance(_providers,  Unset):
            providers = UNSET
        else:
            providers = BreakdownMetricsProviders.from_dict(_providers)




        _endpoints = d.pop("endpoints", UNSET)
        endpoints: BreakdownMetricsEndpoints | Unset
        if isinstance(_endpoints,  Unset):
            endpoints = UNSET
        else:
            endpoints = BreakdownMetricsEndpoints.from_dict(_endpoints)




        _api_keys = d.pop("api_keys", UNSET)
        api_keys: BreakdownMetricsApiKeys | Unset
        if isinstance(_api_keys,  Unset):
            api_keys = UNSET
        else:
            api_keys = BreakdownMetricsApiKeys.from_dict(_api_keys)




        _entities = d.pop("entities", UNSET)
        entities: BreakdownMetricsEntities | Unset
        if isinstance(_entities,  Unset):
            entities = UNSET
        else:
            entities = BreakdownMetricsEntities.from_dict(_entities)




        breakdown_metrics = cls(
            mcp_servers=mcp_servers,
            models=models,
            model_groups=model_groups,
            providers=providers,
            endpoints=endpoints,
            api_keys=api_keys,
            entities=entities,
        )


        breakdown_metrics.additional_properties = d
        return breakdown_metrics

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.routing_group_routing_strategy_args_type_0 import RoutingGroupRoutingStrategyArgsType0





T = TypeVar("T", bound="RoutingGroup")



@_attrs_define
class RoutingGroup:
    """ A group of models that share a routing strategy.

        Attributes:
            group_name (str):
            models (list[str]):
            routing_strategy (str):
            routing_strategy_args (None | RoutingGroupRoutingStrategyArgsType0 | Unset):
     """

    group_name: str
    models: list[str]
    routing_strategy: str
    routing_strategy_args: None | RoutingGroupRoutingStrategyArgsType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.routing_group_routing_strategy_args_type_0 import RoutingGroupRoutingStrategyArgsType0
        group_name = self.group_name

        models = self.models



        routing_strategy = self.routing_strategy

        routing_strategy_args: dict[str, Any] | None | Unset
        if isinstance(self.routing_strategy_args, Unset):
            routing_strategy_args = UNSET
        elif isinstance(self.routing_strategy_args, RoutingGroupRoutingStrategyArgsType0):
            routing_strategy_args = self.routing_strategy_args.to_dict()
        else:
            routing_strategy_args = self.routing_strategy_args


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "group_name": group_name,
            "models": models,
            "routing_strategy": routing_strategy,
        })
        if routing_strategy_args is not UNSET:
            field_dict["routing_strategy_args"] = routing_strategy_args

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.routing_group_routing_strategy_args_type_0 import RoutingGroupRoutingStrategyArgsType0
        d = dict(src_dict)
        group_name = d.pop("group_name")

        models = cast(list[str], d.pop("models"))


        routing_strategy = d.pop("routing_strategy")

        def _parse_routing_strategy_args(data: object) -> None | RoutingGroupRoutingStrategyArgsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                routing_strategy_args_type_0 = RoutingGroupRoutingStrategyArgsType0.from_dict(data)



                return routing_strategy_args_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RoutingGroupRoutingStrategyArgsType0 | Unset, data)

        routing_strategy_args = _parse_routing_strategy_args(d.pop("routing_strategy_args", UNSET))


        routing_group = cls(
            group_name=group_name,
            models=models,
            routing_strategy=routing_strategy,
            routing_strategy_args=routing_strategy_args,
        )


        routing_group.additional_properties = d
        return routing_group

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

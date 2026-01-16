from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Hyperparameters")



@_attrs_define
class Hyperparameters:
    """ 
        Attributes:
            batch_size (int | None | str | Unset):
            learning_rate_multiplier (float | None | str | Unset):
            n_epochs (int | None | str | Unset):
     """

    batch_size: int | None | str | Unset = UNSET
    learning_rate_multiplier: float | None | str | Unset = UNSET
    n_epochs: int | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        batch_size: int | None | str | Unset
        if isinstance(self.batch_size, Unset):
            batch_size = UNSET
        else:
            batch_size = self.batch_size

        learning_rate_multiplier: float | None | str | Unset
        if isinstance(self.learning_rate_multiplier, Unset):
            learning_rate_multiplier = UNSET
        else:
            learning_rate_multiplier = self.learning_rate_multiplier

        n_epochs: int | None | str | Unset
        if isinstance(self.n_epochs, Unset):
            n_epochs = UNSET
        else:
            n_epochs = self.n_epochs


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if batch_size is not UNSET:
            field_dict["batch_size"] = batch_size
        if learning_rate_multiplier is not UNSET:
            field_dict["learning_rate_multiplier"] = learning_rate_multiplier
        if n_epochs is not UNSET:
            field_dict["n_epochs"] = n_epochs

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_batch_size(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        batch_size = _parse_batch_size(d.pop("batch_size", UNSET))


        def _parse_learning_rate_multiplier(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        learning_rate_multiplier = _parse_learning_rate_multiplier(d.pop("learning_rate_multiplier", UNSET))


        def _parse_n_epochs(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        n_epochs = _parse_n_epochs(d.pop("n_epochs", UNSET))


        hyperparameters = cls(
            batch_size=batch_size,
            learning_rate_multiplier=learning_rate_multiplier,
            n_epochs=n_epochs,
        )


        hyperparameters.additional_properties = d
        return hyperparameters

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

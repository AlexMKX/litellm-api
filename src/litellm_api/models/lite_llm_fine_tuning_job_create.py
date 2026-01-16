from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.lite_llm_fine_tuning_job_create_custom_llm_provider_type_0 import LiteLLMFineTuningJobCreateCustomLlmProviderType0
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.hyperparameters import Hyperparameters





T = TypeVar("T", bound="LiteLLMFineTuningJobCreate")



@_attrs_define
class LiteLLMFineTuningJobCreate:
    """ 
        Attributes:
            model (str):
            training_file (str):
            hyperparameters (Hyperparameters | None | Unset):
            suffix (None | str | Unset):
            validation_file (None | str | Unset):
            integrations (list[str] | None | Unset):
            seed (int | None | Unset):
            custom_llm_provider (LiteLLMFineTuningJobCreateCustomLlmProviderType0 | None | Unset):
     """

    model: str
    training_file: str
    hyperparameters: Hyperparameters | None | Unset = UNSET
    suffix: None | str | Unset = UNSET
    validation_file: None | str | Unset = UNSET
    integrations: list[str] | None | Unset = UNSET
    seed: int | None | Unset = UNSET
    custom_llm_provider: LiteLLMFineTuningJobCreateCustomLlmProviderType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.hyperparameters import Hyperparameters
        model = self.model

        training_file = self.training_file

        hyperparameters: dict[str, Any] | None | Unset
        if isinstance(self.hyperparameters, Unset):
            hyperparameters = UNSET
        elif isinstance(self.hyperparameters, Hyperparameters):
            hyperparameters = self.hyperparameters.to_dict()
        else:
            hyperparameters = self.hyperparameters

        suffix: None | str | Unset
        if isinstance(self.suffix, Unset):
            suffix = UNSET
        else:
            suffix = self.suffix

        validation_file: None | str | Unset
        if isinstance(self.validation_file, Unset):
            validation_file = UNSET
        else:
            validation_file = self.validation_file

        integrations: list[str] | None | Unset
        if isinstance(self.integrations, Unset):
            integrations = UNSET
        elif isinstance(self.integrations, list):
            integrations = self.integrations


        else:
            integrations = self.integrations

        seed: int | None | Unset
        if isinstance(self.seed, Unset):
            seed = UNSET
        else:
            seed = self.seed

        custom_llm_provider: None | str | Unset
        if isinstance(self.custom_llm_provider, Unset):
            custom_llm_provider = UNSET
        elif isinstance(self.custom_llm_provider, LiteLLMFineTuningJobCreateCustomLlmProviderType0):
            custom_llm_provider = self.custom_llm_provider.value
        else:
            custom_llm_provider = self.custom_llm_provider


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "model": model,
            "training_file": training_file,
        })
        if hyperparameters is not UNSET:
            field_dict["hyperparameters"] = hyperparameters
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if validation_file is not UNSET:
            field_dict["validation_file"] = validation_file
        if integrations is not UNSET:
            field_dict["integrations"] = integrations
        if seed is not UNSET:
            field_dict["seed"] = seed
        if custom_llm_provider is not UNSET:
            field_dict["custom_llm_provider"] = custom_llm_provider

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hyperparameters import Hyperparameters
        d = dict(src_dict)
        model = d.pop("model")

        training_file = d.pop("training_file")

        def _parse_hyperparameters(data: object) -> Hyperparameters | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                hyperparameters_type_0 = Hyperparameters.from_dict(data)



                return hyperparameters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Hyperparameters | None | Unset, data)

        hyperparameters = _parse_hyperparameters(d.pop("hyperparameters", UNSET))


        def _parse_suffix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        suffix = _parse_suffix(d.pop("suffix", UNSET))


        def _parse_validation_file(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        validation_file = _parse_validation_file(d.pop("validation_file", UNSET))


        def _parse_integrations(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                integrations_type_0 = cast(list[str], data)

                return integrations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        integrations = _parse_integrations(d.pop("integrations", UNSET))


        def _parse_seed(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        seed = _parse_seed(d.pop("seed", UNSET))


        def _parse_custom_llm_provider(data: object) -> LiteLLMFineTuningJobCreateCustomLlmProviderType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                custom_llm_provider_type_0 = LiteLLMFineTuningJobCreateCustomLlmProviderType0(data)



                return custom_llm_provider_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMFineTuningJobCreateCustomLlmProviderType0 | None | Unset, data)

        custom_llm_provider = _parse_custom_llm_provider(d.pop("custom_llm_provider", UNSET))


        lite_llm_fine_tuning_job_create = cls(
            model=model,
            training_file=training_file,
            hyperparameters=hyperparameters,
            suffix=suffix,
            validation_file=validation_file,
            integrations=integrations,
            seed=seed,
            custom_llm_provider=custom_llm_provider,
        )


        lite_llm_fine_tuning_job_create.additional_properties = d
        return lite_llm_fine_tuning_job_create

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

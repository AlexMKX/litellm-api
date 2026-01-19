from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.embeddings_embeddings_post_body_custom_llm_provider_type_1 import EmbeddingsEmbeddingsPostBodyCustomLlmProviderType1
  from ..models.embeddings_embeddings_post_body_litellm_logging_obj_type_0 import EmbeddingsEmbeddingsPostBodyLitellmLoggingObjType0





T = TypeVar("T", bound="EmbeddingsEmbeddingsPostBody")



@_attrs_define
class EmbeddingsEmbeddingsPostBody:
    """ 
        Attributes:
            model (str):
            input_ (list[str] | Unset):
            timeout (int | Unset):  Default: 600.
            api_base (None | str | Unset):
            api_version (None | str | Unset):
            api_key (None | str | Unset):
            api_type (None | str | Unset):
            caching (bool | Unset):  Default: False.
            user (None | str | Unset):
            custom_llm_provider (EmbeddingsEmbeddingsPostBodyCustomLlmProviderType1 | None | str | Unset):
            litellm_call_id (None | str | Unset):
            litellm_logging_obj (EmbeddingsEmbeddingsPostBodyLitellmLoggingObjType0 | None | Unset):
            logger_fn (None | str | Unset):
     """

    model: str
    input_: list[str] | Unset = UNSET
    timeout: int | Unset = 600
    api_base: None | str | Unset = UNSET
    api_version: None | str | Unset = UNSET
    api_key: None | str | Unset = UNSET
    api_type: None | str | Unset = UNSET
    caching: bool | Unset = False
    user: None | str | Unset = UNSET
    custom_llm_provider: EmbeddingsEmbeddingsPostBodyCustomLlmProviderType1 | None | str | Unset = UNSET
    litellm_call_id: None | str | Unset = UNSET
    litellm_logging_obj: EmbeddingsEmbeddingsPostBodyLitellmLoggingObjType0 | None | Unset = UNSET
    logger_fn: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.embeddings_embeddings_post_body_custom_llm_provider_type_1 import EmbeddingsEmbeddingsPostBodyCustomLlmProviderType1
        from ..models.embeddings_embeddings_post_body_litellm_logging_obj_type_0 import EmbeddingsEmbeddingsPostBodyLitellmLoggingObjType0
        model = self.model

        input_: list[str] | Unset = UNSET
        if not isinstance(self.input_, Unset):
            input_ = self.input_



        timeout = self.timeout

        api_base: None | str | Unset
        if isinstance(self.api_base, Unset):
            api_base = UNSET
        else:
            api_base = self.api_base

        api_version: None | str | Unset
        if isinstance(self.api_version, Unset):
            api_version = UNSET
        else:
            api_version = self.api_version

        api_key: None | str | Unset
        if isinstance(self.api_key, Unset):
            api_key = UNSET
        else:
            api_key = self.api_key

        api_type: None | str | Unset
        if isinstance(self.api_type, Unset):
            api_type = UNSET
        else:
            api_type = self.api_type

        caching = self.caching

        user: None | str | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        else:
            user = self.user

        custom_llm_provider: dict[str, Any] | None | str | Unset
        if isinstance(self.custom_llm_provider, Unset):
            custom_llm_provider = UNSET
        elif isinstance(self.custom_llm_provider, EmbeddingsEmbeddingsPostBodyCustomLlmProviderType1):
            custom_llm_provider = self.custom_llm_provider.to_dict()
        else:
            custom_llm_provider = self.custom_llm_provider

        litellm_call_id: None | str | Unset
        if isinstance(self.litellm_call_id, Unset):
            litellm_call_id = UNSET
        else:
            litellm_call_id = self.litellm_call_id

        litellm_logging_obj: dict[str, Any] | None | Unset
        if isinstance(self.litellm_logging_obj, Unset):
            litellm_logging_obj = UNSET
        elif isinstance(self.litellm_logging_obj, EmbeddingsEmbeddingsPostBodyLitellmLoggingObjType0):
            litellm_logging_obj = self.litellm_logging_obj.to_dict()
        else:
            litellm_logging_obj = self.litellm_logging_obj

        logger_fn: None | str | Unset
        if isinstance(self.logger_fn, Unset):
            logger_fn = UNSET
        else:
            logger_fn = self.logger_fn


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "model": model,
        })
        if input_ is not UNSET:
            field_dict["input"] = input_
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if api_base is not UNSET:
            field_dict["api_base"] = api_base
        if api_version is not UNSET:
            field_dict["api_version"] = api_version
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if api_type is not UNSET:
            field_dict["api_type"] = api_type
        if caching is not UNSET:
            field_dict["caching"] = caching
        if user is not UNSET:
            field_dict["user"] = user
        if custom_llm_provider is not UNSET:
            field_dict["custom_llm_provider"] = custom_llm_provider
        if litellm_call_id is not UNSET:
            field_dict["litellm_call_id"] = litellm_call_id
        if litellm_logging_obj is not UNSET:
            field_dict["litellm_logging_obj"] = litellm_logging_obj
        if logger_fn is not UNSET:
            field_dict["logger_fn"] = logger_fn

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embeddings_embeddings_post_body_custom_llm_provider_type_1 import EmbeddingsEmbeddingsPostBodyCustomLlmProviderType1
        from ..models.embeddings_embeddings_post_body_litellm_logging_obj_type_0 import EmbeddingsEmbeddingsPostBodyLitellmLoggingObjType0
        d = dict(src_dict)
        model = d.pop("model")

        input_ = cast(list[str], d.pop("input", UNSET))


        timeout = d.pop("timeout", UNSET)

        def _parse_api_base(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_base = _parse_api_base(d.pop("api_base", UNSET))


        def _parse_api_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_version = _parse_api_version(d.pop("api_version", UNSET))


        def _parse_api_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_key = _parse_api_key(d.pop("api_key", UNSET))


        def _parse_api_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_type = _parse_api_type(d.pop("api_type", UNSET))


        caching = d.pop("caching", UNSET)

        def _parse_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user = _parse_user(d.pop("user", UNSET))


        def _parse_custom_llm_provider(data: object) -> EmbeddingsEmbeddingsPostBodyCustomLlmProviderType1 | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_llm_provider_type_1 = EmbeddingsEmbeddingsPostBodyCustomLlmProviderType1.from_dict(data)



                return custom_llm_provider_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EmbeddingsEmbeddingsPostBodyCustomLlmProviderType1 | None | str | Unset, data)

        custom_llm_provider = _parse_custom_llm_provider(d.pop("custom_llm_provider", UNSET))


        def _parse_litellm_call_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        litellm_call_id = _parse_litellm_call_id(d.pop("litellm_call_id", UNSET))


        def _parse_litellm_logging_obj(data: object) -> EmbeddingsEmbeddingsPostBodyLitellmLoggingObjType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                litellm_logging_obj_type_0 = EmbeddingsEmbeddingsPostBodyLitellmLoggingObjType0.from_dict(data)



                return litellm_logging_obj_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EmbeddingsEmbeddingsPostBodyLitellmLoggingObjType0 | None | Unset, data)

        litellm_logging_obj = _parse_litellm_logging_obj(d.pop("litellm_logging_obj", UNSET))


        def _parse_logger_fn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logger_fn = _parse_logger_fn(d.pop("logger_fn", UNSET))


        embeddings_embeddings_post_body = cls(
            model=model,
            input_=input_,
            timeout=timeout,
            api_base=api_base,
            api_version=api_version,
            api_key=api_key,
            api_type=api_type,
            caching=caching,
            user=user,
            custom_llm_provider=custom_llm_provider,
            litellm_call_id=litellm_call_id,
            litellm_logging_obj=litellm_logging_obj,
            logger_fn=logger_fn,
        )


        embeddings_embeddings_post_body.additional_properties = d
        return embeddings_embeddings_post_body

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

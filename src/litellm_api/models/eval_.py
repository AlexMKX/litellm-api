from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.eval_data_source_config import EvalDataSourceConfig
  from ..models.eval_metadata_type_0 import EvalMetadataType0
  from ..models.eval_testing_criteria_item import EvalTestingCriteriaItem





T = TypeVar("T", bound="Eval")



@_attrs_define
class Eval:
    """ Represents an evaluation from the OpenAI Evals API

        Attributes:
            id (str):
            created_at (int):
            data_source_config (EvalDataSourceConfig):
            testing_criteria (list[EvalTestingCriteriaItem]):
            object_ (str | Unset):  Default: 'eval'.
            updated_at (int | None | Unset):
            name (None | str | Unset):
            metadata (EvalMetadataType0 | None | Unset):
     """

    id: str
    created_at: int
    data_source_config: EvalDataSourceConfig
    testing_criteria: list[EvalTestingCriteriaItem]
    object_: str | Unset = 'eval'
    updated_at: int | None | Unset = UNSET
    name: None | str | Unset = UNSET
    metadata: EvalMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.eval_metadata_type_0 import EvalMetadataType0
        from ..models.eval_data_source_config import EvalDataSourceConfig
        from ..models.eval_testing_criteria_item import EvalTestingCriteriaItem
        id = self.id

        created_at = self.created_at

        data_source_config = self.data_source_config.to_dict()

        testing_criteria = []
        for testing_criteria_item_data in self.testing_criteria:
            testing_criteria_item = testing_criteria_item_data.to_dict()
            testing_criteria.append(testing_criteria_item)



        object_ = self.object_

        updated_at: int | None | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = self.updated_at

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, EvalMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "created_at": created_at,
            "data_source_config": data_source_config,
            "testing_criteria": testing_criteria,
        })
        if object_ is not UNSET:
            field_dict["object"] = object_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if name is not UNSET:
            field_dict["name"] = name
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eval_data_source_config import EvalDataSourceConfig
        from ..models.eval_metadata_type_0 import EvalMetadataType0
        from ..models.eval_testing_criteria_item import EvalTestingCriteriaItem
        d = dict(src_dict)
        id = d.pop("id")

        created_at = d.pop("created_at")

        data_source_config = EvalDataSourceConfig.from_dict(d.pop("data_source_config"))




        testing_criteria = []
        _testing_criteria = d.pop("testing_criteria")
        for testing_criteria_item_data in (_testing_criteria):
            testing_criteria_item = EvalTestingCriteriaItem.from_dict(testing_criteria_item_data)



            testing_criteria.append(testing_criteria_item)


        object_ = d.pop("object", UNSET)

        def _parse_updated_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_metadata(data: object) -> EvalMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = EvalMetadataType0.from_dict(data)



                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EvalMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


        eval_ = cls(
            id=id,
            created_at=created_at,
            data_source_config=data_source_config,
            testing_criteria=testing_criteria,
            object_=object_,
            updated_at=updated_at,
            name=name,
            metadata=metadata,
        )


        eval_.additional_properties = d
        return eval_

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

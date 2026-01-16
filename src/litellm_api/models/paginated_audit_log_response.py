from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.audit_log_response import AuditLogResponse





T = TypeVar("T", bound="PaginatedAuditLogResponse")



@_attrs_define
class PaginatedAuditLogResponse:
    """ Response model for paginated audit logs

        Attributes:
            audit_logs (list[AuditLogResponse]):
            total (int): Total number of audit logs matching the filters
            page (int): Current page number
            page_size (int): Number of items per page
            total_pages (int): Total number of pages
     """

    audit_logs: list[AuditLogResponse]
    total: int
    page: int
    page_size: int
    total_pages: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.audit_log_response import AuditLogResponse
        audit_logs = []
        for audit_logs_item_data in self.audit_logs:
            audit_logs_item = audit_logs_item_data.to_dict()
            audit_logs.append(audit_logs_item)



        total = self.total

        page = self.page

        page_size = self.page_size

        total_pages = self.total_pages


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "audit_logs": audit_logs,
            "total": total,
            "page": page,
            "page_size": page_size,
            "total_pages": total_pages,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_log_response import AuditLogResponse
        d = dict(src_dict)
        audit_logs = []
        _audit_logs = d.pop("audit_logs")
        for audit_logs_item_data in (_audit_logs):
            audit_logs_item = AuditLogResponse.from_dict(audit_logs_item_data)



            audit_logs.append(audit_logs_item)


        total = d.pop("total")

        page = d.pop("page")

        page_size = d.pop("page_size")

        total_pages = d.pop("total_pages")

        paginated_audit_log_response = cls(
            audit_logs=audit_logs,
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages,
        )


        paginated_audit_log_response.additional_properties = d
        return paginated_audit_log_response

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

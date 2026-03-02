from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.blog_post import BlogPost





T = TypeVar("T", bound="BlogPostsResponse")



@_attrs_define
class BlogPostsResponse:
    """ 
        Attributes:
            posts (list[BlogPost]):
     """

    posts: list[BlogPost]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.blog_post import BlogPost
        posts = []
        for posts_item_data in self.posts:
            posts_item = posts_item_data.to_dict()
            posts.append(posts_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "posts": posts,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.blog_post import BlogPost
        d = dict(src_dict)
        posts = []
        _posts = d.pop("posts")
        for posts_item_data in (_posts):
            posts_item = BlogPost.from_dict(posts_item_data)



            posts.append(posts_item)


        blog_posts_response = cls(
            posts=posts,
        )


        blog_posts_response.additional_properties = d
        return blog_posts_response

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

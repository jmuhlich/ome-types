from ome_types._autogenerated.ome_2016_06.boolean_annotation import (
    BooleanAnnotation,
)
from ome_types._autogenerated.ome_2016_06.comment_annotation import (
    CommentAnnotation,
)
from ome_types._autogenerated.ome_2016_06.double_annotation import (
    DoubleAnnotation,
)
from ome_types._autogenerated.ome_2016_06.file_annotation import FileAnnotation
from ome_types._autogenerated.ome_2016_06.list_annotation import ListAnnotation
from ome_types._autogenerated.ome_2016_06.long_annotation import LongAnnotation
from ome_types._autogenerated.ome_2016_06.map_annotation import MapAnnotation
from ome_types._autogenerated.ome_2016_06.tag_annotation import TagAnnotation
from ome_types._autogenerated.ome_2016_06.term_annotation import TermAnnotation
from ome_types._autogenerated.ome_2016_06.timestamp_annotation import (
    TimestampAnnotation,
)
from ome_types._autogenerated.ome_2016_06.xml_annotation import XMLAnnotation
from ome_types._mixins._base_type import OMEType
from ome_types._mixins._collections import StructuredAnnotationsMixin
from xsdata_pydantic_basemodel.pydantic_compat import Field

__NAMESPACE__ = "http://www.openmicroscopy.org/Schemas/OME/2016-06"


class StructuredAnnotations(StructuredAnnotationsMixin, OMEType):
    """
    An unordered collection of annotation attached to objects in the OME data
    model.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    xml_annotations: list[XMLAnnotation] = Field(
        default_factory=list,
        metadata={
            "name": "XMLAnnotation",
            "type": "Element",
        },
    )
    file_annotations: list[FileAnnotation] = Field(
        default_factory=list,
        metadata={
            "name": "FileAnnotation",
            "type": "Element",
        },
    )
    list_annotations: list[ListAnnotation] = Field(
        default_factory=list,
        metadata={
            "name": "ListAnnotation",
            "type": "Element",
        },
    )
    long_annotations: list[LongAnnotation] = Field(
        default_factory=list,
        metadata={
            "name": "LongAnnotation",
            "type": "Element",
        },
    )
    double_annotations: list[DoubleAnnotation] = Field(
        default_factory=list,
        metadata={
            "name": "DoubleAnnotation",
            "type": "Element",
        },
    )
    comment_annotations: list[CommentAnnotation] = Field(
        default_factory=list,
        metadata={
            "name": "CommentAnnotation",
            "type": "Element",
        },
    )
    boolean_annotations: list[BooleanAnnotation] = Field(
        default_factory=list,
        metadata={
            "name": "BooleanAnnotation",
            "type": "Element",
        },
    )
    timestamp_annotations: list[TimestampAnnotation] = Field(
        default_factory=list,
        metadata={
            "name": "TimestampAnnotation",
            "type": "Element",
        },
    )
    tag_annotations: list[TagAnnotation] = Field(
        default_factory=list,
        metadata={
            "name": "TagAnnotation",
            "type": "Element",
        },
    )
    term_annotations: list[TermAnnotation] = Field(
        default_factory=list,
        metadata={
            "name": "TermAnnotation",
            "type": "Element",
        },
    )
    map_annotations: list[MapAnnotation] = Field(
        default_factory=list,
        metadata={
            "name": "MapAnnotation",
            "type": "Element",
        },
    )
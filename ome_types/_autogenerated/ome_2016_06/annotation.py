from typing import Optional

from ome_types._autogenerated.ome_2016_06.annotation_ref import AnnotationRef
from ome_types._mixins._base_type import OMEType
from ome_types._mixins._kinded import KindMixin
from xsdata_pydantic_basemodel.pydantic_compat import Field

__NAMESPACE__ = "http://www.openmicroscopy.org/Schemas/OME/2016-06"


class Annotation(KindMixin, OMEType):
    """
    An annotation from which all others are ultimately derived.

    Attributes
    ----------
    description : None | str
        A description for the annotation. [plain-text multi-line string]
    annotation_refs : list[AnnotationRef]
        (The Annotation AnnotationRefs).
    id : str
        (The Annotation ID).
    namespace : None | str
        We recommend the inclusion of a namespace for annotations you define. If it
        is absent then we assume the annotation is to use our (OME's) default
        interpretation for this type.
    annotator : None | str
        The Annotator is the person who attached this annotation. e.g. If UserA
        annotates something with TagB, owned by UserB, UserA is still the
        Annotator.
    """

    description: Optional[str] = Field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.openmicroscopy.org/Schemas/OME/2016-06",
            "white_space": "preserve",
        },
    )
    annotation_refs: list[AnnotationRef] = Field(
        default_factory=list,
        metadata={
            "name": "AnnotationRef",
            "type": "Element",
            "namespace": "http://www.openmicroscopy.org/Schemas/OME/2016-06",
        },
    )
    id: str = Field(
        default="__auto_sequence__",
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Annotation:\S+)|(Annotation:\S+)",
        },
        regex="(urn:lsid:([\\w\\-\\.]+\\.[\\w\\-\\.]+)+:Annotation:\\S+)|(Annotation:\\S+)",
    )
    namespace: Optional[str] = Field(
        default=None,
        metadata={
            "name": "Namespace",
            "type": "Attribute",
        },
    )
    annotator: Optional[str] = Field(
        default=None,
        metadata={
            "name": "Annotator",
            "type": "Attribute",
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Experimenter:\S+)|(Experimenter:\S+)",
        },
        regex="(urn:lsid:([\\w\\-\\.]+\\.[\\w\\-\\.]+)+:Experimenter:\\S+)|(Experimenter:\\S+)",
    )
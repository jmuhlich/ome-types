from ome_types._autogenerated.ome_2016_06.reference import Reference
from xsdata_pydantic_basemodel.pydantic_compat import Field

__NAMESPACE__ = "http://www.openmicroscopy.org/Schemas/OME/2016-06"


class FilterSetRef(Reference):
    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    id: str = Field(
        default="__auto_sequence__",
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:FilterSet:\S+)|(FilterSet:\S+)",
        },
        regex="(urn:lsid:([\\w\\-\\.]+\\.[\\w\\-\\.]+)+:FilterSet:\\S+)|(FilterSet:\\S+)",
    )
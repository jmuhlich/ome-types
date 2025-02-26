from ome_types._autogenerated.ome_2016_06.annotation import Annotation

__NAMESPACE__ = "http://www.openmicroscopy.org/Schemas/OME/2016-06"


class ListAnnotation(Annotation):
    """This annotation is a grouping object.

    It uses the sequence of annotation refs from the base Annotation to
    form the list.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

from typing import Optional

from ome_types._autogenerated.ome_2016_06.laser_laser_medium import (
    Laser_LaserMedium,
)
from ome_types._autogenerated.ome_2016_06.laser_pulse import Laser_Pulse
from ome_types._autogenerated.ome_2016_06.laser_type import Laser_Type
from ome_types._autogenerated.ome_2016_06.light_source import LightSource
from ome_types._autogenerated.ome_2016_06.pump import Pump
from ome_types._autogenerated.ome_2016_06.units_frequency import UnitsFrequency
from ome_types._autogenerated.ome_2016_06.units_length import UnitsLength
from xsdata_pydantic_basemodel.pydantic_compat import Field

__NAMESPACE__ = "http://www.openmicroscopy.org/Schemas/OME/2016-06"


class Laser(LightSource):
    """Laser types are specified using two attributes - the Type and the LaserMedium.

    Attributes
    ----------
    pump : None | Pump
        The Laser element may contain a Pump sub-element which refers to a
        LightSource used as a laser pump.
    type : None | Laser_Type
        Type is the general category of laser.
    laser_medium : None | Laser_LaserMedium
        The Medium attribute specifies the actual lasing medium for a given laser
        type.
    wavelength : None | float
        The Wavelength of the laser. Units are set by WavelengthUnit.
    wavelength_unit : UnitsLength
        The units of the Wavelength - default:nanometres[nm].
    frequency_multiplication : None | int
        FrequencyMultiplication that may be specified. [units:none]
    tuneable : None | bool
        Whether or not the laser is Tuneable [flag]
    pulse : None | Laser_Pulse
        The Pulse mode of the laser.
    pockel_cell : None | bool
        If true the laser has a PockelCell to rotate the polarization of the beam.
        [flag]
    repetition_rate : None | float
        The is the rate in Hz at which the laser pulses if the Pulse type is
        'Repetitive'. hertz[Hz] Units are set by RepetitionRateUnit.
    repetition_rate_unit : UnitsFrequency
        The units of the RepetitionRate - default:hertz[Hz].
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    pump: Optional[Pump] = Field(
        default=None,
        metadata={
            "name": "Pump",
            "type": "Element",
        },
    )
    type: Optional[Laser_Type] = Field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
    laser_medium: Optional[Laser_LaserMedium] = Field(
        default=None,
        metadata={
            "name": "LaserMedium",
            "type": "Attribute",
        },
    )
    wavelength: Optional[float] = Field(
        default=None,
        metadata={
            "name": "Wavelength",
            "type": "Attribute",
            "min_exclusive": 0.0,
        },
        gt=0.0,
    )
    wavelength_unit: UnitsLength = Field(
        default=UnitsLength.NANOMETER,
        metadata={
            "name": "WavelengthUnit",
            "type": "Attribute",
        },
    )
    frequency_multiplication: Optional[int] = Field(
        default=None,
        metadata={
            "name": "FrequencyMultiplication",
            "type": "Attribute",
            "min_inclusive": 1,
        },
        ge=1,
    )
    tuneable: Optional[bool] = Field(
        default=None,
        metadata={
            "name": "Tuneable",
            "type": "Attribute",
        },
    )
    pulse: Optional[Laser_Pulse] = Field(
        default=None,
        metadata={
            "name": "Pulse",
            "type": "Attribute",
        },
    )
    pockel_cell: Optional[bool] = Field(
        default=None,
        metadata={
            "name": "PockelCell",
            "type": "Attribute",
        },
    )
    repetition_rate: Optional[float] = Field(
        default=None,
        metadata={
            "name": "RepetitionRate",
            "type": "Attribute",
        },
    )
    repetition_rate_unit: UnitsFrequency = Field(
        default=UnitsFrequency.HERTZ,
        metadata={
            "name": "RepetitionRateUnit",
            "type": "Attribute",
        },
    )


LaserMedium = Laser_LaserMedium
Pulse = Laser_Pulse
Type = Laser_Type
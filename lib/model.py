from dataclasses import dataclass
from typing import List
import marshmallow_dataclass


@dataclass
class AxisConfiguration:
    label: str
    increment_per_step: float
    direction: int
    decimal_places: int = 3


@dataclass
class Origin:
    name: str
    offset: List[float]


@dataclass
class Tool:
    tool_number: int
    name: str
    icon: str
    offset: List[float]
    diameter: float


@dataclass
class Settings:
    axis_configurations: List[AxisConfiguration]
    origins: List[Origin]
    tools: List[Tool]
    current_tool: int
    current_origin: int


settings_schema = marshmallow_dataclass.class_schema(Settings)()

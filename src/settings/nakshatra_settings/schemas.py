# -*- coding: utf-8 -*-
from enum import Enum

from pydantic import BaseModel

class AstroObjectName(str, Enum):
    sun = "sun"
    moon = "moon"
    ketu = "ketu"
    rahu = "rahu"
    mars = "mars"
    venus = "venus"
    jupiter = "jupiter"
    saturn = "saturn"

class AstroObjectRusName(str, Enum):
    sun = "Солнце"
    moon = "Луна"
    ketu = "Кету"
    rahu = "Раху"
    mars = "Марс"
    venus = "Венера"
    jupiter = "Юпитреа"
    saturn = "Сатурн"

class AstroObject(BaseModel):
    name: AstroObjectName
    filename: str
    rus_name: AstroObjectRusName
    radius: float
    zoom: float

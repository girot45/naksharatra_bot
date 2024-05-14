# -*- coding: utf-8 -*-
from astropy.table import Table
from astropy.time import Time
from settings.nakshatra_settings.schemas import \
    AstroObject, AstroObjectRusName, AstroObjectName

def create_astro_object(name, radius, zoom):
    return AstroObject(
        name=name,
        rus_name=AstroObjectRusName[name],
        filename=f"resources/img/{name}.png",
        radius=radius,
        zoom=zoom
    )

objects = [
    [AstroObjectName.sun,0.1,1],
    [AstroObjectName.moon,0.1,1],
    [AstroObjectName.ketu,0.1,1],
    [AstroObjectName.rahu,0.1,1],
    [AstroObjectName.mars,0.1,1],
    [AstroObjectName.venus,0.1,1],
    [AstroObjectName.jupiter,0.1,1],
    [AstroObjectName.saturn,0.1,1]
]

astro_objects = {
    name.value: create_astro_object(name, radius, zoom)
    for name, radius, zoom in objects
}

class NakshaSettings:
    res_filename = "res_img/res.png"
    nakshatram_filename = "resources/tex_files/nakshatram_names.tex"
    rashi_filename = "resources/tex_files/rashi_names.tex"
    tithi_filename = "resources/tex_files/tithi_names.tex"
    vaara_filename = "resources/tex_files/vaara_names.tex"

    nak = Table.read(nakshatram_filename, format="latex")
    nakshatram_names = nak['names'].data
    ras = Table.read(rashi_filename, format="latex")
    rashi_names = ras["names"].data
    # tit = Table.read(tithi_filename, format="latex")
    # tithi_names = tit["names"].data
    # vaa = Table.read(vaara_filename, format="latex")
    # vaara_names = vaa["names"].data


    full_circle_degs = 360
    nakshatran_count = 27  # всего накшатр

    start_coord = 23 + 47 / 60 + 14.1 / 3600
    nakshatram_extent = full_circle_degs / nakshatran_count  # шаг между разделителями

    rashi_start = 23 + 46 / 60
    rashi_extent = 360 / 12

    ketu_speed = full_circle_degs  / 18.612958  # градусов в год

    each_tithi = 360 / 30

    known_eclipse_time = Time(
        "2023-04-20 04:16:49",
        format="iso",
        scale="utc"
    )  ### Время когда луна была в раху


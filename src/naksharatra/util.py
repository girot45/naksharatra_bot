from typing import Any

import numpy as np

from settings import nakshatra_settings


def calc_nakshatram_coords():
    return np.linspace(
        nakshatra_settings.start_coord,
        (
            nakshatra_settings.start_coord +
            nakshatra_settings.nakshatram_extent *
            nakshatra_settings.nakshatran_count
        ),
        nakshatra_settings.nakshatran_count
    )

from utilities.hydraulics import *
from utilities.utils_ogee import *

# CONSTANTS
GRAVITY = 9.81


class OgeeWeir:
    def __init__(self):
        """
        Initialization of global variables
        """
        self._discharge = 0.0
        self._crest_length = 0.0
        self._us_apron = 0.0
        self._ds_apron = 0.0
        self._crest_elev = 0.0
        self._tail_water_elev = 0.0

    def calculate_afflux(self):
        us_apron_elev = self._us_apron
        ds_apron_elev = self._ds_apron
        tail_water_elev = self._tail_water_elev
        discharge = self._discharge
        crest_length = self._crest_length
        crest_elev = self._crest_elev
        discharge_intensity = discharge / crest_length

        # Assume initial value for afflux elevation
        afflux_elev = tail_water_elev + 0.0001

        # Calculated discharge intensity
        c_discharge_intensity = 0

        while abs(discharge_intensity - c_discharge_intensity) > 0.005:
            afflux_elev += 0.0001
            da = afflux_elev - us_apron_elev       # Depth of approach
            va = discharge_intensity / da          # Velocity at approach
            ha = get_velocity_head(va)             # Velocity head at approach
            energy_elev = afflux_elev + ha
            ho = energy_elev - crest_elev
            p_h = (crest_elev - us_apron_elev) / ho
            co = get_co(p_h)
            hd = energy_elev - tail_water_elev
            hd_ho = hd / ho
            d = tail_water_elev - ds_apron_elev    # Depth of tail water
            hd_d = hd + d
            hdd_ho = hd_d / ho


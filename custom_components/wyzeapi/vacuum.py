"""Platform for vacuum integration."""
import logging

# Import the device class from the component that you want to support
from homeassistant.components.vacuum import VacuumDevice
from homeassistant.const import ATTR_ATTRIBUTION

from . import DOMAIN

class HAWyzeVacuum(VacuumDevice):
    def turn_on(self, **kwargs):
        pass

    def turn_off(self, **kwargs):
        pass

    def start_pause(self, **kwargs):
        pass

    @property
    def supported_features(self):
        pass

    @property
    def fan_speed_list(self):
        pass

    def stop(self, **kwargs):
        pass

    def return_to_base(self, **kwargs):
        pass

    def clean_spot(self, **kwargs):
        pass

    def locate(self, **kwargs):
        pass

    def set_fan_speed(self, fan_speed, **kwargs):
        pass

    def send_command(self, command, params=None, **kwargs):
        pass

    @property
    def is_on(self) -> bool:
        pass
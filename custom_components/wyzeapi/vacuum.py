"""Platform for vacuum integration."""
import logging

# Import the device class from the component that you want to support
from homeassistant.components.vacuum import (
    SUPPORT_BATTERY,
    SUPPORT_FAN_SPEED,
    SUPPORT_RETURN_HOME,
    SUPPORT_STATUS,
    SUPPORT_STOP,
    SUPPORT_TURN_OFF,
    SUPPORT_TURN_ON,
    VacuumEntity,
)

from . import DOMAIN
from smartbridge.providers.wyze import WyzeProvider
from smartbridge.providers.wyze.devices import WyzeVacuum
from smartbridge.interfaces.devices import VacuumMode

_LOGGER = logging.getLogger(__name__)

SUPPORT_WYZEVAC = (
    SUPPORT_BATTERY
    | SUPPORT_RETURN_HOME
    | SUPPORT_STOP
    | SUPPORT_TURN_OFF
    | SUPPORT_TURN_ON
    | SUPPORT_STATUS
    | SUPPORT_FAN_SPEED
)


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the Wyze vacuums."""
    wyzeapi_platform: WyzeProvider = hass.data[DOMAIN]["wyzeapi_platform"]

    vacuums = []
    for vacuum in wyzeapi_platform.vacuum.list():
        vacuums.append(HAWyzeVacuum(wyzeapi_platform.vacuum.get(vacuum.mac)))

    _LOGGER.debug("Adding Wyze Vacuums to Home Assistant: %s", vacuums)
    add_entities(vacuums, True)


class HAWyzeVacuum(VacuumEntity):
    def start_pause(self, **kwargs):
        raise NotImplementedError()

    def __init__(self, smartbridge_vacuum):
        self.vacuum: WyzeVacuum = smartbridge_vacuum

    def turn_on(self, **kwargs):
        self.vacuum.clean()

    def turn_off(self, **kwargs):
        self.vacuum.dock()

    @property
    def supported_features(self):
        return SUPPORT_WYZEVAC

    @property
    def fan_speed_list(self):
        return self.vacuum._suction_levels

    def stop(self, **kwargs):
        self.vacuum.dock()

    def return_to_base(self, **kwargs):
        self.vacuum.dock()

    def clean_spot(self, **kwargs):
        raise NotImplementedError()

    def locate(self, **kwargs):
        raise NotImplementedError()

    def set_fan_speed(self, fan_speed, **kwargs):
        self.vacuum.suction_level = fan_speed

    def send_command(self, command, params=None, **kwargs):
        raise NotImplementedError()

    @property
    def is_on(self) -> bool:
        return False if self.vacuum.mode is VacuumMode.IDLE else True

    def should_poll(self) -> bool:
        return True

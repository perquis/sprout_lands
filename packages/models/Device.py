import os

import win32api


class Device:
    def __init__(self) -> None:
        self.__device = win32api.EnumDisplayDevices()

    def get_refresh_rate(self) -> float:
        if os.name == "nt":
            settings = win32api.EnumDisplaySettings(
                self.__device.DeviceName, -1
            )
            refresh_rate = settings.DisplayFrequency
            to_float_result = float(refresh_rate)

            return to_float_result

        return 60.0

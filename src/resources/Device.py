import os
import pygame
from typing import Tuple

if os.name == "posix":
    import Quartz
elif os.mane == "nt":
    import win32api

class Device:
    def __init__(self) -> None:
        if os.name == "nt":
            self.__device = win32api.EnumDisplayDevices()

    def get_refresh_rate(self) -> float:
        if os.name == "nt":
            settings = win32api.EnumDisplaySettings(
                self.__device.DeviceName, -1
            )
            refresh_rate = settings.DisplayFrequency
            return float(refresh_rate)
        elif os.name == "posix":
            display = Quartz.CGMainDisplayID()
            refresh_rate = Quartz.CGDisplayModeGetRefreshRate(
                Quartz.CGDisplayCopyDisplayMode(display)
            )
            return refresh_rate if refresh_rate > 0 else 60.0  # Default to 60 Hz if unavailable

        return 60.0  # Default refresh rate

    def get_display(self) -> Tuple[int, int]:
        if os.name == "nt":
            resolution = pygame.display.Info()
            return resolution.current_w, resolution.current_h
        elif os.name == "posix":
            display = Quartz.CGMainDisplayID()
            width = Quartz.CGDisplayPixelsWide(display)
            height = Quartz.CGDisplayPixelsHigh(display)
            return width, height

        return (0, 0)  # Default resolution if OS not supported

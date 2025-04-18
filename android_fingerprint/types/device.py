# Re-defining the protocol after kernel reset
from typing import Protocol, runtime_checkable
from .device_data import DeviceDataT


@runtime_checkable
class AndroidT(Protocol):
    model_name: str
    build_id: str
    android_version_full: str
    android_api_level: int
    manufecturer: str
    manufecturer_id: str
    model_firmware_codename: str
    patch_date: str
    dalvik_version: str

    @property
    def android_version_major(self) -> int: ...

    @property
    def device_platform(self) -> str: ...

    def system_agent(self) -> str: ...

    def to_dict(self) -> DeviceDataT: ...

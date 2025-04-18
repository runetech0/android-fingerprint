# Re-defining the protocol after kernel reset
from typing import Protocol, runtime_checkable
from typing import Dict

# Placeholder for DeviceDataT
DeviceDataT = Dict[str, str | int]  # replace with actual strict type if available


@runtime_checkable
class AndroidProtocol(Protocol):
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

from typing import TypedDict


class DeviceDataT(TypedDict):
    model_name: str
    android_version: str
    build_id: str
    patch_date: str
    model_firmware_codename: str
    api_level: str
    manufecturer: str
    manufecturer_id: str

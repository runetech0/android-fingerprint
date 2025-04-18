import random
from .types.android_data import DeviceDataT
from .data.google_phones import GOOGLE_DEIVCES_LIST


class Android:
    def __init__(self, device_data: DeviceDataT) -> None:
        if not device_data:
            device_data = random.choice(GOOGLE_DEIVCES_LIST)

        self.model_name = device_data["model_name"]
        self.build_id = device_data["build_id"]
        self.android_version_full = device_data["android_version"]
        self.android_api_level = device_data["api_level"]
        self.manufecturer = device_data["manufecturer"]
        self.manufecturer_id = device_data["manufecturer_id"]
        self.model_firmware_codename = device_data["model_firmware_codename"]
        self.patch_date = device_data["patch_date"]
        self.dalvik_version = "2.1.0"

    @property
    def android_version_major(self) -> int:
        return int(self.android_version_full.split(".")[0])

    @property
    def device_platform(self) -> str:
        return "android"

    def system_agent(self) -> str:
        return f"Dalvik/{self.dalvik_version} (Linux; U; Android {self.android_version_major}; {self.model_name} Build/{self.build_id})"

    def to_dict(self) -> DeviceDataT:
        return {
            "model_name": self.model_name,
            "android_version": self.android_version_full,
            "build_id": self.build_id,
            "patch_date": self.patch_date,
            "model_firmware_codename": self.model_firmware_codename,
            "api_level": self.android_api_level,
            "manufecturer": self.manufecturer,
            "manufecturer_id": self.manufecturer_id,
        }

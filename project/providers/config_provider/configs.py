import json
import os

from providers.config_provider.base_config import BaseConfig
from providers.config_provider.default import DEFAULT_CONFIG


class ConfigFromEnvProvider(BaseConfig):

    def __init__(self):
        keys = {}
        for key in DEFAULT_CONFIG.keys():
            if os.environ.get(key):
                to_update = {f"{key}": f"{os.environ.get(key)}"}
                keys.update(to_update)
        super(ConfigFromEnvProvider, self).__init__(**keys)


class ConfigFromDict(BaseConfig):

    def __init__(self, kwargs):
        if not kwargs:
            super().__init__(**DEFAULT_CONFIG)
        super().__init__(**kwargs)


class ConfigFromFile(BaseConfig):

    def __init__(self, file_path):
        self.__dict__ = ConfigFromFile.config_from_file(file_path)
        super().__init__(**self.__dict__)

    @classmethod
    def config_from_file(cls, file):
        with open(file, "r") as file:
            return json.load(file)


class ConfigProvider(BaseConfig):

    def __init__(self, configs: list):
        self.configs = configs

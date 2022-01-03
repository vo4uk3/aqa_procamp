from providers.config_provider.base_config import BaseConfig
from providers.config_provider.configs import ConfigFromDict, ConfigFromEnvProvider, ConfigFromFile, ConfigProvider


class Config(BaseConfig):
    default = 'prod'
    from_dict = {"erty": 456778}

    def __init__(self):
        super(Config, self).__init__()
        env = ConfigFromEnvProvider()
        json_config = f"/home/stepan/AQA_GL/project/providers/config_provider/files/{env.__dict__.get('ENV', Config.default)}.json"
        dct = ConfigFromDict()
        file = ConfigFromFile(json_config)
        config = ConfigProvider([dct, file, env])
        self.update(config.configs)

    def set_key(self, **key):
        self.__dict__.update(key)

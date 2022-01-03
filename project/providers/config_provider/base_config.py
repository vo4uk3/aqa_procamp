
class BaseConfig:

    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

    def __getattr__(self, item):
        if not self.__dict__.get(item):
            raise KeyError(f"No '{item}' key  in the config ")

    def update(self, providers):
        for provider in providers:
            self.__dict__.update(provider.__dict__)

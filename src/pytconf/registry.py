"""
registry of config names
"""

from typing import Any


class Registry:
    def __init__(self) -> None:
        self.names = set()
        self.configs = set()
        self.name_to_data = {}
        self.name_to_config = {}
        self.config_names = {}

    def register(self, config: type, name: str, data: Any) -> None:
        if name in self.names:
            raise ValueError(
                f"pytconf: name [{name}] appears more than once"
            )
        self.names.add(name)
        self.configs.add(config)
        if config not in self.config_names:
            self.config_names[config] = {}
        self.name_to_data[name] = data
        self.name_to_config[name] = config
        self.config_names[config][name] = data

    def yield_configs(self):
        yield from self.configs

    def yield_names_for_config(self, config: type):
        yield from self.config_names[config].keys()

    def yield_name_data_for_config(self, config: type):
        yield from self.config_names[config].items()

    def get_data_for_name(self, name: str):
        return self.name_to_data[name]

    def get_config_for_name(self, name: str):
        return self.name_to_config[name]

    def has_name(self, name: str) -> bool:
        return name in self.names


the_registry: Registry = Registry()

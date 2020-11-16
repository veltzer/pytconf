class Registry:
    def __init__(self):
        self.names = set()
        self.configs = set()
        self.name_to_data = dict()
        self.name_to_config = dict()

    def register(self, config, name, data):
        if name in self.names:
            raise ValueError(
                f"pytconf: name [{name}] appears more than once"
            )
        self.names.add(name)
        self.configs.add(config)
        self.name_to_data[name] = data
        self.name_to_config[name] = config

    def yield_configs(self):
        for config in self.configs:
            yield config

    def get_data_for_name(self, name):
        return self.name_to_data[name]

    def get_config_for_name(self, name):
        return self.name_to_config[name]

    def has_name(self, name):
        return name in self.names


the_registry = Registry()

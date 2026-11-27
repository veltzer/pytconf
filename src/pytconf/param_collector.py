"""
A collector for all parameters
"""



class ParamCollector:
    def __init__(self) -> None:
        self.data = []

    def add_data(self, item: object) -> None:
        self.data.append(item)

    def clear(self) -> None:
        self.data = []

    def get_item(self, i: int):
        return self.data[i]

    def yield_items(self):
        yield from self.data


the_collector: ParamCollector = ParamCollector()

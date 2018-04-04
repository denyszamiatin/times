
class NewsPipeLine:

    def __init__(self, pipes):
        self.pipes = pipes

    def proceed_item(self, item):
        for pipe in self.pipes:
            item = pipe(item)
        return item

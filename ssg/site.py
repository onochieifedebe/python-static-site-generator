from pathlib import Path


class Site:

    def __init__(self, source, dest):
        source = Path()
        dest = Path()
        self.source = source
        self.dest = dest

    def create_dir(self, path):
        directory = self.dest / self.source.relative_to(path)
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path in dir():
                Site.create_dir(path)
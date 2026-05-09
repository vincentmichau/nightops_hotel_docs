class TemplateRepository:
    def __init__(self): self._templates = {}
    def save(self, name, template): self._templates[name] = dict(template); return name
    def load(self, name): return self._templates.get(name)
    def names(self): return sorted(self._templates)

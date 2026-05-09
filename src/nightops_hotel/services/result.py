class ServiceResult:
    def __init__(self, ok=True, data=None, errors=None, warnings=None):
        self.ok=ok; self.data=data or {}; self.errors=errors or []; self.warnings=warnings or []
    def to_dict(self): return {"ok":self.ok,"data":self.data,"errors":self.errors,"warnings":self.warnings}

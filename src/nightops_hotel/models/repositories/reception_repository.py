class ReceptionRepository:
    def __init__(self): self._records=[]
    def replace_all(self, records): self._records=list(records); return len(self._records)
    def list_all(self): return list(self._records)
    def count(self): return len(self._records)
    def total_persons(self): return sum(r.persons for r in self._records)

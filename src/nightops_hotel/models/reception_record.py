from dataclasses import asdict, dataclass

@dataclass(frozen=True)
class ReceptionRecord:
    arrival: str
    departure: str
    room: str
    persons: int
    last_name: str = ""
    first_name: str = ""
    language: str = "FR"
    status: str = ""
    def to_dict(self): return asdict(self)
    def to_template_data(self): return {"reservation": asdict(self)}

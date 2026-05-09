from dataclasses import dataclass, asdict
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
    def to_template_data(self): return {"reservation": asdict(self)}

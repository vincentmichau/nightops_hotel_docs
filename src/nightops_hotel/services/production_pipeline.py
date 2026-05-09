from nightops_hotel.models.reception_record import ReceptionRecord
from nightops_hotel.services.result import ServiceResult

class ProductionPipeline:
    REQUIRED_FIELDS = ["arrival", "departure", "room", "persons"]
    STEPS = ["validate_xml", "normalize", "repository", "template_runtime", "document_generation", "exports", "print_or_fallback", "qa_report", "rgpd_audit"]
    def rows_to_records(self, rows):
        errors, records = [], []
        for index, row in enumerate(rows):
            missing = [field for field in self.REQUIRED_FIELDS if field not in row]
            if missing:
                errors.append(f"Ligne {index}: champs manquants {', '.join(missing)}")
                continue
            try:
                persons = int(row.get("persons") or 0)
            except (TypeError, ValueError):
                errors.append(f"Ligne {index}: personnes invalide")
                continue
            records.append(ReceptionRecord(row.get("arrival", ""), row.get("departure", ""), row.get("room", ""), persons, row.get("last_name", ""), row.get("first_name", ""), (row.get("language") or "FR").upper(), row.get("status", "")))
        return ServiceResult(not errors, {"records": records}, errors)
    def validate_execution(self, executed):
        missing = [step for step in self.STEPS if step not in set(executed)]
        return ServiceResult(not missing, {"missing": missing}, ["Pipeline incomplet"] if missing else [])

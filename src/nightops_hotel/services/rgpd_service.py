from nightops_hotel.services.result import ServiceResult
class RGPDService:
    RETENTION_DAYS = 30
    MINIMAL_EXPORT_FIELDS = ["arrival", "departure", "room", "language", "persons", "status"]
    def audit(self, records):
        purge = [record for record in records if record.get("age_days", 0) > self.RETENTION_DAYS]
        return ServiceResult(True, {"retention_days": self.RETENTION_DAYS, "purge_candidates": len(purge)})

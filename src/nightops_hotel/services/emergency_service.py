from nightops_hotel.services.result import ServiceResult
class EmergencyService:
    SCENARIOS = {"invalid_xml": ["use_last_local_state", "export_qa_logs"], "broken_template": ["use_sample_template", "disable_formula"], "pdf_failure": ["export_html", "manual_print"], "excel_locked": ["csv_fallback", "close_excel"], "printer_unavailable": ["open_pdf", "windows_print"], "local_db_unavailable": ["read_backup", "export_qa_logs"]}
    def resolve(self, scenario): return ServiceResult(True, {"scenario": scenario, "steps": self.SCENARIOS.get(scenario, ["export_qa_logs", "contact_support"])})

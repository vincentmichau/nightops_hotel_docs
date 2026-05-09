from nightops_hotel.services.result import ServiceResult
class DocumentService:
    REQUIRED_OUTPUTS = ["preview_html", "pdf_weasyprint", "excel_export", "docx_contract", "print_preview"]
    def rows_from_records(self, records): return [record.to_template_data()["reservation"] for record in records]
    def validate_outputs(self, outputs):
        missing = [output for output in self.REQUIRED_OUTPUTS if output not in set(outputs)]
        return ServiceResult(not missing, {"missing": missing}, ["Sorties documents incomplètes"] if missing else [])

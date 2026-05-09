class TemplatesImportExportsLock:
    """Verrou non-régression templates/import/exports."""
    CHECKS = ['template_create', 'template_save_load', 'condition', 'calculation', 'xml_import', 'pdf_weasyprint', 'excel_export', 'docx_contract', 'print_preview']
    def validate(self, checked):
        missing = [check for check in self.CHECKS if check not in set(checked)]
        return {'ok': not missing, 'missing': missing}

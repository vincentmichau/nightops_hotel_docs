class OperatorDocumentationRelease:
    """Documentation opérateur finale."""
    SECTIONS = ['import_xml', 'controle_arrivees', 'templates', 'generation_pdf', 'export_excel', 'impression', 'mode_secours', 'rgpd', 'logs_support']
    def validate(self, sections):
        missing = [section for section in self.SECTIONS if section not in set(sections)]
        return {'ok': not missing, 'missing': missing}

class OperationalPipelineLock:
    """Verrou du pipeline réception complet."""
    STEPS = [
        'select_xml', 'parse_xml', 'validate_xml', 'normalize_records', 'persist_records',
        'choose_templates', 'preview_documents', 'generate_pdf', 'export_excel', 'print_or_emergency',
        'qa_trace', 'rgpd_retention'
    ]
    def validate(self, executed):
        missing = [step for step in self.STEPS if step not in set(executed)]
        return {'ok': not missing, 'missing': missing}

class RealRobustnessSuite:
    """Suite de robustesse réelle orientée incidents terrain."""
    CASES = {
        'xml': ['missing_file', 'bad_xml', 'missing_room', 'bad_person_count'],
        'template': ['missing_field', 'bad_formula', 'bad_condition', 'legacy_template'],
        'export': ['pdf_failure', 'excel_locked', 'bad_output_path', 'empty_dataset'],
        'storage': ['db_locked', 'schema_missing', 'write_denied'],
        'print': ['printer_missing', 'manual_print_required'],
        'rgpd': ['purge_due', 'minimal_export_required'],
    }
    def required(self):
        return [f'{domain}:{case}' for domain, cases in self.CASES.items() for case in cases]
    def validate(self, executed):
        missing = [case for case in self.required() if case not in set(executed)]
        return {'ok': not missing, 'missing': missing}

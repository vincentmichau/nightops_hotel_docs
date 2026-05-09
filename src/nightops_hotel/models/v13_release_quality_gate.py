class V13ReleaseQualityGate:
    """Quality gate v13 stable-release."""
    SIGNALS = [
        'features_ok', 'corrections_ok', 'unit_tests_ok', 'integration_tests_ok', 'e2e_ok',
        'robustness_ok', 'code_review_ok', 'workflows_ok', 'artifacts_ok', 'packaging_ok',
        'docs_ok', 'ux_ok', 'rgpd_ok', 'templates_ok', 'xml_ok', 'exports_ok', 'emergency_ok'
    ]
    def evaluate(self, signals):
        missing = [signal for signal in self.SIGNALS if not signals.get(signal, False)]
        return {'ok': not missing, 'missing': missing}

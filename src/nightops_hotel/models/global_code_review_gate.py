class GlobalCodeReviewGate:
    """Revue de code globale obligatoire."""
    CHECKS = ['mvc', 'dao_factory', 'thin_controllers', 'services', 'tests', 'docs', 'ux', 'rgpd', 'templates', 'exports', 'workflows', 'packaging', 'emergency']
    def validate(self, checked):
        missing = [check for check in self.CHECKS if check not in set(checked)]
        return {'ok': not missing, 'missing': missing}

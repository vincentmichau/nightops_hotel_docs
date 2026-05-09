class V13StableReleaseManifest:
    """Manifeste v13 stable-release : tout le projet progresse et reste verrouillé."""
    VERSION = '13.0.0-global-stable-release'
    PILLARS = [
        'features', 'corrections', 'tests', 'code_review', 'github_workflows', 'packaging',
        'documentation', 'ux', 'rgpd', 'templates', 'xml_import', 'exports', 'emergency_mode',
        'mvc', 'dao_factory', 'weasyprint'
    ]
    def as_dict(self):
        return {'version': self.VERSION, 'pillars': list(self.PILLARS)}
    def validate(self, pillars):
        missing = [pillar for pillar in self.PILLARS if pillar not in set(pillars)]
        return {'ok': not missing, 'missing': missing}

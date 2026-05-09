class GitHubArtifactContract:
    """Contrat artefacts GitHub pour CI/release."""
    ARTIFACTS = ['test-report.xml', 'ruff-report.txt', 'qa-summary.md', 'release-report.md', 'nightops-portable.zip']
    def validate(self, produced):
        missing = [artifact for artifact in self.ARTIFACTS if artifact not in set(produced)]
        return {'ok': not missing, 'missing': missing}

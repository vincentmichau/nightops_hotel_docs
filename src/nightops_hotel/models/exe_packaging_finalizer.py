class ExePackagingFinalizer:
    """Finalisation packaging exe portable Windows."""
    REQUIRED = ['nightops.exe', 'nightops-portable.zip', 'assets/', 'templates/', 'docs/', 'logs/', 'data/', 'exports/', 'examples/', 'README.md', 'LICENSE.txt']
    def expected_zip_name(self, version):
        return f'nightops-hotel-documents-{version}-windows-portable.zip'
    def validate(self, produced):
        missing = [item for item in self.REQUIRED if item not in set(produced)]
        return {'ok': not missing, 'missing': missing}

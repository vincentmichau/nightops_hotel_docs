def test_version():
    import nightops_hotel
    assert nightops_hotel.__version__ == '13.0.0-global-stable-release'

def test_v13_manifest():
    from nightops_hotel.models.v13_stable_release_manifest import V13StableReleaseManifest
    m=V13StableReleaseManifest(); assert m.validate(m.PILLARS)['ok'] is True

def test_operational_pipeline_lock():
    from nightops_hotel.models.operational_pipeline_lock import OperationalPipelineLock
    l=OperationalPipelineLock(); assert l.validate(l.STEPS)['ok'] is True

def test_real_robustness_suite():
    from nightops_hotel.models.real_robustness_suite import RealRobustnessSuite
    s=RealRobustnessSuite(); assert s.validate(s.required())['ok'] is True

def test_user_emergency_playbook():
    from nightops_hotel.models.user_emergency_playbook import UserEmergencyPlaybook
    p=UserEmergencyPlaybook(); assert p.validate()['ok'] is True

def test_exe_packaging_finalizer():
    from nightops_hotel.models.exe_packaging_finalizer import ExePackagingFinalizer
    p=ExePackagingFinalizer(); assert p.validate(p.REQUIRED)['ok'] is True

def test_github_artifact_contract():
    from nightops_hotel.models.github_artifact_contract import GitHubArtifactContract
    c=GitHubArtifactContract(); assert c.validate(c.ARTIFACTS)['ok'] is True

def test_global_code_review_gate():
    from nightops_hotel.models.global_code_review_gate import GlobalCodeReviewGate
    g=GlobalCodeReviewGate(); assert g.validate(g.CHECKS)['ok'] is True

def test_templates_import_exports_lock():
    from nightops_hotel.models.templates_import_exports_lock import TemplatesImportExportsLock
    l=TemplatesImportExportsLock(); assert l.validate(l.CHECKS)['ok'] is True

def test_operator_documentation_release():
    from nightops_hotel.models.operator_documentation_release import OperatorDocumentationRelease
    d=OperatorDocumentationRelease(); assert d.validate(d.SECTIONS)['ok'] is True

def test_v13_quality_gate():
    from nightops_hotel.models.v13_release_quality_gate import V13ReleaseQualityGate
    g=V13ReleaseQualityGate(); assert g.evaluate({s: True for s in g.SIGNALS})['ok'] is True

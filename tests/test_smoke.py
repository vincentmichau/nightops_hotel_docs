from nightops_hotel.controllers.production_reception_controller import ProductionReceptionController
from nightops_hotel.models.objective_guard import ObjectiveGuard
from nightops_hotel.models.repositories.reception_repository import ReceptionRepository
from nightops_hotel.services.document_service import DocumentService
from nightops_hotel.services.emergency_service import EmergencyService
from nightops_hotel.services.production_pipeline import ProductionPipeline
from nightops_hotel.services.rgpd_service import RGPDService

def test_version():
    import nightops_hotel
    assert nightops_hotel.__version__ == "15.15.0-github-full-reload-production"

def test_pipeline_controller_repository_documents():
    repo = ReceptionRepository(); pipeline = ProductionPipeline(); docs = DocumentService(); controller = ProductionReceptionController(pipeline, docs)
    result = controller.import_rows([{"arrival": "a", "departure": "d", "room": "1", "persons": "2"}], repo)
    assert result.ok is True
    assert repo.count() == 1
    assert repo.total_persons() == 2
    assert controller.document_rows(repo)[0]["room"] == "1"
    assert docs.validate_outputs(docs.REQUIRED_OUTPUTS).ok is True

def test_rgpd_emergency_objective():
    assert RGPDService().audit([{"age_days": 31}]).data["purge_candidates"] == 1
    assert EmergencyService().resolve("pdf_failure").ok is True
    text = "XML réception templates PDF Excel impression RGPD UX secours GitHub Windows MVC DAO WeasyPrint"
    assert ObjectiveGuard().validate(text)["ok"] is True

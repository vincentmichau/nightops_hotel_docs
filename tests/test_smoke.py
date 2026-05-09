from nightops_hotel.services.production_pipeline import ProductionPipeline
from nightops_hotel.models.repositories.reception_repository import ReceptionRepository
from nightops_hotel.services.document_service import DocumentService
from nightops_hotel.controllers.production_reception_controller import ProductionReceptionController

def test_version():
    import nightops_hotel
    assert nightops_hotel.__version__ == "15.11.0-github-requirements-fix"

def test_pipeline_controller_repository_documents():
    repo=ReceptionRepository(); pipeline=ProductionPipeline(); docs=DocumentService(); controller=ProductionReceptionController(pipeline, docs)
    result=controller.import_rows([{"arrival":"a","departure":"d","room":"1","persons":"2"}], repo)
    assert result.ok is True
    assert repo.count()==1
    assert repo.total_persons()==2
    assert controller.document_rows(repo)[0]["room"]=="1"

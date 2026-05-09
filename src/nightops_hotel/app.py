from nightops_hotel.controllers.production_reception_controller import ProductionReceptionController
from nightops_hotel.models.repositories.reception_repository import ReceptionRepository
from nightops_hotel.services.document_service import DocumentService
from nightops_hotel.services.production_pipeline import ProductionPipeline

def run_demo():
    rows = [{"arrival": "05-05-26", "departure": "06-05-26", "room": "101", "persons": "2"}]
    repo = ReceptionRepository()
    pipeline = ProductionPipeline()
    docs = DocumentService()
    controller = ProductionReceptionController(pipeline, docs)
    result = controller.import_rows(rows, repo)
    return {"ok": result.ok, "message": f"NightOps demo OK - {repo.count()} réservation(s), {repo.total_persons()} personne(s)"}

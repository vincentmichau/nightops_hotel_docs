class ProductionReceptionController:
    def __init__(self, pipeline, document_service): self.pipeline=pipeline; self.document_service=document_service
    def import_rows(self, rows, repository):
        parsed=self.pipeline.rows_to_records(rows)
        if not parsed.ok: return parsed
        repository.replace_all(parsed.data["records"]); return parsed
    def document_rows(self, repository): return self.document_service.rows_from_records(repository.list_all())

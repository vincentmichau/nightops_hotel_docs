class OperatorMessages:
    MESSAGES = {"safe_error": "Action impossible pour le moment. Rien n’a été perdu.", "emergency_available": "Un mode secours est disponible.", "logs_ready": "Les logs support peuvent être exportés."}
    def get(self, key): return self.MESSAGES.get(key, self.MESSAGES["safe_error"])

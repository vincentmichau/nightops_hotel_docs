class ObjectiveGuard:
    KEYWORDS = ["XML", "réception", "templates", "PDF", "Excel", "impression", "RGPD", "UX", "secours", "GitHub", "Windows", "MVC", "DAO", "WeasyPrint"]
    def validate(self, text):
        missing = [keyword for keyword in self.KEYWORDS if keyword.lower() not in text.lower()]
        return {"ok": not missing, "missing": missing}

class Sensore:
    def __init__(self, codice: str, grandezza: str, unita: str, soglia_massima: float) -> None:
        self.codice: str = codice
        self.grandezza: str = grandezza
        self.unita: str = unita
        self.soglia_massima: float = float(soglia_massima)
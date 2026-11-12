class Sensore:
    def __init__(self, codice: str, grandezza: str, unita: str, soglia_massima: float) -> None:
        self.codice: str = codice
        self.grandezza: str = grandezza
        self.unita: str = unita
        self.soglia_massima: float = float(soglia_massima)


if __name__ == "__main__":
    # Test rapido richiesto dal branch features/modello-sensore
    s1 = Sensore("TEMP-01", "temperatura", "C", 45.0)
    s2 = Sensore("BATT-01", "tensione batteria", "V", 8.4)
    print(f"Sensore 1: {s1.codice} ({s1.grandezza}) - Soglia: {s1.soglia_massima} {s1.unita}")
    print(f"Sensore 2: {s2.codice} ({s2.grandezza}) - Soglia: {s2.soglia_massima} {s2.unita}")
from sensore import Sensore

class Satellite:
    def __init__(self, nome: str = "CubeSat Aurora") -> None:
        self.nome: str = nome
        self.sensori: dict[str, Sensore] = {}
        self.letture: list[dict] = []

    def aggiungi_sensore(self, sensore: Sensore) -> None:
        if sensore.codice in self.sensori:
            raise ValueError(f"Errore: il sensore con codice '{sensore.codice}' è già presente.")
        self.sensori[sensore.codice] = sensore
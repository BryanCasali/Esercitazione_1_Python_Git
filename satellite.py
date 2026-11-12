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

    def registra_lettura(self, codice_sensore: str, valore: float) -> None:
        if codice_sensore not in self.sensori:
            raise KeyError(f"Errore: sensore '{codice_sensore}' non registrato sul satellite.")
        
        sensore = self.sensori[codice_sensore]
        in_allarme = float(valore) > sensore.soglia_massima

        lettura = {
            "sensore": sensore.codice,
            "grandezza": sensore.grandezza,
            "valore": float(valore),
            "unita": sensore.unita,
            "allarme": in_allarme
        }
        self.letture.append(lettura)

    def letture_in_allarme(self) -> list[dict]:
        return [lettura for lettura in self.letture if lettura["allarme"]]

    def riepilogo(self) -> None:
        print(f"=== Riepilogo Telemetria: {self.nome} ===")
        if not self.letture:
            print("Nessuna lettura registrata.")
            return

        for l in self.letture:
            stato = "ALLARME" if l["allarme"] else "OK"
            print(f"[{stato}] Sensore {l['sensore']} ({l['grandezza']}): {l['valore']} {l['unita']}")
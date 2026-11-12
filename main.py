from sensore import Sensore
from satellite import Satellite


def main() -> None:
    # 1. Creazione del satellite
    cubo = Satellite("CubeSat Aurora")

    # 2. Creazione e aggiunta di 3 sensori
    s_temp = Sensore("TEMP-01", "temperatura", "C", 50.0)
    s_batt = Sensore("BATT-01", "tensione batteria", "V", 8.4)
    s_gyro = Sensore("GYRO-01", "velocità angolare", "deg/s", 12.0)

    cubo.aggiungi_sensore(s_temp)
    cubo.aggiungi_sensore(s_batt)
    cubo.aggiungi_sensore(s_gyro)

    # 3. Registrazione letture (sotto soglia, uguale alla soglia, sopra soglia)
    cubo.registra_lettura("TEMP-01", 32.5)  # Sotto soglia (OK)
    cubo.registra_lettura("TEMP-01", 50.0)  # Uguale alla soglia (OK)
    cubo.registra_lettura("TEMP-01", 54.2)  # Sopra soglia (ALLARME)

    cubo.registra_lettura("BATT-01", 7.9)   # Sotto soglia (OK)
    cubo.registra_lettura("BATT-01", 8.7)   # Sopra soglia (ALLARME)

    cubo.registra_lettura("GYRO-01", 12.0)  # Uguale alla soglia (OK)
    cubo.registra_lettura("GYRO-01", 15.5)  # Sopra soglia (ALLARME)

    # 4. Stampa del riepilogo completo
    cubo.riepilogo()

    # 5. Stampa della lista degli allarmi
    print("\n=== Letture in Allarme ===")
    allarmi = cubo.letture_in_allarme()
    for a in allarmi:
        print(f"- {a['sensore']} ({a['grandezza']}): {a['valore']} {a['unita']}")

    print("\n=== Test Sensore Inesistente ===")
    try:
        cubo.registra_lettura("RAD-99", 100.0)
    except KeyError as e:
        print(f"Eccezione gestita correttamente -> {e}")


if __name__ == "__main__":
    main()
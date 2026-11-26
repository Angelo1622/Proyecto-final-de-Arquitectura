from app import app

def test_health():
    cliente = app.test_client()
    respuesta = cliente.get("/health")
    assert respuesta.status_code == 200
    assert respuesta.get_json()["status"] == "ok"

def test_listar_citas():
    cliente = app.test_client()
    respuesta = cliente.get("/citas")
    assert respuesta.status_code == 200
    assert len(respuesta.get_json()) >= 2

def test_crear_cita():
    cliente = app.test_client()
    nueva = {"paciente": "Laura Pérez", "fecha": "2026-11-26 14:00", "especialidad": "Optometría"}
    respuesta = cliente.post("/citas", json=nueva)
    assert respuesta.status_code == 201
    assert respuesta.get_json()["paciente"] == "Laura Pérez"

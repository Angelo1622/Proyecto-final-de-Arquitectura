from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de datos simulada en memoria (stub)
citas = [
    {"id": 1, "paciente": "Ana Gómez", "fecha": "2026-11-25 09:00", "especialidad": "Medicina General"},
    {"id": 2, "paciente": "Carlos Ruiz", "fecha": "2026-11-25 10:30", "especialidad": "Odontología"}
]

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "servicio": "CloudLite-Citas"}), 200

@app.route("/citas", methods=["GET"])
def listar_citas():
    return jsonify(citas), 200

@app.route("/citas", methods=["POST"])
def crear_cita():
    datos = request.get_json()
    if not datos or "paciente" not in datos or "fecha" not in datos:
        return jsonify({"error": "Datos incompletos"}), 400
    
    nueva_cita = {
        "id": len(citas) + 1,
        "paciente": datos["paciente"],
        "fecha": datos["fecha"],
        "especialidad": datos.get("especialidad", "General")
    }
    citas.append(nueva_cita)
    return jsonify(nueva_cita), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

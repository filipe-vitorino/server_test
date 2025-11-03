from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota de teste
@app.route("/")
def index():
    return "Servidor Flask rodando!"

# Rota para receber leituras
@app.route("/enviar", methods=["POST"])
def receber_leitura():
    data = request.get_json()
    if not data:
        return jsonify({"status": "erro", "mensagem": "JSON inválido"}), 400

    # 🔹 Print do JSON bruto recebido
    print("\n📥 JSON bruto recebido do app Flutter:")
    print(data)

    # Campos esperados na leitura
    required_fields = [
        "leituraId",
        "dataLeitura",
        "totalRegistros",
        "deviceId",
        "deviceName",
        "latitude",
        "longitude",
        "logs",
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({"status": "erro", "mensagem": f"Campo '{field}' faltando"}), 400

    leitura_id = data["leituraId"]
    total_registros = data["totalRegistros"]
    device_id = data["deviceId"]
    device_name = data["deviceName"]
    latitude = data["latitude"]
    longitude = data["longitude"]
    logs = data["logs"]

    print(f"\n✅ Recebida leitura {leitura_id} do dispositivo {device_name} (ID: {device_id})")
    print(f"Timestamp: {data['dataLeitura']}, total logs: {total_registros}")
    print(f"Latitude: {latitude}, Longitude: {longitude}")
    print("Logs enviados:")
    for log in logs:
        print(log)

    return jsonify({"status": "sucesso", "mensagem": f"Leitura {leitura_id} recebida"}), 200


if __name__ == "__main__":
    # host="0.0.0.0" para permitir acesso da rede local
    app.run(host="0.0.0.0", port=5000, debug=True)

import json
import random
import os

def gerar_poligono(num_vertices):
    if num_vertices < 3:
        raise ValueError("Um polígono precisa de pelo menos 3 vértices.")
    vertices = []
    for _ in range(num_vertices):
        lon = random.uniform(-50.0, -40.0)
        lat = random.uniform(-25.0, -15.0)
        vertices.append([lon, lat])
    vertices.append(vertices[0])
    return vertices

def gerar_body_json(num_vertices):
    return {
        "srid": "4326",
        "body": {
            "areaEstudo": [
                {
                    "coordinates": [
                        gerar_poligono(num_vertices)
                    ],
                    "type": "Polygon",
                    "tipoLocalizacao": "VETORIZAR"
                }
            ]
        }
    }

if __name__ == "__main__":
    num_vertices = 1000 #configuração da variavel de vertices
    try:
        body_json = gerar_body_json(num_vertices)
        os.makedirs("massa_exemplo", exist_ok=True)
        nome_arquivo = f"massa_exemplo/polygon_{num_vertices}.json"
        with open(nome_arquivo, "w") as f:
            json.dump(body_json, f, indent=4)
        print(f"✔ Arquivo gerado: {nome_arquivo}")
    except Exception as e:
        print(f"Erro: {e}")

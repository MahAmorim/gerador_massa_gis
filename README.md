# 🗺️ Gerador de Massa GIS — JSON (Polygon, Point, Line)

Gere arquivos `.json` com geometrias vetoriais realistas — **Polygon**, **Point** e **Line** — para uso em testes de APIs GIS, validação geoespacial, automações com Postman/ApiDog/Bruno e simulações em sistemas que utilizam coordenadas SRID **4326 (WGS84)**.

Ideal para testes de:
🧪 **Validação de Geometria • GIS Loader • ArcGIS • PostGIS • Serviços Ambientais • Cadastro Territorial**

---

## 📦 O que o script gera

Um arquivo JSON com estrutura vetorial válida, incluindo:

| Campo            | Descrição                                                                 |
|------------------|----------------------------------------------------------------------------|
| `srid`           | Sistema de coordenadas — 4326 (WGS84 em graus decimais)                   |
| `type`           | Tipo vetorial: `Polygon`, `Point` ou `Line`                                |
| `coordinates`    | Lista de coordenadas válidas e fechadas (LinearRing)                      |
| `tipoLocalizacao`| Valor aceito pela API (`VETORIZAR` ou `UPLOAD`)                           |

### 🧾 Exemplo básico — Polygon com SRID 4326

```json
{
  "srid": "4326",
  "body": {
    "areaEstudo": [
      {
        "coordinates": [
          [
            [-45.60, -20.87],
            [-45.59, -20.77],
            [-45.47, -20.78],
            [-45.60, -20.87]
          ]
        ],
        "type": "Polygon",
        "tipoLocalizacao": "VETORIZAR"
      }
    ]
  }
}
```

---

## 🗂 Estrutura do Projeto

```
gerador_massa_gis/
│
├── massa_exemplo/           # Arquivos JSON gerados automaticamente
│   └── polygon_1000.json
│
├── scripts/                 # Código-fonte do gerador
│   └── gerador_poligono.py
│
├── README.md                # Este arquivo
├── LICENSE                  # MIT
└── .gitignore
```

---

## 🚀 Como usar

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/MahAmorim/gerador-massa-gis
cd gerador-massa-gis
```

---

### 2️⃣ Execute o script para gerar massa vetorial JSON

```bash
python scripts/gerador_poligono.py
```

Altere apenas esta linha no script para personalizar:

```python
num_vertices = 2000
```

O arquivo será salvo automaticamente em:

```
massa_exemplo/polygon_2000_vertices.json
```

---

## 🧪 Aplicações Reais — Onde Usar

| Ferramenta | Uso |
|------------|-----|
| ApiDog / Bruno / Postman | Envio direto como payload JSON |
| Playwright / Cypress | Automação de upload de geometria |
| Banco PostGIS | Inserção e teste de geometrias em BD |
| ArcGIS / QGIS | Visualização, inspeção e validação |
| JMeter / k6 | Testes de carga simulando payloads grandes |
| Java (DTO validation) | Teste de Enum, SRID e LinearRing |

---

## 💡 Tipos já suportados

| Tipo GIS | Status |
|----------|--------|
| Polygon  | ✔ Implementado |
| Point    | 🔜 Em desenvolvimento |
| Line     | 🔜 Em desenvolvimento |

---

## 📌 SRIDs compatíveis (validados)

| SRID | Nome | Status |
|------|------|--------|
| 4326 | WGS84 Geográfico | ✔ Aceito |
| 4674 | SIRGAS2000 Brasil | 🔜 Previsto |
| 3857 | Web Mercator | ❌ Rejeitado conforme regra |

---

## ⚠️ Importante: validade das coordenadas

As coordenadas são geradas automaticamente dentro de um **range realista para território nacional (Brasil)**:

| Tipo    | Faixa gerada |
|---------|--------------|
| Longitude | -50.0 a -40.0 |
| Latitude  | -25.0 a -15.0 |

> Essa faixa pode ser adaptada para outras regiões ou países.

---

## 🤝 Contribuindo

Contribuições são bem-vindas — especialmente para:

- Suporte a GeoJSON
- Geração de POLYGON com buracos (holes)
- CLI com argumentos (`--vertices`, `--type`, `--srid`)
- Exportar para `.geojson` e Shapefile (.shp)

---

## 📄 Licença

Este projeto é de uso livre sob licença **MIT**.  
Use, estude, modifique e compartilhe — mantendo os créditos.

---

> 💜 Criado para ajudar QAs, Engenheiros GIS, Devs e Squads a testarem APIs geoespaciais com massa válida, intencional e inteligente — sem dor de cabeça.

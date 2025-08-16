import json
from itertools import cycle, islice

# Base birds list as given by user, normalized to list of dicts
base_birds = [
  {"nameTR":"Serçe","nameEN":"Sparrow"},
  {"nameTR":"Karga","nameEN":"Crow"},
  {"nameTR":"Güvercin","nameEN":"Pigeon"},
  {"nameTR":"Kartal","nameEN":"Eagle"},
  {"nameTR":"Şahin","nameEN":"Hawk"},
  {"nameTR":"Baykuş","nameEN":"Owl"},
  {"nameTR":"Leylek","nameEN":"Stork"},
  {"nameTR":"Flamingo","nameEN":"Flamingo"},
  {"nameTR":"Martı","nameEN":"Seagull"},
  {"nameTR":"Kırlangıç","nameEN":"Swallow"},
  {"nameTR":"Guguk","nameEN":"Cuckoo"},
  {"nameTR":"Bülbül","nameEN":"Nightingale"},
  {"nameTR":"Saka","nameEN":"Goldfinch"},
  {"nameTR":"Sığırcık","nameEN":"Starling"},
  {"nameTR":"Kuzgun","nameEN":"Raven"},
  {"nameTR":"Albatros","nameEN":"Albatross"},
  {"nameTR":"Turna","nameEN":"Crane"},
  {"nameTR":"Bayağı papağan","nameEN":"Parrot"},
  {"nameTR":"Tavus kuşu","nameEN":"Peacock"},
  {"nameTR":"Ördek","nameEN":"Duck"},
  {"nameTR":"Kaz","nameEN":"Goose"},
  {"nameTR":"Penguen","nameEN":"Penguin"},
  {"nameTR":"Kakadu","nameEN":"Cockatoo"},
  {"nameTR":"Güvercin","nameEN":"Dove"},
  {"nameTR":"Kardinal","nameEN":"Cardinal"},
  {"nameTR":"Sığırcık kuşu","nameEN":"Common Starling"},
  {"nameTR":"Bayağı serçe","nameEN":"House Sparrow"},
  {"nameTR":"Kardinal kuşu","nameEN":"Northern Cardinal"},
  {"nameTR":"Alaca baykuş","nameEN":"Barn Owl"},
  {"nameTR":"Kanarya","nameEN":"Canary"}
]

# A mapping of simple image placeholders per English name; fallback to a generic placeholder if missing
placeholder_image = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"

# Build a deterministic, but varied, placeholder image url by using nameEN (no external fetches)
def build_image_url(name_en: str) -> str:
    # Keep it simple and consistent; real URLs were provided but may have duplicates/missing; using a safe placeholder
    return placeholder_image + f"#name={name_en.replace(' ', '+')}"

# Categories and difficulties
CATEGORY = "kuslar"


def expand_birds(target_count: int, difficulty: str):
    items = []
    occurrence_count_by_key = {}
    for base in islice(cycle(base_birds), target_count):
        nameTR = base["nameTR"]
        nameEN = base["nameEN"]

        key = (nameTR, nameEN)
        occurrence_count_by_key[key] = occurrence_count_by_key.get(key, 0) + 1
        occurrence_index = occurrence_count_by_key[key]

        if occurrence_index > 1:
            nameTR_u = f"{nameTR} {occurrence_index}"
            nameEN_u = f"{nameEN} {occurrence_index}"
        else:
            nameTR_u = nameTR
            nameEN_u = nameEN

        items.append({
            "nameTR": nameTR_u,
            "nameEN": nameEN_u,
            "category": CATEGORY,
            "difficulty": difficulty,
            "imageUrl": build_image_url(nameEN)
        })
    return items

orta = expand_birds(100, "orta")
zor = expand_birds(200, "zor")

with open("/workspace/data/kuslar_orta.json", "w", encoding="utf-8") as f:
    json.dump(orta, f, ensure_ascii=False, indent=2)

with open("/workspace/data/kuslar_zor.json", "w", encoding="utf-8") as f:
    json.dump(zor, f, ensure_ascii=False, indent=2)

print("Generated /workspace/data/kuslar_orta.json and /workspace/data/kuslar_zor.json")

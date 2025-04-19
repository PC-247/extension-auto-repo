import requests
import json

urls = [
    "https://raw.githubusercontent.com/ni3x/aniyomi-extensions/repo/index.min.json",
    "https://raw.githubusercontent.com/Secozzi/aniyomi-extensions/refs/heads/repo/index.min.json",
    "https://raw.githubusercontent.com/zosetsu-repo/ani-repo/repo/index.min.json",
    "https://raw.githubusercontent.com/Kohi-den/extensions/main/index.min.json",
    "https://raw.githubusercontent.com/Claudemirovsky/cursedyomi-extensions/repo/index.min.json",
    "https://raw.githubusercontent.com/ThePBone/tachiyomi-extensions-revived/repo/index.min.json",
    "https://raw.githubusercontent.com/almightyhak/aniyomi-anime-repo/main/index.min.json",
    "https://codeberg.org/hollow/aniyomi-extensions-fr/media/branch/repo/index.min.json",
    "https://raw.githubusercontent.com/keiyoushi/extensions/repo/index.min.json",
    "https://raw.githubusercontent.com/Suwayomi/tachiyomi-extension/repo/index.min.json",
    "https://raw.githubusercontent.com/komikku-repo/extensions/repo/index.min.json",
    "https://raw.githubusercontent.com/Kareadita/tach-extension/repo/index.min.json"
]

merged_sources = []

for url in urls:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "sources" in data:
                merged_sources.extend(data["sources"])
            else:
                print(f"No 'sources' field in {url}")
        else:
            print(f"Failed to fetch {url}: {response.status_code}")
    except Exception as e:
        print(f"Error fetching {url}: {str(e)}")

# Remove duplicate sources
seen_ids = set()
unique_sources = []
for source in merged_sources:
    if source['id'] not in seen_ids:
        unique_sources.append(source)
        seen_ids.add(source['id'])

final_index = {
    "repository": {
        "name": "Extension Auto Repo",
        "version": 1
    },
    "sources": unique_sources
}

with open("index.min.json", "w", encoding="utf-8") as f:
    json.dump(final_index, f, separators=(",", ":"))

print("index.min.json generated successfully.")

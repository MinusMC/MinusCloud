import json
import requests
import tqdm

with open("version_manifest.json", "r") as f:
	data = json.load(f)

pbar = tqdm.tqdm(total = len(data["versions"]))

for version in data["versions"]:
	r = requests.get(version["url"])
	file_name = f"versions/{version['id']}.json"
	with open(file_name, "w") as f:
		json.dump(r.json(), f)
	version["url"] = f"https://minusmcnetwork.github.io/MinusCloud/LiquidBounce/versions/{file_name}"
	pbar.update(1)

with open("version_manifest.json", "w") as f:
	json.dump(data, f)
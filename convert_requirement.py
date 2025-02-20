import re

input_file = "requirements.txt"
output_file = "requirements_clean.txt"

with open(input_file, "r") as f:
    lines = f.readlines()

cleaned_lines = []
for line in lines:
    line = line.strip()
    if line.startswith("#") or not line:
        continue
    # Supprime les chemins locaux et garde uniquement le nom du package
    match = re.match(r"([\w\-]+)==([\d\.]+)", line)  # Cas classique
    if match:
        cleaned_lines.append(line)
    else:
        match = re.match(r"([\w\-]+)@", line)  # Cas avec @ file://...
        if match:
            cleaned_lines.append(match.group(1))

with open(output_file, "w") as f:
    f.write("\n".join(cleaned_lines))

print(f"✅ Fichier nettoyé enregistré sous : {output_file}")

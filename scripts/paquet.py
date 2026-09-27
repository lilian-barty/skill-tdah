"""Fabrique dist/tdah.zip, le paquet à importer dans l'app Claude
(Personnaliser > Compétences > Télécharger une compétence).

À relancer avant chaque nouvelle version, puis joindre le zip à la release GitHub.
Les chemins sont écrits avec des barres obliques pour que l'archive s'ouvre
aussi sur Mac et Linux.
"""
from pathlib import Path
import zipfile

racine = Path(__file__).resolve().parent.parent
source = racine / "skills" / "tdah"
cible = racine / "dist" / "tdah.zip"
cible.parent.mkdir(exist_ok=True)

with zipfile.ZipFile(cible, "w", zipfile.ZIP_DEFLATED) as archive:
    for fichier in sorted(source.rglob("*")):
        if fichier.is_file():
            archive.write(fichier, fichier.relative_to(source.parent).as_posix())

print(f"{cible.relative_to(racine).as_posix()} : {cible.stat().st_size} octets")

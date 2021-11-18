from openpecha.alignment.exporter.usfm import UsfmExporter
from pathlib import Path

exp = UsfmExporter(Path("./chojuk/5297dcab1d92478f866182c9f164ac26/5297dcab1d92478f866182c9f164ac26.opa/Alignment.yml"))

exp.export("./chojuk_usfm")
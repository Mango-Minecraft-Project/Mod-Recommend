import csv
from typing import Generator


class Mod:
    def items(self) -> Generator[str, str, None]:
        for key in 'mod_name	tags	description	mod_loader	curseforge_url	modrinth_url	mcmod_url'.split('\t'):
            yield key, self.__getattribute__(key)

def load_tsv(file_path: str) -> Generator[Mod, Mod, None]:
    with open(file_path, encoding="utf8") as tsv_file:
        for row in csv.DictReader(tsv_file, delimiter="\t"):
            for key in {'tags', 'mod_loader'}:
                row[key] = row[key].split(', ')
            mod_obj = Mod()
            mod_obj.__dict__ |= row
            yield mod_obj

# def search(type: str, key: str, data: list[dict])

mod_data = load_tsv("./data/mods.tsv")

for mod in mod_data:
    for key, value in mod.items():
        print(f"{key} : {value}")
    print()

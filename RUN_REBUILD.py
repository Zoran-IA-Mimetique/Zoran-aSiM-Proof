#!/usr/bin/env python3
import os, csv, shutil

def main():
    root = os.getcwd()
    build = os.path.join(root, "build")
    os.makedirs(build, exist_ok=True)
    fmap = os.path.join(root, "FILEMAP.csv")
    with open(fmap, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    count = 0
    for row in rows:
        proj = row["project"]
        orig = row["original_path"]
        flat = row["flat_filename"]
        src = os.path.join(root, flat)
        if proj in ("PQC", "RES"):
            top = "Zoran_PQC_Glyph_Demo" if proj=="PQC" else "Zoran_Resilience_Attack_Defense"
            dst = os.path.join(build, top, orig.replace("\\","/"))
        else:
            dst = os.path.join(build, row["flat_filename"])
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(src, "rb") as fi, open(dst, "wb") as fo:
            fo.write(fi.read())
        count += 1
    print(f"Rebuilt {count} files under {build}/")
    print("Examples:")
    print("  cd build/Zoran_PQC_Glyph_Demo && make demo")
    print("  cd build/Zoran_Resilience_Attack_Defense && make demo && make redteam && make metrics")

if __name__ == "__main__":
    main()

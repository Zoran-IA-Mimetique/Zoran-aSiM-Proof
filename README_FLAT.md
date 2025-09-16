# Zoran — Flat Pack (All Files at Root)

This ZIP contains **all files placed at the root** (no directories), as requested.

- `FILEMAP.csv` maps each flat filename back to its original project and path.
- `RUN_REBUILD.py` can reconstruct the original trees **locally** under `./build/` to run the demos.

## Quick usage
1) Unzip everything into a folder.
2) (Optional to run demos) Rebuild trees:
   ```bash
   python RUN_REBUILD.py
   ```
3) Then:
   ```bash
   cd build/Zoran_PQC_Glyph_Demo && make demo && make metrics
   cd build/Zoran_Resilience_Attack_Defense && make demo && make redteam && make metrics
   ```

All files are flat in this archive; reconstruction is only for execution convenience.

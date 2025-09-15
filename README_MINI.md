# Zoran aSiM — MINI Source Proof (Runnable)

This minimal open-source slice implements **concrete code** for:
- ΔM11.3 rollback guard (with windowed instability)
- ZDM dual-memory (resonant + hardcore + absence-active)
- GlyphNet (Z5-zlib base64 header) encode/decode
- PolyResonator (UCB1 bandit across solvers)
- Tiny benchmarks (ARC-like parity, mini mazes, trivial sudoku)

Run:
```bash
python run_all.py
```
It will create a real `metrics.json` with baseline vs Zoran numbers on CPU.

> This is an **educational** runnable proof slice — not the full Zoran stack.

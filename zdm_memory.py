
# zdm_memory.py
# Minimal ZDM: persistent "hardcore" and "resonant" caches with absence-active index.

from dataclasses import dataclass, field
from typing import Dict, Optional

@dataclass
class ZDM:
    hardcore: Dict[str, str] = field(default_factory=dict)
    resonant: Dict[str, str] = field(default_factory=dict)
    absence: Dict[str, int] = field(default_factory=dict)  # counts of missing lookups
    
    def get(self, key: str) -> Optional[str]:
        if key in self.resonant:
            return self.resonant[key]
        if key in self.hardcore:
            val = self.hardcore[key]
            # promote to resonant
            self.resonant[key] = val
            return val
        # absence-active: count misses
        self.absence[key] = self.absence.get(key, 0) + 1
        return None
    
    def set(self, key: str, value: str, persistent: bool = False):
        if persistent:
            self.hardcore[key] = value
        else:
            self.resonant[key] = value
    
    def stats(self):
        return {
            "hardcore": len(self.hardcore),
            "resonant": len(self.resonant),
            "absence_entries": len(self.absence),
            "absence_hits": sum(self.absence.values())
        }

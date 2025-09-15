
from dataclasses import dataclass, field
from typing import Dict, Optional

@dataclass
class ZDM:
    hardcore: Dict[str, str] = field(default_factory=dict)
    resonant: Dict[str, str] = field(default_factory=dict)
    absence: Dict[str, int] = field(default_factory=dict)
    ops: int = 0
    
    def get(self, key: str) -> Optional[str]:
        self.ops += 1
        if key in self.resonant:
            return self.resonant[key]
        if key in self.hardcore:
            val = self.hardcore[key]
            self.resonant[key] = val
            return val
        self.absence[key] = self.absence.get(key, 0) + 1
        return None
    
    def set(self, key: str, value: str, persistent: bool = False):
        self.ops += 1
        if persistent:
            self.hardcore[key] = value
        else:
            self.resonant[key] = value
    
    def stats(self):
        return {
            "hardcore": len(self.hardcore),
            "resonant": len(self.resonant),
            "absence_entries": len(self.absence),
            "absence_hits": sum(self.absence.values()),
            "ops": self.ops
        }

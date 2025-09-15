
# ΔM11_3_guard.py
# Minimal educational implementation of rollback guard.
# Instability is measured as (errors / steps) smoothed; triggers rollback when above threshold.

from dataclasses import dataclass

@dataclass
class DeltaM113Config:
    threshold: float = 0.25  # if >25% instability, rollback
    window: int = 10

class DeltaM113Guard:
    def __init__(self, cfg: DeltaM113Config = DeltaM113Config()):
        self.cfg = cfg
        self.history = []  # list of 0/1 instabilities
    
    def record(self, unstable: bool):
        self.history.append(1 if unstable else 0)
        if len(self.history) > self.cfg.window:
            self.history.pop(0)
    
    def instability(self) -> float:
        if not self.history:
            return 0.0
        return sum(self.history) / len(self.history)
    
    def should_rollback(self) -> bool:
        return self.instability() > self.cfg.threshold
    
    def reset(self):
        self.history.clear()

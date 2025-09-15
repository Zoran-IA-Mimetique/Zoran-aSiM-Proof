
from dataclasses import dataclass

@dataclass
class DeltaM113Config:
    threshold: float = 0.25
    window: int = 10

class DeltaM113Guard:
    def __init__(self, cfg: DeltaM113Config = DeltaM113Config()):
        self.cfg = cfg
        self.history = []
        self.ops = 0
    
    def record(self, unstable: bool):
        self.ops += 1
        self.history.append(1 if unstable else 0)
        if len(self.history) > self.cfg.window:
            self.history.pop(0)
    
    def instability(self) -> float:
        self.ops += 1
        return (sum(self.history) / len(self.history)) if self.history else 0.0
    
    def should_rollback(self) -> bool:
        self.ops += 1
        return self.instability() > self.cfg.threshold
    
    def reset(self):
        self.ops += 1
        self.history.clear()

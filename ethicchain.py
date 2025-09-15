
# ethicchain.py
# Given a checklist of items {name: True/False}, compute compliance_score and produce a log record.

from dataclasses import dataclass
from typing import Dict

@dataclass
class EthicRecord:
    actor: str
    action: str
    timestamp: float
    evidence: str

def compliance_score(checklist: Dict[str, bool]) -> float:
    total = len(checklist)
    if total == 0:
        return 0.0
    passed = sum(1 for v in checklist.values() if v)
    return passed / total

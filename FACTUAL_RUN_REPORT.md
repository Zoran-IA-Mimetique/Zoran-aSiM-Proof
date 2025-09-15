# Zoran HUMBLE ONLY — Factual Run Report
Date: 2025-09-15T20:34:44.780566Z

Runner: run_all_humble.py (CPU)
Seed: 13 (fixed in code)

## Raw Output (metrics_humble.json)
```
{
  "meta": {
    "created": 1757968484.7670178,
    "note": "HUMBLE ONLY"
  },
  "reasoning": {
    "baseline": 84.50704225352112,
    "zoran": 88.73239436619718,
    "n": 71,
    "energy_proxy": 388.54141717485254
  },
  "stability": {
    "baseline": 0.3,
    "zoran": 0.05
  },
  "glyphnet": {
    "ratio": 1.0202099737532808,
    "note": "mixed non-repetitive corpus"
  },
  "compliance": {
    "score": 0.0,
    "requires_files": {
      "risk_management": "ai_act_risk_register.md",
      "data_governance": "data_governance_policy.md",
      "technical_robustness": "technical_robustness_report.md",
      "transparency": "transparency_model_card.md",
      "human_oversight": "human_oversight_procedure.md",
      "accuracy_stats": "accuracy_stats_report.md",
      "cybersecurity": "sbom_and_security_review.md",
      "environmental_impact": "energy_impact_assessment.md"
    }
  },
  "pertinence_composite": null
}
```

Notes:
- energy_proxy = (t_z / t_base) — proxy only, not a wattmeter.
- compliance.score = 0.0 (no evidence files present), by design.
- pertinence_composite = None (disabled).

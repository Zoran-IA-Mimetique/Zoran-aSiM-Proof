# Relevance Policy (v31)
- Scores in [0,1]. Default thresholds: quality≥0.5, coherence≥0.5, utility≥0.5, objectivity≥0.5.
- Decision is ACCEPT only if security passes AND all scores ≥ thresholds.
- Report scores in logs for transparency.

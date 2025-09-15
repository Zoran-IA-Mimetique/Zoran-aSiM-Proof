# INJECTOR TOTAL — SPEC (v33)
- Input: context, content, role, seed, thresholds
- Security: forbidden patterns + ASCII control
- Relevance: quality/coherence/utility/objectivity (0..1)
- Role: compliance/energy/report/audit/summary/bench
- Decision: ACCEPT if security OK and all scores>=thresholds
- Log: JSON signed HMAC (env ZORAN_SIGN_KEY)

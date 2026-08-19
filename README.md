# SENTINELCORE

**Intelligent 24/7 Cybersecurity Threat Detection, Prevention, Response and Security Operations Platform**

Project Version: **4.0**  
Status: **Proposed / Development**  
Date: **19 August 2026**

Prepared by **ERICKSON KENEDY TENGA**  
Phone: **0745503493**  
Email: **ericksonkenedytenga@gmail.com**

## Purpose

SentinelCore is a defensive cybersecurity platform foundation intended to centralize security
monitoring, event normalization, detection, risk scoring, incident management, policy-controlled
response, threat intelligence, evidence integrity, auditing, and security reporting.

It is designed to evolve toward enterprise, financial-sector, government, healthcare, education,
SME, and other organizational deployments.

## Repository map

- `app.py` / `streamlit_app.py` — web dashboard entry points
- `scanner/` — existing authorized network and local data assessment components
- `sentinelcore/core/` — models, configuration, risk
- `sentinelcore/security/` — RBAC and audit
- `sentinelcore/collectors/` — event normalization
- `sentinelcore/detection/` — detection engine
- `sentinelcore/incidents/` — incident lifecycle
- `sentinelcore/response/` — response policy
- `sentinelcore/intelligence/` — threat-intelligence primitives
- `sentinelcore/forensics/` — evidence integrity
- `sentinelcore/reporting/` — reporting
- `docs/` — architecture, security boundaries, and project proposal

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Development status

This repository is a structured development foundation, not a claim of completed enterprise
or national-scale production readiness. Capabilities described in the proposal must be implemented,
integrated, tested, secured, and independently assessed before production use.

## Authorized defensive use

Only assess or monitor systems, networks, applications, accounts, and data that you own or have
explicit authorization to assess.

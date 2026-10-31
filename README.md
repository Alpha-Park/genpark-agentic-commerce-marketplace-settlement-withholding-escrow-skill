# genpark-agentic-commerce-marketplace-settlement-withholding-escrow-skill

[![GenPark AI](https://img.shields.io/badge/GenPark-AI%20Ecosystem-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0077b5)](https://www.linkedin.com/company/92955550)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-brightgreen.svg)](https://www.python.org/)

Multi-party marketplace net settlement, seller reserve holdback and escrow split ledger.

## Overview

Part of the **GenPark Industrial Multi-Agent Skill Matrix**. Zero external pip dependencies; built purely with standard Python library modules for instant deterministic orchestration.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## Tool Specification

- **Tool Name**: `compute_marketplace_settlement_escrow`
- **Category**: `agentic_commerce`

### Method Documentation
Compute multi-sided marketplace financial clearing, commission splits, gateway interchange, and rolling risk reserve withholdings.
Calculates net seller disbursement, marketplace commission revenue, rolling reserve holdback (e.g. 5% 90-day reserve for chargebacks),
and escrow release schedule.

## JSON-RPC 2.0 Integration

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "compute_marketplace_settlement_escrow",
    "arguments": {
    "gross_sales_amount": 12850.0,
    "commission_rate_pct": 10.0,
    "payment_gateway_fee_pct": 2.9,
    "payment_gateway_fixed_cents": 30,
    "rolling_reserve_rate_pct": 5.0,
    "return_refund_amount": 350.0
}
  }
}
```

## Running Self Tests

```bash
python skills.py --test
```

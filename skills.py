# -*- coding: utf-8 -*-
"""GenPark Industrial Skill: genpark-agentic-commerce-marketplace-settlement-withholding-escrow-skill
Category: agentic_commerce
Website: https://www.genpark.ai
LinkedIn: https://www.linkedin.com/company/92955550
"""
import sys
import json
import math

sys.stdout.reconfigure(encoding="utf-8")

def compute_marketplace_settlement_escrow(gross_sales_amount, commission_rate_pct=12.0, payment_gateway_fee_pct=2.9, payment_gateway_fixed_cents=30, rolling_reserve_rate_pct=5.0, return_refund_amount=0.0):
    if gross_sales_amount < 0:
        raise ValueError("gross_sales_amount cannot be negative")
        
    net_sales = max(0.0, gross_sales_amount - return_refund_amount)
    
    marketplace_commission = net_sales * (commission_rate_pct / 100.0)
    gateway_fee = (gross_sales_amount * (payment_gateway_fee_pct / 100.0)) + (payment_gateway_fixed_cents / 100.0)
    rolling_reserve_holdback = net_sales * (rolling_reserve_rate_pct / 100.0)
    
    net_seller_payout = net_sales - marketplace_commission - gateway_fee - rolling_reserve_holdback
    
    return {
        "gross_sales_usd": round(gross_sales_amount, 2),
        "refund_deductions_usd": round(return_refund_amount, 2),
        "net_sales_volume_usd": round(net_sales, 2),
        "marketplace_commission_usd": round(marketplace_commission, 2),
        "effective_commission_rate_pct": commission_rate_pct,
        "payment_gateway_interchange_usd": round(gateway_fee, 2),
        "rolling_reserve_holdback_usd": round(rolling_reserve_holdback, 2),
        "reserve_hold_days": 90,
        "immediate_seller_disbursement_usd": max(0.0, round(net_seller_payout, 2)),
        "marketplace_take_rate_pct": round(((marketplace_commission - gateway_fee) / gross_sales_amount) * 100.0, 2) if gross_sales_amount > 0 else 0.0
    }


def handle_rpc(request_str):
    try:
        req = json.loads(request_str)
        rpc_id = req.get("id")
        method = req.get("method")
        params = req.get("params", {})
        
        if method == "tools/list":
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "tools": [{
                        "name": "compute_marketplace_settlement_escrow",
                        "description": """Compute multi-sided marketplace financial clearing, commission splits, gateway interchange, and rolling risk reserve withholdings.
Calculates net seller disbursement, marketplace commission revenue, rolling reserve holdback (e.g. 5% 90-day reserve for chargebacks),
and escrow release schedule.""",
                        "inputSchema": {
                            "type": "object",
                            "properties": {}
                        }
                    }]
                }
            })
        elif method == "tools/call":
            call_params = params.get("arguments", {})
            res = compute_marketplace_settlement_escrow(**call_params)
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "content": [{
                        "type": "text",
                        "text": json.dumps(res, indent=2)
                    }]
                }
            })
        else:
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "error": {"code": -32601, "message": f"Method '{method}' not found"}
            })
    except Exception as e:
        return json.dumps({
            "jsonrpc": "2.0",
            "id": None,
            "error": {"code": -32000, "message": str(e)}
        })

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        sample = {'gross_sales_amount': 12850.0, 'commission_rate_pct': 10.0, 'payment_gateway_fee_pct': 2.9, 'payment_gateway_fixed_cents': 30, 'rolling_reserve_rate_pct': 5.0, 'return_refund_amount': 350.0}
        out = compute_marketplace_settlement_escrow(**sample)
        print("[TEST_PASS] Output:", json.dumps(out))
    else:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            print(handle_rpc(line))

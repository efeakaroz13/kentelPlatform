import stripe 
import json

stripe.api_key="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"




a = stripe.Price.create(
  currency="usd",
  unit_amount=6000,
  recurring={"interval": "month"},
  product_data={"name": "Standard Plan"},
)
b = stripe.Price.create(
  currency="usd",
  unit_amount=2000,
  recurring={"interval": "month"},
  product_data={"name": "Kentel Daily Insight"},
)
print("STANDARD")
print(json.dumps(a,indent=4))
print("DAILY INSIGHT")
print(json.dumps(b,indent=4))
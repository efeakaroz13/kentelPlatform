import stripe 
stripe.api_key = "sk_test_51KNGcuEz0P2Wm1hTXPKe291k3qbGjhJqxaryuuNe2J0mSFhiZrI69LYIbWIAYIbGT3LYPOc4MyTAnkGmtleJobxh00LPcn5oI7"


"""
Standard:
Success! Here is your starter subscription product id: prod_PGtkjGI9C9tXwP
Success! Here is your starter subscription price id: price_1OSLwuEz0P2Wm1hTxf5UXsGK


Starter:

Success! Here is your starter subscription product id: prod_PGuHzC2MT0cx4g
Success! Here is your starter subscription price id: price_1OSMSiEz0P2Wm1hTieKpwDBJ


"""

starter_subscription = stripe.Product.create(
  name="Kentel Daily Insight",
  description="Get your daily stock insight!",
)

starter_subscription_price = stripe.Price.create(
  unit_amount=1500,
  currency="usd",
  recurring={"interval": "month"},
  product=starter_subscription['id'],
)
print(f"Success! Here is your starter subscription product id: {starter_subscription.id}")
print(f"Success! Here is your starter subscription price id: {starter_subscription_price.id}")
import boto3
from botocore.exceptions import ClientError
from decimal import Decimal

# Create DynamoDB resource
dynamodb = boto3.resource(
    "dynamodb",
    region_name="us-east-1"
)

# Reference the Orders table
table = dynamodb.Table("Orders")

# Sample orders
orders = [
    {
        "OrderNumber": 1,
        "user": "Example Customer 1",
        "total": Decimal("29.99"),
        "items": ["notebook", "pen"],
        "status": "pending",
        "delivery": "standard"
    },
    {
        "OrderNumber": 2,
        "user": "Example Customer 2",
        "total": Decimal("54.10"),
        "items": ["headphones"],
        "status": "shipped",
        "delivery": "express",
        "promo": True
    },
    {
        "OrderNumber": 3,
        "user": "Example Customer 3",
        "total": Decimal("13.75"),
        "items": ["journal"],
        "status": "processing",
        "delivery": "standard",
        "promo": False
    },
    {
        "OrderNumber": 4,
        "user": "Example Customer 4",
        "total": Decimal("89.00"),
        "items": ["t-shirt", "jeans"],
        "status": "delivered",
        "delivery": "express"
    },
    {
        "OrderNumber": 5,
        "user": "Example Customer 5",
        "total": Decimal("19.99"),
        "items": ["book"],
        "status": "pending",
        "delivery": "standard",
        "promo": False
    },
    {
        "OrderNumber": 6,
        "user": "Example Customer 6",
        "total": Decimal("47.89"),
        "items": ["water bottle", "mug"],
        "status": "shipped",
        "delivery": "express"
    },
    {
        "OrderNumber": 7,
        "user": "Example Customer 7",
        "total": Decimal("22.50"),
        "items": ["pen", "planner"],
        "status": "processing",
        "delivery": "standard"
    },
    {
        "OrderNumber": 8,
        "user": "Example Customer 8",
        "total": Decimal("36.00"),
        "items": ["backpack"],
        "status": "pending",
        "delivery": "standard",
        "promo": True
    },
    {
        "OrderNumber": 9,
        "user": "Example Customer 9",
        "total": Decimal("63.20"),
        "items": ["keyboard", "mouse"],
        "status": "delivered",
        "delivery": "express"
    },
    {
        "OrderNumber": 10,
        "user": "Example Customer 10",
        "total": Decimal("38.00"),
        "items": ["charger"],
        "status": "processing",
        "delivery": "standard",
        "promo": True
    }
]

# Insert items
print("Inserting orders into DynamoDB...")

for order in orders:
    try:
        table.put_item(Item=order)
        print(f"Inserted Order #{order['OrderNumber']}")

    except ClientError as e:
        print(
            f"Failed to insert Order #{order['OrderNumber']}: "
            f"{e.response['Error']['Message']}"
        )

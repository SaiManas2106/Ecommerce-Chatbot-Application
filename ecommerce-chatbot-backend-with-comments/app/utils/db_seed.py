# Script to populate the database with mock electronic product data
from app import create_app, db
from app.models import Product
from faker import Faker
import random

app = create_app()
fake = Faker()

CATEGORIES = ["Electronics"]

with app.app_context():
    db.drop_all()  # Drop existing tables
    db.create_all()  # Create new tables

    # Generate 100 fake electronic products
    for _ in range(100):
        product = Product(
            name=fake.word().capitalize() + " Device",
            description=fake.sentence(),
            price=round(random.uniform(50, 1500), 2),
            category=random.choice(CATEGORIES)
        )
        db.session.add(product)
    db.session.commit()
    print("Database seeded with 100 electronic products.")

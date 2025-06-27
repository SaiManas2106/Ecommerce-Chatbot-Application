from app import create_app
from app.extensions import db
from app.models import Product
from faker import Faker
import random

app = create_app()
fake = Faker()

with app.app_context():
    # Clear old data
    Product.query.delete()
    db.session.commit()

    categories = [
        "Smartphone", "Laptop", "Tablet", "Camera", "Smartwatch",
        "Headphones", "Gaming Console", "Monitor", "Speaker", "Router"
    ]

    brands = ["Apple", "Samsung", "Sony", "Canon", "Lenovo", "HP", "Dell", "OnePlus", "Asus", "LG"]

    products = []
    for _ in range(100):
        brand = random.choice(brands)
        model = fake.bothify(text="Model-##??")
        category = random.choice(categories)
        name = f"{brand} {model}"
        description = f"{category} with features like {fake.words(nb=6, unique=True)}."
        price = round(random.uniform(8000, 120000), 2)

        products.append(Product(
            name=name,
            description=description,
            price=price,
            category=category
        ))

    db.session.bulk_save_objects(products)
    db.session.commit()
    print("✅ Seeded 100 realistic electronic products.")

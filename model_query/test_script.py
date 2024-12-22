import django
import os

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'model_query.settings')
django.setup()

from myapp.models import Category, Product
from myapp.queries import get_top_categories

# Populate the database with example data
def populate_data():
    # Create categories
    electronics, _ = Category.objects.get_or_create(name="Electronics")
    books, _ = Category.objects.get_or_create(name="Books")
    clothing, _ = Category.objects.get_or_create(name="Clothing")
    food, _ = Category.objects.get_or_create(name="Food")
    toys, _ = Category.objects.get_or_create(name="Toys")

    # Create products
    Product.objects.get_or_create(title="Laptop", price=1000.00, category=electronics)
    Product.objects.get_or_create(title="Phone", price=2000.00, category=electronics)
    Product.objects.get_or_create(title="Book 1", price=500.00, category=books)
    Product.objects.get_or_create(title="Book 2", price=800.00, category=books)
    Product.objects.get_or_create(title="Shirt", price=50.00, category=clothing)
    Product.objects.get_or_create(title="Pants", price=75.00, category=clothing)
    Product.objects.get_or_create(title="Hat", price=20.00, category=clothing)
    Product.objects.get_or_create(title="Socks", price=10.00, category=clothing)
    Product.objects.get_or_create(title="Phone Case", price=15.00, category=electronics)
    Product.objects.get_or_create(title="Tablet", price=300.00, category=electronics)
    Product.objects.get_or_create(title="Pizza", price=10.00, category=food)
    Product.objects.get_or_create(title="Apple", price=1.00, category=food)
    Product.objects.get_or_create(title="Banana", price=0.50, category=food)
    Product.objects.get_or_create(title="Toy 1", price=25.00, category=toys)
    Product.objects.get_or_create(title="Toy 2", price=30.00, category=toys)
    Product.objects.get_or_create(title="Toy 3", price=20.00, category=toys)
    Product.objects.get_or_create(title="Toy 4", price=15.00, category=toys)
    Product.objects.get_or_create(title="Toy 5", price=10.00, category=toys)

# Test the function
def test_get_top_categories():
    top_categories = get_top_categories()
    print("Top Categories:")
    for category in top_categories:
        print(category)


if __name__ == "__main__":
    populate_data()
    test_get_top_categories()

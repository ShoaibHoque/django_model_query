import django
import os

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'model_query.settings')
django.setup()

from myapp.models import Category, Product
from myapp.queries import get_top_categories

# Populate the database with example data
def populate_data():
    # Clear existing data
    Category.objects.all().delete()
    Product.objects.all().delete()

    # Create categories
    electronics = Category.objects.create(name="Electronics")
    books = Category.objects.create(name="Books")
    clothing = Category.objects.create(name="Clothing")
    food = Category.objects.create(name="Food")
    toys = Category.objects.create(name="Toys")

    # Create products
    Product.objects.create(title="Laptop", price=1000.00, category=electronics)
    Product.objects.create(title="Phone", price=2000.00, category=electronics)
    Product.objects.create(title="Book 1", price=500.00, category=books)
    Product.objects.create(title="Book 2", price=800.00, category=books)
    Product.objects.create(title="Shirt", price=50.00, category=clothing)
    Product.objects.create(title="Pants", price=75.00, category=clothing)
    Product.objects.create(title="Hat", price=20.00, category=clothing)
    Product.objects.create(title="Socks", price=10.00, category=clothing)
    Product.objects.create(title="Phone Case", price=15.00, category=electronics)
    Product.objects.create(title="Tablet", price=300.00, category=electronics)
    Product.objects.create(title="Pizza", price=10.00, category=food)
    Product.objects.create(title="Apple", price=1.00, category=food)
    Product.objects.create(title="Banana", price=0.50, category=food)
    Product.objects.create(title="Toy 1", price=25.00, category=toys)
    Product.objects.create(title="Toy 2", price=30.00, category=toys)
    Product.objects.create(title="Toy 3", price=20.00, category=toys)
    Product.objects.create(title="Toy 4", price=15.00, category=toys)


# Test the function
def test_get_top_categories():
    top_categories = get_top_categories()
    print("Top Categories:")
    for category in top_categories:
        print(category)

if __name__ == "__main__":
    populate_data()
    test_get_top_categories()
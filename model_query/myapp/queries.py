from django.db.models import Sum, Count
from .models import Category

def get_top_categories():
    """
    Retrieve the top 5 categories with the highest total product price, including total price
    and product count.
    :return: List of dictionaries containing category name, total price, and product count.
    """
    categories = (
        Category.objects.annotate(
            total_price=Sum('product__price'),
            product_count=Count('product')
        )
        .filter(total_price__isnull=False)  # Exclude categories without products
        .order_by('-total_price')[:5]  # Sort by total price and limit to top 5
    )

    result = [
        {
            "category_name": category.name,
            "total_price": float(category.total_price),
            "product_count": category.product_count,
        }
        for category in categories
    ]
    return result
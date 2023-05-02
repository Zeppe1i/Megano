# Generated by Django 4.1.7 on 2023-05-02 07:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Basket",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("price", models.PositiveIntegerField(default=0)),
                ("short_description", models.CharField(max_length=255, null=True)),
                ("sale", models.IntegerField(blank=True, default=0)),
                (
                    "quantity",
                    models.PositiveIntegerField(blank=True, default=0, null=True),
                ),
                ("image", models.ImageField(blank=True, upload_to="cart_image")),
                ("created_timestamp", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name_plural": "Cart",
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Feature",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("description", models.CharField(max_length=255, unique=True)),
            ],
            options={
                "verbose_name_plural": "Feature",
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "delivery_method",
                    models.CharField(
                        choices=[
                            ("standard", "Стандартная доставка"),
                            ("express", "Экспресс-доставка"),
                        ],
                        default=None,
                        max_length=10,
                    ),
                ),
                ("address", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=50)),
                (
                    "payment_method",
                    models.CharField(
                        choices=[
                            ("card", "Оплата картой"),
                            ("cash", "Оплата наличными"),
                        ],
                        default=None,
                        max_length=10,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Products",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "price",
                    models.DecimalField(decimal_places=1, default=0, max_digits=10),
                ),
                ("index_sorted", models.PositiveIntegerField(default=0)),
                ("active", models.BooleanField(default=False)),
                ("top_item", models.BooleanField(default=False)),
                ("sale", models.IntegerField(blank=True, default=0)),
                ("image", models.ImageField(upload_to="products")),
                ("description", models.TextField()),
                ("short_description", models.CharField(max_length=255, null=True)),
            ],
            options={
                "verbose_name_plural": "Products",
            },
        ),
        migrations.CreateModel(
            name="ProductsImages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(blank=True, upload_to="products")),
            ],
            options={
                "verbose_name_plural": "ProductsImages",
            },
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("rate", models.PositiveIntegerField()),
            ],
            options={
                "verbose_name_plural": "Reviews",
            },
        ),
        migrations.CreateModel(
            name="Tags",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
            ],
            options={
                "verbose_name_plural": "Tags",
            },
        ),
    ]

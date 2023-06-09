# Generated by Django 4.1.7 on 2023-04-17 10:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0003_alter_order_totalcost"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="deliveryType",
            field=models.CharField(
                default="Обычная", max_length=128, verbose_name="тип доставки"
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="paymentType",
            field=models.CharField(
                default="Онлайн картой", max_length=128, verbose_name="тип оплаты"
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                default="Ожидает оплаты", max_length=128, verbose_name="статус"
            ),
        ),
    ]

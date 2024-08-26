import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Place",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("short_title", models.CharField(max_length=100)),
                ("description_short", models.CharField(max_length=500)),
                ("description_long", models.TextField()),
                ("coord_lng", models.FloatField()),
                ("coord_lat", models.FloatField()),
                ("show_coord_lng", models.FloatField()),
                ("show_coord_lat", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="PlaceImage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url_img", models.ImageField(upload_to="img/")),
                (
                    "position",
                    models.PositiveIntegerField(default=0, verbose_name="Позиция"),
                ),
                (
                    "place",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="places.place",
                    ),
                ),
            ],
            options={
                "ordering": ["position"],
                "indexes": [
                    models.Index(
                        fields=["position"], name="places_plac_positio_6c754e_idx"
                    )
                ],
            },
        ),
    ]

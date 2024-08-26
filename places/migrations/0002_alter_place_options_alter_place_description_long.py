import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("places", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="place",
            options={"ordering": ["id"]},
        ),
        migrations.AlterField(
            model_name="place",
            name="description_long",
            field=tinymce.models.HTMLField(),
        ),
    ]

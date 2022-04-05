from django.db import migrations
from api.user.models import customuser

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = customuser(name="hitesh",
                          email="hitesh@lco.dev",
                          is_staff=True,
                          is_superuser=True,
                          gender="Male"
                          )
        user.set_password("12345")
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]

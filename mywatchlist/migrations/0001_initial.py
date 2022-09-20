
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched', models.TextField()),
                ('title', models.TextField()),
                ('rating', models.IntegerField()),
                ('release_date', models.TextField()),
                ('review', models.TextField()),
            ],
        ),
    ]

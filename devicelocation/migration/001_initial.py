from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceID', models.CharField(max_length=50)),
                ('lat', models.CharField(max_length=50)),
                ('long', models.CharField(max_length=50)),
                ('timestamp', models.CharField(max_length=50)),
                ('speed', models.CharField(max_length=50)),
                ('accuracy', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'DeviceLocation',
            },
        ),
    ]

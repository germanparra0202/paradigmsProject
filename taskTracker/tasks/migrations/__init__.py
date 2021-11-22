from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migtation):
    
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name = 'Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=200)),
                ('desc_text', models.CharField(max_length=200)),
                ('proj_text', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=True))
            ],
        ),
        migrations.CreateModel(
            name = 'TimeEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=tasks.task)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField())
            ],
        )
    ]
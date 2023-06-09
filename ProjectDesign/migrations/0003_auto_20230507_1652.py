# Generated by Django 3.2.6 on 2023-05-07 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectDesign', '0002_auto_20230507_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='The Young Baker', max_length=255, unique=True)),
                ('subtitle', models.CharField(default='Your ocassion, our cakes!', max_length=255)),
                ('image', models.ImageField(default='default.jpg', upload_to='Chef/')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('facebook', models.URLField(default='facebook', max_length=255)),
                ('instagram', models.URLField(default='instagram', max_length=255)),
                ('twitter', models.URLField(default='twitter', max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='home',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='about',
            name='sub_image1',
            field=models.ImageField(default='default.jpg', upload_to='About/'),
        ),
        migrations.AddField(
            model_name='about',
            name='sub_image2',
            field=models.ImageField(default='default.jpg', upload_to='About/'),
        ),
        migrations.AddField(
            model_name='about',
            name='sub_image3',
            field=models.ImageField(default='default.jpg', upload_to='About/'),
        ),
        migrations.AddField(
            model_name='home',
            name='facebook',
            field=models.URLField(default='facebook', max_length=255),
        ),
        migrations.AddField(
            model_name='home',
            name='image2',
            field=models.ImageField(default='default.jpg', upload_to='Home/'),
        ),
        migrations.AddField(
            model_name='home',
            name='image3',
            field=models.ImageField(default='default.jpg', upload_to='Home/'),
        ),
        migrations.AddField(
            model_name='home',
            name='instagram',
            field=models.URLField(default='instagram', max_length=255),
        ),
        migrations.AddField(
            model_name='home',
            name='linkedin',
            field=models.URLField(default='linkedin', max_length=255),
        ),
        migrations.AddField(
            model_name='home',
            name='twitter',
            field=models.URLField(default='twitter', max_length=255),
        ),
    ]

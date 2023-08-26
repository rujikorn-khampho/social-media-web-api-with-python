# Generated by Django 4.2.3 on 2023-08-26 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('SENT', 'Sent'), ('ACCEPTED', 'Accepted'), ('REJECTED', 'Rejected')], default='SENT', max_length=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('acceptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acceptor_friend_requests', to=settings.AUTH_USER_MODEL)),
                ('initiator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='initiator_friend_requests', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'friends_friend_request',
            },
        ),
    ]
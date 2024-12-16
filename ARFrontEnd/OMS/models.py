# from django.db import models
# from django.db.models import JSONField

# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=150)
#     full_name = models.CharField(max_length=255, blank=True, null=True)
#     pwd = models.CharField(max_length=255)
#     email = models.EmailField(max_length=255, unique=True)
#     mfa_enabled = models.BooleanField(default=False)
#     mfa_key = models.CharField(max_length=255, blank=True, null=True)
#     role = models.CharField(max_length=50, blank=True, null=True)
#     active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = 'users'
#         managed = False

#     def __str__(self):
#         return self.username
    
# class Strategy(models.Model):
#     id = models.AutoField(primary_key=True)
#     user_id = models.IntegerField(null=True, blank=True)
#     client_id = models.CharField(max_length=25, null=True, blank=True)
#     name = models.CharField(max_length=100, null=True, blank=True)
#     active = models.BooleanField(default=True)
#     portfolio = models.CharField(max_length=50, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = 'strategy'

#     def __str__(self):
#         return f'{self.name} - {self.client_id}'
    

# class Watchlist(models.Model):
#     id = models.AutoField(primary_key=True)
#     strategy_id = models.IntegerField()
#     strategy_name = models.CharField(max_length=255)
#     strategy_code = models.CharField(max_length=100)
#     underlying = models.CharField(max_length=255)
#     portfolio = models.CharField(max_length=255)
#     bidding_mode = models.CharField(max_length=50)
#     expiry = models.DateField()
#     legs_info = JSONField()
#     active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = 'watchlist'
#         managed = False

#     def __str__(self):
#         return self.strategy_name
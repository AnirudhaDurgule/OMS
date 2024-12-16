from django.contrib import admin
# from .models import Strategy, User, Watchlist

# @admin.site.unregister(Strategy)
# class StrategyAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user_id', 'client_id', 'name', 'active', 'portfolio', 'created_at', 'updated_at')
#     readonly_fields = ('created_at', 'updated_at')

# @admin.site.unregister(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'username', 'full_name', 'email', 'role', 'active', 'created_at', 'updated_at')
#     search_fields = ('username', 'full_name', 'email')
#     list_filter = ('active', 'role')
#     readonly_fields = ('created_at', 'updated_at')

#     fieldsets = (
#         (None, {'fields': ('username', 'full_name', 'email', 'role', 'active')}),
#         ('Security', {'fields': ('pwd', 'mfa_enabled', 'mfa_key')}),
#         ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    # )

# @admin.site.unregister(Watchlist)
# class WatchlistAdmin(admin.ModelAdmin):
#     list_display = ('id', 'strategy_id', 'strategy_name', 'strategy_code', 'underlying', 'portfolio', 'bidding_mode', 'expiry', 'active', 'created_at', 'updated_at')
#     search_fields = ('strategy_name', 'strategy_code', 'underlying', 'portfolio')
#     list_filter = ('bidding_mode', 'active', 'expiry')
#     readonly_fields = ('created_at', 'updated_at')

#     fieldsets = (
#         (None, {'fields': ('strategy_id', 'strategy_name', 'strategy_code', 'underlying', 'portfolio', 'bidding_mode', 'expiry', 'legs_info', 'active')}),
#         ('Timestamps', {'fields': ('created_at', 'updated_at')}),
#     )
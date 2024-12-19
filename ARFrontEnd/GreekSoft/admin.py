from django.contrib import admin
# Register your models here.
from django.contrib import admin
from .models import Users, Strategy, Watchlist, Cmmaster, Client, Fnomaster, Mqreceiver, StrategyHistory, Test, \
    WatchlistHistory, Tradebook, Orderbook, NetPosition
from .models import Liveorder ,Templiveorder

@admin.register(Strategy)
class StrategyAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'client_id', 'name', 'portfolio', 'active', 'created_at', 'updated_at')
    search_fields = ('client_id', 'name', 'portfolio')
    list_filter = ('active', 'portfolio')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Strategy Details', {
            'fields': ('user_id', 'client_id', 'name', 'portfolio', 'active'),
            'description': 'Details about the strategy, including its unique identifiers and status'
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'description': 'Automatically managed fields showing when the strategy was created and last updated'
        }),
    )

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'full_name', 'email', 'role', 'active', 'created_at', 'updated_at')
    search_fields = ('username', 'full_name', 'email')
    list_filter = ('active', 'role')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('User Information', {
            'fields': ('username', 'full_name', 'email', 'role', 'active')
        }),
        ('Security Details', {
            'fields': ('pwd', 'mfa_enabled', 'mfa_key'),
            'description': 'Sensitive information related to user security'
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'description': 'Automatically managed fields showing when the user was created and last updated'
        }),
    )

@admin.register(Watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'strategy_id', 'strategy_name', 'strategy_code', 'underlying', 'portfolio', 'bidding_mode', 'expiry', 'active', 'created_at', 'updated_at')
    search_fields = ('strategy_name', 'strategy_code', 'underlying', 'portfolio')
    list_filter = ('active', 'expiry', 'bidding_mode')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Watchlist Details', {
            'fields': ('strategy_id', 'strategy_name', 'strategy_code', 'underlying', 'portfolio', 'bidding_mode', 'expiry', 'legs_info', 'active'),
            'description': 'Information about the watchlist entry, including strategy details and additional information'
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'description': 'Automatically managed fields showing when the watchlist entry was created and last updated'
        }),
    )

@admin.register(Orderbook)
class OrderbookAdmin(admin.ModelAdmin):
    # list_display = ('app_order_id', 'client_id', 'trading_symbol', 'order_status', 'order_quantity', 'order_price', 'exchange_segment', 'exchange_transact_time', 'last_update_date_time', 'order_expiry_date')
    list_display = [field.name for field in Orderbook._meta.fields]
    search_fields = ('app_order_id', 'client_id', 'trading_symbol', 'order_status', 'exchange_order_id')
    list_filter = ('order_status', 'exchange_segment', 'order_side', 'product_type')
    readonly_fields = ('app_order_id', 'exchange_transact_time', 'last_update_date_time', 'order_generated_date_time', 'order_expiry_date')

    fieldsets = (
        ('Order Information', {
            'fields': ('app_order_id', 'order_reference_id', 'generated_by', 'exchange_order_id', 'order_category_type', 'exchange_segment', 'exchange_instrument_id', 'trading_symbol')
        }),
        ('Execution Details', {
            'fields': ('order_side', 'order_type', 'product_type', 'time_in_force', 'order_price', 'order_quantity', 'order_stop_price', 'order_status', 'order_average_traded_price', 'leaves_quantity', 'cumulative_quantity', 'order_disclosed_quantity')
        }),
        ('Timestamps', {
            'fields': ('order_generated_date_time', 'exchange_transact_time', 'last_update_date_time', 'order_expiry_date')
        }),
        ('Unique Identifiers', {
            'fields': ('order_unique_identifier', 'bo_leg_details', 'bo_entry_order_id', 'sequence_number')
        }),
        ('Additional Information', {
            'fields': ('api_order_source', 'is_spread', 'is_amo', 'cancel_reject_reason', 'message_code', 'message_version', 'token_id', 'application_type', 'login_id', 'client_id')
        }),
    )

@admin.register(Tradebook)
class TradebookAdmin(admin.ModelAdmin):
    # list_display = ('app_order_id', 'client_id', 'trading_symbol', 'order_status', 'order_quantity', 'order_price', 'exchange_segment', 'exchange_transact_time', 'last_update_date_time','exchange_instrument_id',)
    list_display = [field.name for field in Tradebook._meta.fields]
    # search_fields = [field.name for field in Tradebook._meta.fields]  # Add search functionality for all fields
    # list_filter = [field.name for field in Tradebook._meta.fields]  # Add filtering options for all fields
    search_fields = ('app_order_id', 'client_id', 'trading_symbol', 'order_status', 'exchange_order_id')
    list_filter = ('order_status', 'exchange_segment', 'order_side', 'product_type')
    readonly_fields = ('app_order_id', 'exchange_transact_time', 'last_update_date_time', 'order_generated_date_time')

    fieldsets = (
        ('Order Details', {
            'fields': ('app_order_id', 'order_reference_id', 'generated_by', 'exchange_order_id', 'order_category_type', 'exchange_segment', 'exchange_instrument_id', 'trading_symbol')
        }),
        ('Execution Details', {
            'fields': ('order_side', 'order_type', 'product_type', 'time_in_force', 'order_price', 'order_quantity', 'order_stop_price', 'order_status', 'order_average_traded_price', 'leaves_quantity', 'cumulative_quantity', 'order_disclosed_quantity')
        }),
        ('Timestamps', {
            'fields': ('order_generated_date_time', 'exchange_transact_time', 'last_update_date_time')
        }),
        ('Unique Identifiers', {
            'fields': ('order_unique_identifier', 'execution_id', 'execution_report_index', 'sequence_number')
        }),
        ('Additional Information', {
            'fields': ('api_order_source', 'is_spread', 'message_code', 'message_version', 'token_id', 'application_type', 'login_id', 'client_id', 'last_traded_price', 'last_traded_quantity', 'last_execution_transact_time', 'order_leg_status')
        }),
    )

@admin.register(NetPosition)
class NetPositionAdmin(admin.ModelAdmin):
    # list_display = (
    #     'account_id', 'trading_symbol', 'exchange_segment', 'exchange_instrument_id',
    #     'product_type', 'market_lot', 'multiplier', 'buy_average_price', 'sell_average_price',
    #     'open_buy_quantity', 'open_sell_quantity', 'quantity', 'buy_amount', 'sell_amount',
    #     'net_amount', 'unrealized_mtm', 'realized_mtm', 'mtm', 'bep', 'sum_of_traded_quantity_and_price_buy',
    #     'sum_of_traded_quantity_and_price_sell', 'statistics_level', 'is_inter_op_position', 'child_positions',
    #     'message_code', 'message_version', 'token_id', 'application_type', 'sequence_number'
    # )
    list_display = [field.name for field in NetPosition._meta.fields]
    search_fields = (
        'account_id', 'trading_symbol', 'exchange_segment', 'exchange_instrument_id',
        'product_type', 'buy_average_price', 'sell_average_price', 'quantity', 'buy_amount',
        'sell_amount', 'net_amount', 'unrealized_mtm', 'realized_mtm', 'mtm', 'bep', 'statistics_level'
    )
    list_filter = (
        'exchange_segment', 'product_type', 'is_inter_op_position', 'message_code'
    )
    readonly_fields = (
        'unrealized_mtm', 'realized_mtm', 'mtm', 'bep', 'sum_of_traded_quantity_and_price_buy',
        'sum_of_traded_quantity_and_price_sell', 'message_code', 'message_version', 'token_id',
        'application_type', 'sequence_number'
    )

    fieldsets = (
        ('Position Information', {
            'fields': (
                'account_id', 'trading_symbol', 'exchange_segment', 'exchange_instrument_id',
                'product_type', 'market_lot', 'multiplier'
            )
        }),
        ('Trade Details', {
            'fields': (
                'buy_average_price', 'sell_average_price', 'open_buy_quantity', 'open_sell_quantity',
                'quantity', 'buy_amount', 'sell_amount', 'net_amount'
            )
        }),
        ('MTM and BEP', {
            'fields': (
                'unrealized_mtm', 'realized_mtm', 'mtm', 'bep'
            )
        }),
        ('Summary', {
            'fields': (
                'sum_of_traded_quantity_and_price_buy', 'sum_of_traded_quantity_and_price_sell'
            )
        }),
        ('Additional Information', {
            'fields': (
                'statistics_level', 'is_inter_op_position', 'child_positions', 'message_code',
                'message_version', 'token_id', 'application_type', 'sequence_number'
            )
        }),
    )

@admin.register(Liveorder)
class LiveorderAdmin(admin.ModelAdmin):
    # list_display = (
    #     'id', 'portfolioname', 'watchlistid', 'username', 'clientname', 'strategy', 'symbol',
    #     'expiry', 'strike', 'optiontype', 'executiontype', 'askbidprice', 'calclimitprice',
    #     'scripcode', 'orderqty', 'filledqty', 'pendingqty', 'orderbs', 'producttype',
    #     'targetspdprice', 'qtypercycle', 'biddingmode', 'ordergeneratedtime', 'apporderid',
    #     'active', 'orderstatus', 'uniqueid', 'spreadid', 'argid', 'cycleid', 'modifystatus',
    #     'cancelstatus', 'ratio', 'created_at', 'updated_at', 'jumpqty', 'step', 'spread_bs'
    # )
    list_display = [field.name for field in Liveorder._meta.fields]
    search_fields = (
        'portfolioname', 'username', 'clientname', 'strategy', 'symbol', 'expiry', 'strike',
        'optiontype', 'executiontype', 'orderbs', 'producttype', 'biddingmode', 'ordergeneratedtime',
        'apporderid', 'active', 'orderstatus', 'uniqueid', 'spreadid', 'argid', 'cycleid'
    )
    list_filter = (
        'optiontype', 'executiontype', 'orderbs', 'producttype', 'biddingmode', 'active', 'orderstatus'
    )
    readonly_fields = (
        'created_at', 'updated_at'
    )

    fieldsets = (
        (None, {
            'fields': (
                'portfolioname', 'watchlistid', 'username', 'clientname', 'strategy', 'symbol',
                'expiry', 'strike', 'optiontype', 'executiontype', 'askbidprice', 'calclimitprice',
                'scripcode', 'orderqty', 'filledqty', 'pendingqty', 'orderbs', 'producttype',
                'targetspdprice', 'qtypercycle', 'biddingmode', 'ordergeneratedtime', 'apporderid',
                'active', 'orderstatus', 'uniqueid', 'spreadid', 'argid', 'cycleid', 'jumpqty',
                'step', 'spread_bs'
            )
        }),
        ('Status', {
            'fields': (
                'modifystatus', 'cancelstatus', 'ratio'
            )
        }),
        ('Timestamps', {
            'fields': (
                'created_at', 'updated_at'
            )
        }),
    )

@admin.register(Templiveorder)
class TempliveorderAdmin(admin.ModelAdmin):
    # list_display = (
    #     'id', 'portfolioname', 'watchlistid', 'username', 'clientname', 'strategy', 'symbol',
    #     'expiry', 'strike', 'optiontype', 'executiontype', 'askbidprice', 'calclimitprice',
    #     'scripcode', 'orderqty', 'filledqty', 'pendingqty', 'orderbs', 'producttype',
    #     'targetspdprice', 'qtypercycle', 'biddingmode', 'ordergeneratedtime', 'apporderid',
    #     'active', 'orderstatus', 'uniqueid', 'spreadid', 'argid', 'cycleid', 'modifystatus',
    #     'cancelstatus', 'ratio', 'created_at', 'updated_at', 'jumpqty', 'step', 'spread_bs'
    # )
    list_display = [field.name for field in Templiveorder._meta.fields]
    search_fields = (
        'portfolioname', 'username', 'clientname', 'strategy', 'symbol', 'expiry', 'strike',
        'optiontype', 'executiontype', 'orderbs', 'producttype', 'biddingmode', 'ordergeneratedtime',
        'apporderid', 'active', 'orderstatus', 'uniqueid', 'spreadid', 'argid', 'cycleid'
    )
    list_filter = (
        'optiontype', 'executiontype', 'orderbs', 'producttype', 'biddingmode', 'active', 'orderstatus'
    )
    readonly_fields = (
        'created_at', 'updated_at'
    )

    fieldsets = (
        (None, {
            'fields': (
                'portfolioname', 'watchlistid', 'username', 'clientname', 'strategy', 'symbol',
                'expiry', 'strike', 'optiontype', 'executiontype', 'askbidprice', 'calclimitprice',
                'scripcode', 'orderqty', 'filledqty', 'pendingqty', 'orderbs', 'producttype',
                'targetspdprice', 'qtypercycle', 'biddingmode', 'ordergeneratedtime', 'apporderid',
                'active', 'orderstatus', 'uniqueid', 'spreadid', 'argid', 'cycleid', 'jumpqty',
                'step', 'spread_bs'
            )
        }),
        ('Status', {
            'fields': (
                'modifystatus', 'cancelstatus', 'ratio'
            )
        }),
        ('Timestamps', {
            'fields': (
                'created_at', 'updated_at'
            )
        }),
    )

@admin.register(Fnomaster)
class FnomasterAdmin(admin.ModelAdmin):
    # list_display = (
    #     'scripcode', 'exchange', 'lotsize', 'symbol', 'expiry', 'instname', 'opt_type', 'strike', 'created_at'
    # )
    list_display = [field.name for field in Fnomaster._meta.fields]
    search_fields = (
        'scripcode', 'symbol', 'expiry', 'instname', 'opt_type', 'strike'
    )
    list_filter = (
        'exchange', 'opt_type'
    )
    readonly_fields = (
        'created_at',
    )

    fieldsets = (
        (None, {
            'fields': (
                'scripcode', 'exchange', 'lotsize', 'symbol', 'expiry', 'instname', 'opt_type', 'strike'
            )
        }),
        ('Timestamps', {
            'fields': (
                'created_at',
            )
        }),
    )

@admin.register(Mqreceiver)
class MqreceiverAdmin(admin.ModelAdmin):
    # list_display = (
    #     'messagetype', 'jdata', 'created_at', 'updated_at'
    # )
    list_display = [field.name for field in Mqreceiver._meta.fields]
    search_fields = (
        'messagetype',
    )
    readonly_fields = (
        'created_at', 'updated_at',
    )

    fieldsets = (
        (None, {
            'fields': (
                'messagetype', 'jdata'
            )
        }),
        ('Timestamps', {
            'fields': (
                'created_at', 'updated_at',
            )
        }),
    )

@admin.register(Cmmaster)
class CmmasterAdmin(admin.ModelAdmin):
    list_display = ('scripcode', 'indexname', 'created_at')
    search_fields = ('scripcode', 'indexname')
    readonly_fields = ('created_at',)

    fieldsets = (
        (None, {
            'fields': ('scripcode', 'indexname')
        }),
        ('Timestamps', {
            'fields': ('created_at',)
        }),
    )

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'vendor', 'client_id', 'customer_id', 'active', 'app_id', 'created_at', 'updated_at'
    )
    search_fields = (
        'vendor', 'client_id', 'customer_id', 'app_id'
    )
    list_filter = (
        'active', 'status'
    )
    readonly_fields = (
        'created_at', 'updated_at'
    )

    fieldsets = (
        (None, {
            'fields': (
                'vendor', 'client_id', 'client_pass', 'client_pass_1', 'client_pass_2',
                'customer_id', 'active', 'app_id', 'app_secret', 'redirect_url',
                'request_token', 'access_token', 'reserve', 'status', 'info'
            )
        }),
        ('Timestamps', {
            'fields': (
                'created_at', 'updated_at',
            )
        }),
    )

@admin.register(StrategyHistory)
class StrategyHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'strategy_id', 'user_id', 'client_id', 'name', 'active', 'created_at', 'updated_at'
    )
    search_fields = (
        'strategy_id', 'user_id', 'client_id', 'name'
    )
    list_filter = (
        'active', 'created_at', 'updated_at'
    )
    readonly_fields = (
        'created_at', 'updated_at'
    )

    fieldsets = (
        (None, {
            'fields': (
                'strategy_id', 'user_id', 'client_id', 'name', 'active'
            )
        }),
        ('Timestamps', {
            'fields': (
                'created_at', 'updated_at'
            )
        }),
    )

@admin.register(WatchlistHistory)
class WatchlistHistoryAdmin(admin.ModelAdmin):
    list_display = ('watchlist_id', 'strategy_id', 'strategy_name', 'underlying', 'expiry', 'active')
    search_fields = ('strategy_name', 'strategy_code', 'underlying')
    list_filter = ('active', 'expiry')
    ordering = ('-created_at',)

    fieldsets = (
        ('Strategy Details', {
            'fields': ('strategy_id', 'strategy_name', 'strategy_code', 'underlying', 'expiry')
        }),
        ('Leg Information', {
            'fields': ('legs_info',)
        }),
        ('Status', {
            'fields': ('active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('info', 'created_at', 'updated_at')
    ordering = ('-created_at',)

    fieldsets = (
        ('Information', {
            'fields': ('info',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

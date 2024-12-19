# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Client(models.Model):
    vendor = models.CharField(max_length=50)
    client_id = models.CharField(max_length=50)
    client_pass = models.CharField(max_length=100)
    client_pass_1 = models.CharField(max_length=100, blank=True, null=True)
    client_pass_2 = models.CharField(max_length=100, blank=True, null=True)
    customer_id = models.CharField(max_length=50, blank=True, null=True)
    active = models.BooleanField()
    app_id = models.CharField(max_length=100)
    app_secret = models.CharField(max_length=100)
    redirect_url = models.CharField(max_length=50, blank=True, null=True)
    request_token = models.CharField(max_length=1000, blank=True, null=True)
    access_token = models.CharField(max_length=1000, blank=True, null=True)
    reserve = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    info = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client'


class Cmmaster(models.Model):
    scripcode = models.AutoField(primary_key=True)
    indexname = models.CharField(max_length=150)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cmmaster'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


    # SELECT
    # scripcode, exchange, lotsize, symbol, expiry, instname, opt_type, strike, created_at
    # FROM
    # public.fnomaster;

# class Fnomaster(models.Model):
#     scripcode = models.BigIntegerField(blank=True, null=True)
#     exchange = models.BigIntegerField(blank=True, null=True)
#     lotsize = models.BigIntegerField(blank=True, null=True)
#     symbol = models.TextField(blank=True, null=True)
#     expiry = models.TextField(blank=True, null=True)
#     instname = models.TextField(blank=True, null=True)
#     opt_type = models.TextField(blank=True, null=True)
#     strike = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'fnomaster'
#
#     class Meta:
#         managed = False
#         db_table = 'fnomaster'
#         unique_together = (('scripcode','strike'),)  # If these fields together can be considered as unique
#         # unique_together = (('scripcode', 'exchange', 'expiry', 'instname','strike'),)  # If these fields together can be considered as unique


class Fnomaster(models.Model):
    scripcode = models.BigIntegerField(primary_key=True)
    exchange = models.BigIntegerField(blank=True, null=True)
    lotsize = models.BigIntegerField(blank=True, null=True)
    symbol = models.TextField(blank=True, null=True)
    expiry = models.TextField(blank=True, null=True)
    instname = models.TextField(blank=True, null=True)
    opt_type = models.TextField(blank=True, null=True)
    strike = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fnomaster'


class Liveorder(models.Model):
    id = models.AutoField(primary_key=True)
    portfolioname = models.CharField(max_length=50)
    # watchlistid = models.IntegerField(primary_key=True)  # The composite primary key (watchlistid, id, cycleid) found, that is not supported. The first column is selected.
    watchlistid = models.IntegerField()  # The composite primary key (watchlistid, id, cycleid) found, that is not supported. The first column is selected.
    username = models.CharField(max_length=30, blank=True, null=True)
    clientname = models.CharField(max_length=20, blank=True, null=True)
    strategy = models.CharField(max_length=50, blank=True, null=True)
    symbol = models.CharField(max_length=30, blank=True, null=True)
    expiry = models.CharField(max_length=20, blank=True, null=True)
    strike = models.CharField(max_length=20, blank=True, null=True)
    optiontype = models.CharField(max_length=10)
    executiontype = models.CharField(max_length=20, blank=True, null=True)
    askbidprice = models.FloatField(blank=True, null=True)
    calclimitprice = models.FloatField(blank=True, null=True)
    scripcode = models.IntegerField(blank=True, null=True)
    orderqty = models.IntegerField(blank=True, null=True)
    filledqty = models.IntegerField(blank=True, null=True)
    pendingqty = models.IntegerField(blank=True, null=True)
    orderbs = models.CharField(max_length=20, blank=True, null=True)
    producttype = models.CharField(max_length=20, blank=True, null=True)
    targetspdprice = models.FloatField(blank=True, null=True)
    qtypercycle = models.IntegerField(blank=True, null=True)
    biddingmode = models.CharField(max_length=20, blank=True, null=True)
    ordergeneratedtime = models.CharField(max_length=50, blank=True, null=True)
    apporderid = models.BigIntegerField(blank=True, null=True)
    active = models.CharField(max_length=20, blank=True, null=True)
    orderstatus = models.CharField(max_length=20, blank=True, null=True)
    uniqueid = models.CharField(max_length=50, blank=True, null=True)
    spreadid = models.BigIntegerField(blank=True, null=True)
    argid = models.BigIntegerField(blank=True, null=True)
    cycleid = models.BigIntegerField()
    modifystatus = models.JSONField(blank=True, null=True)
    cancelstatus = models.JSONField(blank=True, null=True)
    ratio = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    jumpqty = models.IntegerField(blank=True, null=True)
    step = models.IntegerField(blank=True, null=True)
    spread_bs = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'liveorder'
        unique_together = (('watchlistid', 'id', 'cycleid'),)



class Mqreceiver(models.Model):
    messagetype = models.CharField(max_length=100)
    jdata = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mqreceiver'


class Strategy(models.Model):
    user_id = models.IntegerField()
    client_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    active = models.BooleanField()
    portfolio = models.CharField(max_length=50)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'strategy'
        unique_together = (('user_id', 'client_id', 'name', 'portfolio'),)


class StrategyHistory(models.Model):
    strategy_id = models.IntegerField()
    user_id = models.IntegerField()
    client_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    active = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'strategy_history'


class Templiveorder(models.Model):
    id = models.AutoField(primary_key=True)
    portfolioname = models.CharField(max_length=50)
    watchlistid = models.IntegerField()  # The composite primary key (watchlistid, id) found, that is not supported. The first column is selected.
    username = models.CharField(max_length=30, blank=True, null=True)
    clientname = models.CharField(max_length=20, blank=True, null=True)
    strategy = models.CharField(max_length=50, blank=True, null=True)
    symbol = models.CharField(max_length=30, blank=True, null=True)
    expiry = models.CharField(max_length=20, blank=True, null=True)
    strike = models.CharField(max_length=20, blank=True, null=True)
    optiontype = models.CharField(max_length=10)
    executiontype = models.CharField(max_length=20, blank=True, null=True)
    askbidprice = models.FloatField(blank=True, null=True)
    calclimitprice = models.FloatField(blank=True, null=True)
    scripcode = models.IntegerField(blank=True, null=True)
    orderqty = models.IntegerField(blank=True, null=True)
    filledqty = models.IntegerField(blank=True, null=True)
    pendingqty = models.IntegerField(blank=True, null=True)
    orderbs = models.CharField(max_length=20, blank=True, null=True)
    producttype = models.CharField(max_length=20, blank=True, null=True)
    targetspdprice = models.FloatField(blank=True, null=True)
    qtypercycle = models.IntegerField(blank=True, null=True)
    biddingmode = models.CharField(max_length=20, blank=True, null=True)
    ordergeneratedtime = models.CharField(max_length=50, blank=True, null=True)
    apporderid = models.BigIntegerField(blank=True, null=True)
    active = models.CharField(max_length=20, blank=True, null=True)
    orderstatus = models.CharField(max_length=20, blank=True, null=True)
    uniqueid = models.CharField(max_length=50, blank=True, null=True)
    spreadid = models.BigIntegerField(blank=True, null=True)
    argid = models.BigIntegerField(blank=True, null=True)
    cycleid = models.BigIntegerField(blank=True, null=True)
    modifystatus = models.JSONField(blank=True, null=True)
    cancelstatus = models.JSONField(blank=True, null=True)
    ratio = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    jumpqty = models.IntegerField(blank=True, null=True)
    step = models.IntegerField(blank=True, null=True)
    spread_bs = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'templiveorder'
        unique_together = (('watchlistid', 'id'),)


class Test(models.Model):
    info = models.JSONField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'


class Token(models.Model):
    token_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    token = models.CharField(max_length=50)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'token'


class Users(models.Model):
    username = models.CharField(unique=True, max_length=50)
    full_name = models.CharField(max_length=100)
    pwd = models.CharField(max_length=300)
    email = models.CharField(max_length=50)
    mfa_enabled = models.BooleanField()
    mfa_key = models.CharField(max_length=50)
    role = models.CharField(max_length=15)
    active = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Vendortoken(models.Model):
    appkey = models.TextField(blank=True, null=True)
    appsecret = models.TextField(blank=True, null=True)
    dealer_or_clientid = models.TextField(blank=True, null=True)
    keyno = models.BigIntegerField(blank=True, null=True)
    keytype = models.TextField(blank=True, null=True)
    vendor = models.TextField(blank=True, null=True)
    isdealer = models.TextField(blank=True, null=True)
    clientcode = models.TextField(blank=True, null=True)
    token = models.TextField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendortoken'


class Watchlist(models.Model):
    id = models.AutoField(primary_key=True)
    strategy_id = models.IntegerField()
    strategy_name = models.CharField(max_length=100)
    strategy_code = models.CharField(max_length=50)
    underlying = models.CharField(max_length=50)
    portfolio = models.CharField(max_length=50)
    bidding_mode = models.CharField(max_length=50)
    expiry = models.DateField()
    legs_info = models.JSONField()
    active = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'watchlist'
        # unique_together = (('strategy_id', 'strategy_name'),)
        constraints = [
            models.UniqueConstraint(fields=['strategy_id', 'strategy_name'], name='uq_watchlist_xref')
        ]


class WatchlistHistory(models.Model):
    watchlist_id = models.IntegerField()
    strategy_id = models.IntegerField()
    strategy_name = models.CharField(max_length=100)
    strategy_code = models.CharField(max_length=50)
    underlying = models.CharField(max_length=50)
    expiry = models.DateField()
    legs_info = models.JSONField()
    active = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'watchlist_history'




# class Tradebook(models.Model):
#     login_id = models.TextField(db_column='LoginID', blank=True, null=True)
#     client_id = models.TextField(db_column='ClientID', blank=True, null=True)
#     app_order_id = models.TextField(db_column='AppOrderID', blank=True, primary_key=True)
#     order_reference_id = models.TextField(db_column='OrderReferenceID', blank=True, null=True)
#     generated_by = models.TextField(db_column='GeneratedBy', blank=True, null=True)
#     exchange_order_id = models.TextField(db_column='ExchangeOrderID', blank=True, null=True)
#     order_category_type = models.TextField(db_column='OrderCategoryType', blank=True, null=True)
#     exchange_segment = models.TextField(db_column='ExchangeSegment', blank=True, null=True)
#     exchange_instrument_id = models.TextField(db_column='ExchangeInstrumentID', blank=True, null=True)
#     order_side = models.TextField(db_column='OrderSide', blank=True, null=True)
#     order_type = models.TextField(db_column='OrderType', blank=True, null=True)
#     product_type = models.TextField(db_column='ProductType', blank=True, null=True)
#     time_in_force = models.TextField(db_column='TimeInForce', blank=True, null=True)
#     order_price = models.TextField(db_column='OrderPrice', blank=True, null=True)
#     order_quantity = models.TextField(db_column='OrderQuantity', blank=True, null=True)
#     order_stop_price = models.TextField(db_column='OrderStopPrice', blank=True, null=True)
#     order_status = models.TextField(db_column='OrderStatus', blank=True, null=True)
#     order_average_traded_price = models.TextField(db_column='OrderAverageTradedPrice', blank=True, null=True)
#     leaves_quantity = models.TextField(db_column='LeavesQuantity', blank=True, null=True)
#     cumulative_quantity = models.TextField(db_column='CumulativeQuantity', blank=True, null=True)
#     order_disclosed_quantity = models.TextField(db_column='OrderDisclosedQuantity', blank=True, null=True)
#     order_generated_date_time = models.TextField(db_column='OrderGeneratedDateTime', blank=True, null=True)
#     exchange_transact_time = models.TextField(db_column='ExchangeTransactTime', blank=True, null=True)
#     last_update_date_time = models.TextField(db_column='LastUpdateDateTime', blank=True, null=True)
#     order_unique_identifier = models.TextField(db_column='OrderUniqueIdentifier', blank=True, null=True)
#     order_leg_status = models.TextField(db_column='OrderLegStatus', blank=True, null=True)
#     last_traded_price = models.TextField(db_column='LastTradedPrice', blank=True, null=True)
#     last_traded_quantity = models.TextField(db_column='LastTradedQuantity', blank=True, null=True)
#     last_execution_transact_time = models.TextField(db_column='LastExecutionTransactTime', blank=True, null=True)
#     execution_id = models.TextField(db_column='ExecutionID', blank=True, null=True)
#     trading_symbol = models.TextField(db_column='TradingSymbol', blank=True, null=True)
#     execution_report_index = models.TextField(db_column='ExecutionReportIndex', blank=True, null=True)
#     api_order_source = models.TextField(db_column='ApiOrderSource', blank=True, null=True)
#     is_spread = models.TextField(db_column='IsSpread', blank=True, null=True)
#     message_code = models.TextField(db_column='MessageCode', blank=True, null=True)
#     message_version = models.TextField(db_column='MessageVersion', blank=True, null=True)
#     token_id = models.TextField(db_column='TokenID', blank=True, null=True)
#     application_type = models.TextField(db_column='ApplicationType', blank=True, null=True)
#     sequence_number = models.TextField(db_column='SequenceNumber', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tradebook'
#         unique_together = (('app_order_id', 'exchange_transact_time'),)  # Ensure uniqueness on these fields

from django.db import models

class Tradebook(models.Model):
    login_id = models.TextField(db_column='LoginID', blank=True, null=True)
    client_id = models.TextField(db_column='ClientID', blank=True, null=True)
    app_order_id = models.TextField(db_column='AppOrderID', primary_key=True)
    order_reference_id = models.TextField(db_column='OrderReferenceID', blank=True, null=True)
    generated_by = models.TextField(db_column='GeneratedBy', blank=True, null=True)
    exchange_order_id = models.TextField(db_column='ExchangeOrderID', blank=True, null=True)
    order_category_type = models.TextField(db_column='OrderCategoryType', blank=True, null=True)
    exchange_segment = models.TextField(db_column='ExchangeSegment', blank=True, null=True)
    exchange_instrument_id = models.TextField(db_column='ExchangeInstrumentID', blank=True, null=True)
    order_side = models.TextField(db_column='OrderSide', blank=True, null=True)
    order_type = models.TextField(db_column='OrderType', blank=True, null=True)
    product_type = models.TextField(db_column='ProductType', blank=True, null=True)
    time_in_force = models.TextField(db_column='TimeInForce', blank=True, null=True)
    order_price = models.TextField(db_column='OrderPrice', blank=True, null=True)
    order_quantity = models.TextField(db_column='OrderQuantity', blank=True, null=True)
    order_stop_price = models.TextField(db_column='OrderStopPrice', blank=True, null=True)
    order_status = models.TextField(db_column='OrderStatus', blank=True, null=True)
    order_average_traded_price = models.TextField(db_column='OrderAverageTradedPrice', blank=True, null=True)
    leaves_quantity = models.TextField(db_column='LeavesQuantity', blank=True, null=True)
    cumulative_quantity = models.TextField(db_column='CumulativeQuantity', blank=True, null=True)
    order_disclosed_quantity = models.TextField(db_column='OrderDisclosedQuantity', blank=True, null=True)
    order_generated_date_time = models.TextField(db_column='OrderGeneratedDateTime', blank=True, null=True)
    exchange_transact_time = models.TextField(db_column='ExchangeTransactTime', blank=True, null=True)
    last_update_date_time = models.TextField(db_column='LastUpdateDateTime', blank=True, null=True)
    order_unique_identifier = models.TextField(db_column='OrderUniqueIdentifier', blank=True, null=True)
    order_leg_status = models.TextField(db_column='OrderLegStatus', blank=True, null=True)
    last_traded_price = models.TextField(db_column='LastTradedPrice', blank=True, null=True)
    last_traded_quantity = models.TextField(db_column='LastTradedQuantity', blank=True, null=True)
    last_execution_transact_time = models.TextField(db_column='LastExecutionTransactTime', blank=True, null=True)
    execution_id = models.TextField(db_column='ExecutionID', blank=True, null=True)
    trading_symbol = models.TextField(db_column='TradingSymbol', blank=True, null=True)
    execution_report_index = models.TextField(db_column='ExecutionReportIndex', blank=True, null=True)
    api_order_source = models.TextField(db_column='ApiOrderSource', blank=True, null=True)
    is_spread = models.TextField(db_column='IsSpread', blank=True, null=True)
    message_code = models.TextField(db_column='MessageCode', blank=True, null=True)
    message_version = models.TextField(db_column='MessageVersion', blank=True, null=True)
    token_id = models.TextField(db_column='TokenID', blank=True, null=True)
    application_type = models.TextField(db_column='ApplicationType', blank=True, null=True)
    sequence_number = models.TextField(db_column='SequenceNumber', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tradebook'
        unique_together = (('app_order_id', 'exchange_transact_time'),)  # Ensure uniqueness on these fields


# from django.db import models

class Orderbook(models.Model):
    login_id = models.TextField(db_column='LoginID', blank=True, null=True)
    client_id = models.TextField(db_column='ClientID', blank=True, null=True)
    app_order_id = models.TextField(db_column='AppOrderID', primary_key=True)
    order_reference_id = models.TextField(db_column='OrderReferenceID', blank=True, null=True)
    generated_by = models.TextField(db_column='GeneratedBy', blank=True, null=True)
    exchange_order_id = models.TextField(db_column='ExchangeOrderID', blank=True, null=True)
    order_category_type = models.TextField(db_column='OrderCategoryType', blank=True, null=True)
    exchange_segment = models.TextField(db_column='ExchangeSegment', blank=True, null=True)
    exchange_instrument_id = models.TextField(db_column='ExchangeInstrumentID', blank=True, null=True)
    order_side = models.TextField(db_column='OrderSide', blank=True, null=True)
    order_type = models.TextField(db_column='OrderType', blank=True, null=True)
    product_type = models.TextField(db_column='ProductType', blank=True, null=True)
    time_in_force = models.TextField(db_column='TimeInForce', blank=True, null=True)
    order_price = models.TextField(db_column='OrderPrice', blank=True, null=True)
    order_quantity = models.TextField(db_column='OrderQuantity', blank=True, null=True)
    order_stop_price = models.TextField(db_column='OrderStopPrice', blank=True, null=True)
    order_status = models.TextField(db_column='OrderStatus', blank=True, null=True)
    order_average_traded_price = models.TextField(db_column='OrderAverageTradedPrice', blank=True, null=True)
    leaves_quantity = models.TextField(db_column='LeavesQuantity', blank=True, null=True)
    cumulative_quantity = models.TextField(db_column='CumulativeQuantity', blank=True, null=True)
    order_disclosed_quantity = models.TextField(db_column='OrderDisclosedQuantity', blank=True, null=True)
    order_generated_date_time = models.TextField(db_column='OrderGeneratedDateTime', blank=True, null=True)
    exchange_transact_time = models.TextField(db_column='ExchangeTransactTime', blank=True, null=True)
    trading_symbol = models.TextField(db_column='TradingSymbol', blank=True, null=True)
    last_update_date_time = models.TextField(db_column='LastUpdateDateTime', blank=True, null=True)
    order_expiry_date = models.TextField(db_column='OrderExpiryDate', blank=True, null=True)
    cancel_reject_reason = models.TextField(db_column='CancelRejectReason', blank=True, null=True)
    order_unique_identifier = models.TextField(db_column='OrderUniqueIdentifier', blank=True, null=True)
    order_leg_status = models.TextField(db_column='OrderLegStatus', blank=True, null=True)
    bo_leg_details = models.TextField(db_column='BoLegDetails', blank=True, null=True)
    is_spread = models.TextField(db_column='IsSpread', blank=True, null=True)
    bo_entry_order_id = models.TextField(db_column='BoEntryOrderId', blank=True, null=True)
    api_order_source = models.TextField(db_column='ApiOrderSource', blank=True, null=True)
    message_code = models.TextField(db_column='MessageCode', blank=True, null=True)
    message_version = models.TextField(db_column='MessageVersion', blank=True, null=True)
    token_id = models.TextField(db_column='TokenID', blank=True, null=True)
    application_type = models.TextField(db_column='ApplicationType', blank=True, null=True)
    sequence_number = models.TextField(db_column='SequenceNumber', blank=True, null=True)
    is_amo = models.TextField(db_column='IsAMO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orderbook'
        unique_together = (('app_order_id',),)

# from django.db import models

class NetPosition(models.Model):
    account_id = models.TextField(db_column='AccountID', blank=True, null=True)
    trading_symbol = models.TextField(db_column='TradingSymbol', primary_key=True)
    exchange_segment = models.TextField(db_column='ExchangeSegment', blank=True, null=True)
    exchange_instrument_id = models.TextField(db_column='ExchangeInstrumentId', blank=True, null=True)
    product_type = models.TextField(db_column='ProductType', blank=True, null=True)
    market_lot = models.TextField(db_column='Marketlot', blank=True, null=True)
    multiplier = models.TextField(db_column='Multiplier', blank=True, null=True)
    buy_average_price = models.TextField(db_column='BuyAveragePrice', blank=True, null=True)
    sell_average_price = models.TextField(db_column='SellAveragePrice', blank=True, null=True)
    open_buy_quantity = models.TextField(db_column='OpenBuyQuantity', blank=True, null=True)
    open_sell_quantity = models.TextField(db_column='OpenSellQuantity', blank=True, null=True)
    quantity = models.TextField(db_column='Quantity', blank=True, null=True)
    buy_amount = models.TextField(db_column='BuyAmount', blank=True, null=True)
    sell_amount = models.TextField(db_column='SellAmount', blank=True, null=True)
    net_amount = models.TextField(db_column='NetAmount', blank=True, null=True)
    unrealized_mtm = models.TextField(db_column='UnrealizedMTM', blank=True, null=True)
    realized_mtm = models.TextField(db_column='RealizedMTM', blank=True, null=True)
    mtm = models.TextField(db_column='MTM', blank=True, null=True)
    bep = models.TextField(db_column='BEP', blank=True, null=True)
    sum_of_traded_quantity_and_price_buy = models.TextField(db_column='SumOfTradedQuantityAndPriceBuy', blank=True, null=True)
    sum_of_traded_quantity_and_price_sell = models.TextField(db_column='SumOfTradedQuantityAndPriceSell', blank=True, null=True)
    statistics_level = models.TextField(db_column='statisticsLevel', blank=True, null=True)
    is_inter_op_position = models.TextField(db_column='isInterOpPosition', blank=True, null=True)
    child_positions = models.TextField(db_column='childPositions', blank=True, null=True)
    message_code = models.TextField(db_column='MessageCode', blank=True, null=True)
    message_version = models.TextField(db_column='MessageVersion', blank=True, null=True)
    token_id = models.TextField(db_column='TokenID', blank=True, null=True)
    application_type = models.TextField(db_column='ApplicationType', blank=True, null=True)
    sequence_number = models.TextField(db_column='SequenceNumber', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'netposition'
        unique_together = (('trading_symbol',),)



# from django.contrib.admin import AdminSite
# from django.utils.translation import gettext_lazy as _
#
# class MyAdminSite(AdminSite):
#     site_header = _('My Site Header')
#     site_title = _('My Site Title')
#     index_title = _('My Index Title')
#
# admin_site = MyAdminSite(name='myadmin')

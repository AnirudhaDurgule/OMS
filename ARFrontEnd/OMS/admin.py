from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .resources import *

# Register your models here.

from .models import *
# Register your models here.
#admin.site.register(Client_Model)
#admin.site.register(applicationUserTypes)
#admin.site.register(applicationSettings)
#admin.site.register(ClientTransaction1)

admin.site.register(Watchlist)

admin.site.register(WatchListDetails)
admin.site.register(UserOrderLimitMaster)
admin.site.register(UserOrderLimit)
admin.site.register(UserExposureLimitMaster)
admin.site.register(UserExposureOrderLimit)
admin.site.register(ClientStrategyOrderFiller)





@admin.register(Client_Model)
class ExistingClientDetailExportAdmin(ImportExportModelAdmin):

    list_display = ['clientID', 'mobileNumber', 'emailID', 'panNumber', ]
    search_fields = ['clientID', 'mobileNumber', 'emailID', 'panNumber', ]
    resource_class = ExistingClientDetailResource
    search_help_text = f'search in: {", ".join(search_fields)}'


   



@admin.register(IncomingOrder)
class IncomingOrderImportExportAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in IncomingOrder._meta.fields if field.name != "id"]
    search_fields = ['clientCode', 'symbol', 'instrumentName']
    resource_class = IncomingOrderResource



@admin.register(MorningOpenPosition)
class MorningOpenPositionImportExportAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in MorningOpenPosition._meta.fields if field.name != "id"]
    search_fields = ['clientCode', 'tickerCode', 'underlyingSymbol']
    resource_class = MorningOpenPositionResource


@admin.register(OrderBook)
class OrderBookImportExportAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in OrderBook._meta.fields if field.name != "id"]
    search_fields = ['accountNumber', 'symbol', 'instrumentName']
    resource_class = OrderBookResource


@admin.register(TradeBook)
class TradeBookImportExportAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in TradeBook._meta.fields if field.name != "id"]
    search_fields = ['accountNumber', 'symbol', 'instrumentName']
    resource_class = TradeBookResource


@admin.register(PendingOrders)
class PendingOrdersImportExportAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in PendingOrders._meta.fields if field.name != "id"]
    search_fields = ['accountNumber', 'symbol', 'instrumentName']
    resource_class = PendingOrdersResource
    search_help_text = "Enter search terms to find matching pending orders."



@admin.register(BanSymbol)
class BanSymbolImportExportAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in BanSymbol._meta.fields if field.name != "id"]
    search_fields = ['symbol']
    resource_class = BanSymbolResource


@admin.register(FreezeQuantity)
class FreezeQuantityImportExportAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in FreezeQuantity._meta.fields if field.name != "id"]
    search_fields = ['symbol']
    resource_class = FreezeQuantityResource


@admin.register(NetPositionTable)
class NetPositionTableImportExportAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in NetPositionTable._meta.fields]
    search_fields = ['clientCode', 'tickerCode', 'underlyingSymbol']
    resource_class = NetPositionTableResource



@admin.register(NseFnoSymbol)
class NseFnoSymbolAdmin(admin.ModelAdmin):
    list_display = ('underlying_name', 'exchange', 'segment')

@admin.register(ClientTable)
class ClientTableAdmin(admin.ModelAdmin):
    list_display = ('clientCode', 'name', 'emailID', 'phoneNumber', 'squareOff', 'banned', 'proClientIndicator')

@admin.register(ClientUnderlyingSymbol)
class ClientUnderlyingSymbolAdmin(admin.ModelAdmin):
    list_display = ('client', 'underlying_name')

@admin.register(RejectReasonCodeDetails)
class RejectReasonCodeDetailsAdmin(ImportExportModelAdmin):
    resource_class = RejectReasonCodeDetailsResource
    list_display = ('reasonCode', 'reason')  
    search_fields = ('reasonCode', 'reason') 

@admin.register(LPPRange)
class LPPRangeAdmin(ImportExportModelAdmin):
    resource_class = LPPRangeResource
    list_display = ('InstrumentName', 'token','upperPriceRange','lowerPriceRange','ltp','bid1Price','bid1Quantity','ask1Price','ask1Quantity')  
    search_fields = ('InstrumentName', 'token') 



@admin.register(StrategyManager)
class StrategyManagerAdmin(ImportExportModelAdmin):
    resource_class = StrategyManagerResources
    list_display = ('strategyName', 'fileName','description','algoID')  
    search_fields = ('strategyName','fileName') 


@admin.register(ClientStrategyManager)
class ClientStrategyManagerAdmin(ImportExportModelAdmin):
    resource_class = ClientStrategyManagerResources
    list_display = ('strategyID_id', 'clientID','algoID')  
    search_fields = ('strategyID_id', 'clientID') 

@admin.register(PriceHistory)
class PriceHistoryAdmin(ImportExportModelAdmin):
    resource_class = PriceHistoryResources
    list_display = ( 'id',
            'tokenNumber',
            'exchange',
            'segment',
            'ltp',
            'ltq',
            'ltt',
            'lut',
            'pc',
            'openPrice',
            'highPrice',
            'lowPrice',
            'closePrice',
            'atp',
            'atv',
            'dayhigh',
            'dayLow',
            'oi',
            'volume',
            'bidPrice',
            'bidQuantity',
            'bidOrders',
            'askPrice',
            'askQuantity',
            'askOrders',
            'dayHighOI',
            'dayLowOI',
            'dprHigh',
            'dprLow')  
    search_fields = ('tokenNumber',) 

class LogFileAdmin(admin.ModelAdmin):
    readonly_fields = ['content']

    def has_add_permission(self, request, obj=None):
        # Disable adding new entries, as we are only viewing logs.
        return False

    def has_delete_permission(self, request, obj=None):
        # Disable deleting entries.
        return False

admin.site.register(LogFile, LogFileAdmin)
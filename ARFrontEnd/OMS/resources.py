
from import_export.widgets import ForeignKeyWidget
from .models import *
from import_export import resources,fields



class ExistingClientDetailResource(resources.ModelResource):
    class Meta:
        model = Client_Model
        import_id_fields = ('clientID',)
        exclude = ('id',)
    

class IncomingOrderResource(resources.ModelResource):
    class Meta:
        model = IncomingOrder

class MorningOpenPositionResource(resources.ModelResource):
    class Meta:
        model = MorningOpenPosition

class OrderBookResource(resources.ModelResource):
    class Meta:
        model = OrderBook

class TradeBookResource(resources.ModelResource):
    class Meta:
        model = TradeBook

class PendingOrdersResource(resources.ModelResource):
    class Meta:
        model = PendingOrders

class BanSymbolResource(resources.ModelResource):
    class Meta:
        model = BanSymbol

class FreezeQuantityResource(resources.ModelResource):
    class Meta:
        model = FreezeQuantity

class NetPositionTableResource(resources.ModelResource):
    class Meta:
        model = NetPositionTable
class RejectReasonCodeDetailsResource(resources.ModelResource):
    class Meta:
        model = RejectReasonCodeDetails
        fields = ('id', 'reasonCode', 'reason')  
        export_order = ('id', 'reasonCode', 'reason') 
class LPPRangeResource(resources.ModelResource):
    class Meta:
        model = LPPRange
        fields = ('id', 'InstrumentName', 'token','upperPriceRange','lowerPriceRange','ltp')  
        export_order = ('id', 'InstrumentName', 'token','upperPriceRange','lowerPriceRange','ltp') 

class StrategyManagerResources(resources.ModelResource):
    class Meta:
        model = StrategyManager
        fields = ('id', 'strategyName', 'fileName','description')  
        export_order = ('id', 'strategyName', 'fileName','description') 


class ClientStrategyManagerResources(resources.ModelResource):
    class Meta:
        model = StrategyManager
        fields = ('id', 'strategyName', 'fileName','description')  
        export_order = ('id', 'strategyName', 'fileName','description') 

class PriceHistoryResources(resources.ModelResource):
    class Meta:
        model = PriceHistory
        fields = (
            'id',
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
            'askPrice',
            'askQuantity',
            'dayHighOI',
            'dayLowOI',
            'dprHigh',
            'dprLow')  
        export_order = (
            'id',
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
            'dprLow',) 





'''
class NseFnoSymbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = NseFnoSymbol
        fields = '__all__'

class ClientTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientTable
        fields = '__all__'

class ClientUnderlyingSymbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientUnderlyingSymbol
        fields = '__all__'
'''


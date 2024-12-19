from django.db import models

# Create your models here.

from django.db import models
from hashids import Hashids

from binascii import hexlify, unhexlify
# Create your models here.

from django.utils import timezone
import time,os, subprocess
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import ArrayField  # Import ArrayField


# Create your models here.

def return_date_time():
    now = timezone.now()
    return now

class Unique_Identifier (models.Model):
    uniqueIdentifier = models.CharField (max_length=20,  default='AAA')
    def save(self, **kwargs):
        super().save(*kwargs)
        if self.pk:
            code = self.pk
            self.uniqueIdentifier = '{}{}'.format('abc',code)
            super().save(*kwargs)


class Client_Model(models.Model):
    clientID = models.CharField(default='aaa', max_length=10, primary_key=True)
    choices = (('mobile', 'mobile'), ('web', 'web'), ('window_desktop', 'window_desktop'),
               ('mac_desktop', 'mac_desktop'), ('linux_desktop', 'linux_desktop'))
    source = models.CharField(max_length=40, choices=choices, default='mobile')
    secretKey = models.CharField(default='aaa', max_length=50)
    token = models.CharField(max_length=500, blank=False, default='aaa')
    appKey =  models.CharField(max_length=50, blank=False, default='aaa')
    mobileNumber =  models.CharField(max_length=20, blank=True, default='7325903013')
    guestUser = models.BooleanField(default=False)
    panNumber = models.CharField(max_length=20, blank=True, default='AAAAA')
    allowUserToContinue = models.BooleanField(default=False)
    clientName = models.CharField(max_length=200, blank=True)
    emailID = models.CharField(max_length=100, blank=True)
    upiLink = models.CharField(max_length=200, blank=True)
    rmsLink = models.CharField(max_length=600, blank=True, editable=False)
    password = models.CharField(max_length=100, blank=False, editable=False)
    newPassword = models.CharField(max_length=100, blank=True, editable=False)
    passwordLastChange = models.IntegerField(max_length=10, default=0, editable=False)
    userNeedToResetPassword = models.BooleanField(default=False)
    totalMarginAvailable = models.FloatField(default=0)
    totalMarginUsed = models.FloatField(default=0)
    totalOptionBuy = models.FloatField(default=0)
    totalFutureMTM = models.FloatField(default=0)
    blockForTrading = models.BooleanField(default=False)
    numberOfPasswordChange = models.IntegerField(max_length=10, default=0, editable=False)
    lastFivePassword=models.CharField(max_length=1000, blank=True, editable=False)



    class Meta:
        db_table = 'Client_Details'
        managed=False
        
    

    def __str__(self):
        return self.clientID
    def save(self, *args, **kwargs):
        # Retrieve the current instance from the database
        try:
            if self.pk:
                previous = Client_Model.objects.get(pk=self.pk)
                if previous.password != self.password:
                    self.passwordLastChange= time.time()
            if self.userNeedToResetPassword:
                self.password="ABC@123"
        except Exception as e:
            pass
        super(Client_Model, self).save(*args, **kwargs)

    
class ClientTransaction1(models.Model):
    ClientCode = models.CharField(default='aaa', max_length=10)
    API_INITIATION_TIME = models.CharField(default="NONE", blank=True, max_length=50,  )
    API_RESPONSE_TIME = models.CharField(default="NONE", blank=True, max_length=50, )
    TotalTimeConsumed = models.FloatField(max_length=10, default=0.0, )
    Payload = models.CharField(default="NONE", blank=True, max_length=200,)
    Response = models.TextField(default="NONE", blank=False, )
    choices = (('Client_Login', 'Client_Login'), ('Client_Token', 'Client_Token'),
               ('Order_Execution', 'Order_Execution'),
               ('Order_Modification', 'Order_Modification'), ('Order_Cancellation', 'Order_Cancellation'),
               ('Log_Off', 'Log_Off'), ('Order_Book', 'Order_Book'),
               ('Cover_Order_Execution', 'Cover_Order_Execution'),
               ('Cover_Order_Cancellation', 'Cover_Order_Cancellation'),
               ('Bracket_Order_Execution', 'Bracket_Order_Execution'),
               ('Bracket_Order_Modification', 'Bracket_Order_Modification'),
               ('Bracket_Order_Cancellation', 'Bracket_Order_Cancellation'),
               ('Order_History', 'Order_History'), ('Trade_Book', 'Trade_Book'),
               ('Holding', 'Holding'), ('Day_Position', 'Day_Position'),('Net_Position', 'Net_Position'),
               ('Position_Convert', 'Position_Convert'), ('Order_Status', 'Order_Status'),
               ('Balance_Status','Balance_Status'), ('Cancel_All_Order', 'Cancel_All_Order'),
               ('Order_Square_Off','Order_Square_Off'), ('All_Order_Square_Off', 'All_Order_Square_Off')
               )
    RequestType = models.CharField(max_length=40, choices=choices, default='Client_Login', editable=False)
    def __str__(self):
        return str(self.ClientCode+' '+self.RequestType)
class applicationUserTypes(models.Model):
    userType = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.userType
    def __str__(self):
        return self.userType
class applicationSettings(models.Model):
    userType = models.ForeignKey(applicationUserTypes, on_delete=models.CASCADE)
    broadcastSocket = models.CharField(max_length=200,blank=True )
    OMSSocket = models.CharField(max_length=200, blank =True)
    watchlistFetchAPI = models.CharField(max_length=200, blank =True)
    wathclistAddAPI = models.CharField(max_length=200, blank=True)
    wathcListDeleteAPI =  models.CharField(max_length=200, blank=True)
    pricebandURL = models.CharField(max_length=200, blank=True)
    netPositionAPI = models.CharField(max_length=200, blank=True)
    tradeBookAPI = models.CharField(max_length=200, blank=True)
    orderBookAPI =models.CharField(max_length=200, blank=True)
    orderHistoryAPI  = models.CharField(max_length=200, blank=True)
    clientHoldingAPI = models.CharField(max_length=200, blank=True)
    tickerPriceSearchAPI = models.CharField(max_length=200, blank=True)
    tickerTechnicalIndicatorSearchAPI = models.CharField(max_length=200, blank=True)
    callAndTradeAPI = models.CharField(max_length=200, blank=True)
    def __unicode__(self):
        return self.userType.userType

    def __str__(self):
        return self.userType.userType
class ATSClientDetailsTable(models.Model):
    client_code = models.CharField(max_length=10, unique=True, default="aaa")
    client_name = models.CharField(max_length=200, blank=False)
    mobile_number = models.CharField(max_length=50, blank=True)
    email_id = models.CharField(max_length=100, blank=True)
    pan_id = models.CharField(max_length=20, blank=True)
    demat_id = models.CharField(max_length=200, blank=True)

    def save(self, **kwargs):
        try:
            object = Client_Model()
            object.clientID = self.client_code
            object.mobileNumber = self.mobile_number
            object.clientName = self.client_name
            object.emailID = self.email_id
            object.guestUser = False
            object.panNumber = self.pan_id
            object.emailID = self.email_id
            upiCode = encode(self.client_code)
            final_url = "http://upi.adityatrading.in/simplefundtransfermain/{}/".format(upiCode)
            object.upiLink = final_url
            object.save()
            super().save(*kwargs)
        except Exception as e:
            print(e)

'''
class applicationUserTypes(models.Model):
    userType = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.userType
    def __str__(self):
        return self.userType
    


class applicationSettings(models.Model):
    userType = models.ForeignKey(applicationUserTypes, on_delete=models.CASCADE)
    broadcastSocket = models.CharField(max_length=200,blank=True )
    OMSSocket = models.CharField(max_length=200, blank =True)
    watchlistFetchAPI = models.CharField(max_length=200, blank =True)
    wathclistAddAPI = models.CharField(max_length=200, blank=True)
    wathcListDeleteAPI =  models.CharField(max_length=200, blank=True)
    pricebandURL = models.CharField(max_length=200, blank=True)
    netPositionAPI = models.CharField(max_length=200, blank=True)
    tradeBookAPI = models.CharField(max_length=200, blank=True)
    orderBookAPI =models.CharField(max_length=200, blank=True)
    orderHistoryAPI  = models.CharField(max_length=200, blank=True)
    clientHoldingAPI = models.CharField(max_length=200, blank=True)
    tickerPriceSearchAPI = models.CharField(max_length=200, blank=True)
    tickerTechnicalIndicatorSearchAPI = models.CharField(max_length=200, blank=True)
    callAndTradeAPI = models.CharField(max_length=200, blank=True)
    def __unicode__(self):
        return self.userType.userType

    def __str__(self):
        return self.userType.userType






class ATSClientDetailsTable(models.Model):
    client_code = models.CharField(max_length=10, unique=True, default="aaa")
    client_name = models.CharField(max_length=200, blank=False)
    mobile_number = models.CharField(max_length=50, blank=True)
    email_id = models.CharField(max_length=100, blank=True)
    pan_id = models.CharField(max_length=20, blank=True)
    demat_id = models.CharField(max_length=200, blank=True)

    def save(self, **kwargs):
        try:
            object = Client_Model()
            object.clientID = self.client_code
            object.mobileNumber = self.mobile_number
            object.clientName = self.client_name
            object.emailID = self.email_id
            object.guestUser = False
            object.panNumber = self.pan_id
            object.emailID = self.email_id
            upiCode = encode(self.client_code)
            final_url = "http://upi.adityatrading.in/simplefundtransfermain/{}/".format(upiCode)
            object.upiLink = final_url
            object.save()
            super().save(*kwargs)
        except Exception as e:
            print(e)

class BankDetails (models.Model):
    client_code = models.ForeignKey(ATSClientDetailsTable, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=15, blank=False)
    mobile_number = models.CharField(max_length=50, blank=True)
    email_id = models.CharField(max_length=100, blank=True)
    pan_id = models.CharField(max_length=20, blank=True)
    demat_id = models.CharField(max_length=200, blank=True)


class Unique_Identifier (models.Model):
    uniqueIdentifier = models.CharField (max_length=20,  default='AAA')
    def save(self, **kwargs):
        super().save(*kwargs)
        if self.pk:
            code = self.pk
            self.uniqueIdentifier = '{}{}'.format('abc',code)
            super().save(*kwargs)


'''

class BytesIntEncoder:

    @staticmethod
    def encode(b: bytes) -> int:
        return int(hexlify(b), 16) if b != b'' else 0

    @staticmethod
    def decode(i: int) -> int:
        return unhexlify('%x' % i) if i != 0 else b''

def encode(client_code):
    s = client_code
    b = s.encode()
    hashids = Hashids(salt="UPI Ats payment gateway", alphabet='abcdefghijklmnopqrstuvwxyz', min_length=25)
    test = BytesIntEncoder.encode(b)
    code = hashids.encode(test)
    return code


class UserOrderLimitMaster(models.Model):
    maximumAllowedModification = models.BigIntegerField(default=0)
    maximumOpenBuyQuantity = models.BigIntegerField(default=0)
    maximumOpenOrdersValue = models.BigIntegerField(default=0)
    maximumOpenSellQuantity = models.BigIntegerField(default=0)
    maximumOrderQuantity = models.BigIntegerField(default=0)
    maximumOrderValue = models.BigIntegerField(default=0)
    def __str__(self):
            return "user_order_limit_master"
    class Meta:
            db_table = 'user_order_limit_master'
            managed=True




class UserOrderLimit(models.Model):
    userName=models.ForeignKey(Client_Model, on_delete=models.CASCADE)
    choices = (('limit', 'limit'), ('ioc', 'ioc'), ('limitMarket', 'limitMarket'),
               ('all', 'all'))
    source = models.CharField(max_length=40, choices=choices, default='mobile', unique=False)
    userAllowedOrderType = models.CharField(max_length=40, choices=choices, default='all', unique=False)
    ltpAllowedLimitPriceDifference = models.IntegerField(default=10)
    maximumAllowedModification = models.IntegerField(default=0, max_length=20)
    maximumOpenBuyQuantity = models.IntegerField(default=0, max_length=20)
    maximumOpenOrdersValue = models.IntegerField(default=0, max_length=20)
    maximumOpenSellQuantity = models.IntegerField(default=0, max_length=20)
    maximumOrderQuantity = models.IntegerField(default=0, max_length=20)
    maximumOrderValue = models.IntegerField(default=0, max_length=20)
    def __str__(self):
            return self.userName.clientID
    class Meta:
            db_table = 'user_order_limit'
            managed=True
            verbose_name_plural = "UserOrderLimit"  
    
    def save(self, **kwargs):
        #super().save(*kwargs)
        data = UserOrderLimitMaster.objects.first()
        if self.maximumAllowedModification > data.maximumAllowedModification:
            self.maximumAllowedModification=data.maximumAllowedModification
        if self.maximumOpenBuyQuantity > data.maximumOpenBuyQuantity:
            self.maximumOpenBuyQuantity= data.maximumOpenBuyQuantity
        if self.maximumOpenOrdersValue > data.maximumOpenOrdersValue:
            self.maximumOpenOrdersValue= data.maximumOpenOrdersValue
        if self.maximumOpenSellQuantity > data.maximumOpenSellQuantity:
            self.maximumOpenSellQuantity= data.maximumOpenSellQuantity
        if self.maximumOrderQuantity > data.maximumOrderQuantity:
            self.maximumOrderQuantity= data.maximumOrderQuantity
        
        if self.maximumOrderValue > data.maximumOrderValue:
            self.maximumOrderValue= data.maximumOrderValue
        
        
        super().save(*kwargs)



class UserExposureLimitMaster(models.Model):
    maximumDayTurnover = models.BigIntegerField(default=0)
    maximumExposure = models.BigIntegerField(default=0)
    maximumMTM = models.BigIntegerField(default=0)
    maximumPosition = models.BigIntegerField(default=0)
    def __str__(self):
            return "user_exposure_limit_master"
    class Meta:
            db_table = 'user_exposure_limit_master'
            managed=True


class RejectReasonCodeDetails(models.Model):
    reasonCode = models.BigIntegerField(default=0)
    reason = models.CharField(max_length=300, default="")
    def __str__(self):
            return "reject_reason_code"
    class Meta:
            db_table = 'reject_reason_code_master'
            managed=True
            verbose_name_plural = "RejectReason"  




class UserExposureOrderLimit(models.Model):
    userName=models.ForeignKey(Client_Model, on_delete=models.CASCADE)
    maximumDayTurnover = models.BigIntegerField(default=0)
    maximumExposure = models.BigIntegerField(default=0)
    maximumMTM = models.BigIntegerField(default=0)
    maximumPosition = models.BigIntegerField(default=0)

    
    def __str__(self):
            return self.userName.clientID
    class Meta:
            db_table = 'user_exposure_limit'
            managed=True
    
    def save(self, **kwargs):
        #super().save(*kwargs)
        data = UserExposureLimitMaster.objects.first()
        if self.maximumDayTurnover > data.maximumDayTurnover:
            self.maximumDayTurnover=data.maximumDayTurnover
        if self.maximumExposure > data.maximumExposure:
            self.maximumExposure= data.maximumExposure
        if self.maximumMTM > data.maximumMTM:
            self.maximumMTM= data.maximumMTM
        if self.maximumPosition > data.maximumPosition:
            self.maximumPosition= data.maximumPosition
        super().save(*kwargs)








   




class Watchlist(models.Model):
    userName=models.ForeignKey(Client_Model, on_delete=models.CASCADE)
    choices = (('mobile', 'mobile'), ('web', 'web'), ('window_desktop', 'window_desktop'),
               ('mac_desktop', 'mac_desktop'), ('linux_desktop', 'linux_desktop'))
    source = models.CharField(max_length=40, choices=choices, default='mobile', unique=False)

    def __str__(self):
        return self.userName.clientID
    class Meta:
        db_table = 'Watchlist'
        managed=True
class WatchListDetails(models.Model):
    watchlist = models.ForeignKey(Watchlist, on_delete=models.CASCADE)
    securityName = models.CharField(max_length=100, blank=False, default='NIFTY')
    segment = models.CharField(max_length=4, default='CM', blank=True)
    token = models.CharField(max_length=10, blank=False, default='1594')
    exchange = models.CharField(max_length=10, blank=False, default='NSE')
    tokenID= models.CharField(max_length=10, blank=True, default='aaaa')
    created = models.DateTimeField(default=return_date_time)
    def save(self, **kwargs):
        super().save(*kwargs)
        if self.tokenID=='aaaa':
            self.tokenID = self.exchange + self.segment + self.token
            super().save(*kwargs)
    class Meta:
        db_table = 'WatchListDetails'
        managed=True




#######################################################################new models##############################################################

class IncomingOrder(models.Model):
    tokenNumber = models.IntegerField()
    orderType = models.CharField(max_length=50)
    instrumentName = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50)
    expiryDate = models.BigIntegerField()
    strikePrice = models.IntegerField()
    optionType = models.CharField(max_length=2)
    buySellIndicator = models.IntegerField()
    price = models.BigIntegerField()
    volume = models.IntegerField()
    market = models.IntegerField()
    disclosedVolume = models.IntegerField()
    triggerPrice = models.DecimalField(max_digits=10, decimal_places=2)
    nnfField = models.BigIntegerField()
    clientCode = models.CharField(max_length=50)
    GTD = models.IntegerField()
    pan = models.CharField(max_length=20)
    bookType = models.IntegerField()
    ATO = models.IntegerField()
    day = models.IntegerField()
    MIT = models.IntegerField()
    GTC = models.IntegerField()
    IOC = models.IntegerField()
    AON = models.IntegerField()
    SL = models.IntegerField()
    MF = models.IntegerField()
    openClose = models.CharField(max_length=1)
    proClientIndicator = models.IntegerField()
    STPC = models.IntegerField()
    COL = models.IntegerField()
    BOC = models.IntegerField()
    parentClientCode = models.CharField(max_length=50)
    strategyRemarks = models.IntegerField()
    class Meta:
        db_table = 'incoming_order'


class MorningOpenPosition(models.Model):
    clientCode = models.CharField(max_length=100)
    tokenID = models.BigIntegerField(max_length=100)
    exchange = models.CharField(max_length=50)
    segment = models.CharField(max_length=50)
    tickerCode = models.CharField(max_length=100)
    optionType = models.CharField(max_length=50)
    underlyingSymbol = models.CharField(max_length=50)
    underlyingToken = models.CharField(max_length=50)
    finalQuantity = models.BigIntegerField()
    expiry = models.BigIntegerField()
    netPrice = models.BigIntegerField()
    class Meta:
        db_table = 'morning_open_position'


class OrderBook(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    transactionCode = models.BigIntegerField()
    logTime = models.BigIntegerField()
    userID = models.BigIntegerField()
    errorCode = models.CharField(max_length=400, default="")
    timeStamp1 = models.BigIntegerField(null=True, blank=True)
    timeStamp2 = models.CharField(max_length=1, null=True, blank=True)
    modifiedCancelledBy = models.CharField(max_length=1, null=True, blank=True)
    reasonCode = models.BigIntegerField(null=True, blank=True)
    tokenNo = models.BigIntegerField()
    instrumentName = models.CharField(max_length=6)
    symbol = models.CharField(max_length=10)
    expiryDate = models.BigIntegerField(null=True, blank=True)
    strikePrice = models.BigIntegerField(null=True, blank=True)
    optionType = models.CharField(max_length=2)
    closeOutFlag = models.CharField(max_length=1, null=True, blank=True)
    orderNumber = models.FloatField()
    accountNumber = models.CharField(max_length=10)
    bookType = models.BigIntegerField(null=True, blank=True)
    buySellIndicator = models.BigIntegerField()
    buySellAction = models.CharField(max_length=4, null=True, blank=True)
    disclosedVolume = models.BigIntegerField(null=True, blank=True)
    disclosedVolumeRemaining = models.BigIntegerField(null=True, blank=True)
    totalVolumeRemaining = models.BigIntegerField(null=True, blank=True)
    volume = models.BigIntegerField()
    volumeFilledToday = models.BigIntegerField(null=True, blank=True)
    price = models.BigIntegerField()
    triggerPrice = models.BigIntegerField(default=0)
    goodTillDate = models.BigIntegerField()
    entryDateTime = models.BigIntegerField(null=True, blank=True)
    lastModified = models.BigIntegerField(null=True, blank=True)
    ATO = models.BigIntegerField(default=0)
    market = models.BigIntegerField(default=0)
    SL = models.BigIntegerField(default=0)
    MIT = models.BigIntegerField(default=0)
    day = models.BigIntegerField(default=0)
    GTC = models.BigIntegerField(default=0)
    IOC = models.BigIntegerField(default=0)
    AON = models.BigIntegerField(default=0)
    MF = models.BigIntegerField(default=0)
    matchedInd = models.BigIntegerField(default=0)
    traded = models.BigIntegerField(default=0)
    modified = models.BigIntegerField(default=0)
    frozen = models.BigIntegerField(default=0)
    branchID = models.BigIntegerField(default=0)
    traderID = models.BigIntegerField(default=0)
    brokerID = models.CharField(max_length=5, default='')
    openClose = models.CharField(max_length=1, null=True, blank=True)
    settlor = models.CharField(max_length=12, default='', null=True, blank=True)
    proClientIndicator = models.BigIntegerField(null=True, blank=True)
    STPC = models.BigIntegerField(default=0)
    COL = models.BigIntegerField(default=0)
    BOC = models.BigIntegerField(default=0)
    NNF = models.FloatField(default=0)
    timeStamp3 = models.BigIntegerField(null=True, blank=True)
    PAN = models.CharField(max_length=10, null=True, blank=True)
    algoID = models.BigIntegerField(null=True, blank=True)
    lastActivityReference = models.BigIntegerField(null=True, blank=True)
    strategyRemarks = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = 'order_book'
        managed= False


class TradeBook(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    transactionCode = models.BigIntegerField()
    logTime = models.BigIntegerField()
    traderID = models.BigIntegerField()
    timeStamp = models.BigIntegerField(null=True, blank=True)
    timeStamp1 = models.FloatField(null=True, blank=True)
    timeStamp2 = models.FloatField(null=True, blank=True)
    responseOrderNumber = models.FloatField(null=True, blank=True)
    brokerID = models.CharField(max_length=5)
    accountNumber = models.CharField(max_length=10)
    buySellIndicator = models.BigIntegerField()
    originalVolume = models.BigIntegerField(null=True, blank=True)
    disclosedVolume = models.BigIntegerField(null=True, blank=True)
    remainingVolume = models.BigIntegerField(null=True, blank=True)
    price = models.BigIntegerField(null=True, blank=True)
    ATO = models.BigIntegerField(default=0)
    market = models.BigIntegerField(default=0)
    SL = models.BigIntegerField(default=0)
    MIT = models.BigIntegerField(default=0)
    day = models.BigIntegerField(default=0)
    GTC = models.BigIntegerField(default=0)
    IOC = models.BigIntegerField(default=0)
    AON = models.BigIntegerField(default=0)
    MF = models.BigIntegerField(default=0)
    matchedInd = models.BigIntegerField(default=0)
    traded = models.BigIntegerField(default=0)
    modified = models.BigIntegerField(default=0)
    frozen = models.BigIntegerField(default=0)
    goodTillDate = models.BigIntegerField()
    fillNumber = models.BigIntegerField(null=True, blank=True)
    fillQuantity = models.BigIntegerField(null=True, blank=True)
    fillPrice = models.BigIntegerField(null=True, blank=True)
    volumeFilledToday = models.BigIntegerField(null=True, blank=True)
    activityType = models.CharField(max_length=2, null=True, blank=True)
    activityTime = models.BigIntegerField(null=True, blank=True)
    tokenNo = models.BigIntegerField(null=True, blank=True)
    instrumentName = models.CharField(max_length=6)
    symbol = models.CharField(max_length=10)
    expiryDate = models.BigIntegerField(null=True, blank=True)
    strikePrice = models.BigIntegerField(null=True, blank=True)
    optionType = models.CharField(max_length=2)
    openClose = models.CharField(max_length=1, null=True, blank=True)
    bookType = models.BigIntegerField(null=True, blank=True)
    participant = models.CharField(max_length=12, null=True, blank=True)
    STPC = models.BigIntegerField(default=0)
    COL = models.BigIntegerField(default=0)
    BOC = models.BigIntegerField(default=0)
    PAN = models.CharField(max_length=10, null=True, blank=True)
    algoID = models.BigIntegerField(null=True, blank=True)
    lastActivityReference = models.BigIntegerField(null=True, blank=True)
    counterTraderOrderNumber = models.FloatField(null=True, blank=True)
    counterBrokerID = models.CharField(max_length=5, null=True, blank=True)
    class Meta:
        db_table = 'trade_book'
        managed= False


class PendingOrders(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    transactionCode = models.BigIntegerField()
    logTime = models.BigIntegerField()
    userID = models.BigIntegerField()
    errorCode = models.CharField(max_length=400, default="")
    timeStamp1 = models.BigIntegerField(null=True, blank=True)
    timeStamp2 = models.CharField(max_length=1, null=True, blank=True)
    modifiedCancelledBy = models.CharField(max_length=1, null=True, blank=True)
    reasonCode = models.BigIntegerField(null=True, blank=True)
    tokenNo = models.BigIntegerField()
    instrumentName = models.CharField(max_length=6)
    symbol = models.CharField(max_length=10)
    expiryDate = models.BigIntegerField(null=True, blank=True)
    strikePrice = models.BigIntegerField(null=True, blank=True)
    optionType = models.CharField(max_length=2)
    closeOutFlag = models.CharField(max_length=1, null=True, blank=True)
    orderNumber = models.DecimalField(max_digits=25, decimal_places=1)
    accountNumber = models.CharField(max_length=10)
    bookType = models.BigIntegerField(null=True, blank=True)
    buySellIndicator = models.BigIntegerField()
    buySellAction = models.CharField(max_length=4, null=True, blank=True)
    disclosedVolume = models.BigIntegerField(null=True, blank=True)
    disclosedVolumeRemaining = models.BigIntegerField(null=True, blank=True)
    totalVolumeRemaining = models.BigIntegerField(null=True, blank=True)
    volume = models.BigIntegerField()
    volumeFilledToday = models.BigIntegerField(null=True, blank=True)
    price = models.BigIntegerField()
    triggerPrice = models.BigIntegerField(default=0)
    goodTillDate = models.BigIntegerField()
    entryDateTime = models.BigIntegerField(null=True, blank=True)
    lastModified = models.BigIntegerField(null=True, blank=True)
    ATO = models.BigIntegerField(default=0)
    market = models.BigIntegerField(default=0)
    SL = models.BigIntegerField(default=0)
    MIT = models.BigIntegerField(default=0)
    day = models.BigIntegerField(default=0)
    GTC = models.BigIntegerField(default=0)
    IOC = models.BigIntegerField(default=0)
    AON = models.BigIntegerField(default=0)
    MF = models.BigIntegerField(default=0)
    matchedInd = models.BigIntegerField(default=0)
    traded = models.BigIntegerField(default=0)
    modified = models.BigIntegerField(default=0)
    frozen = models.BigIntegerField(default=0)
    branchID = models.BigIntegerField(default=0)
    traderID = models.BigIntegerField(default=0)
    brokerID = models.CharField(max_length=5, default='')
    openClose = models.CharField(max_length=1, null=True, blank=True)
    settlor = models.CharField(max_length=12, default='', null=True, blank=True)
    proClientIndicator = models.BigIntegerField(null=True, blank=True)
    STPC = models.BigIntegerField(default=0)
    COL = models.BigIntegerField(default=0)
    BOC = models.BigIntegerField(default=0)
    NNF = models.FloatField(default=0)
    timeStamp3 = models.BigIntegerField(null=True, blank=True)
    PAN = models.CharField(max_length=10, null=True, blank=True)
    algoID = models.BigIntegerField(null=True, blank=True)
    lastActivityReference = models.BigIntegerField(null=True, blank=True)
    strategyRemarks = models.BigIntegerField(null=True, blank=True)
    orderStatus = models.CharField(max_length=100, default='pending')

    class Meta:
        unique_together = ('traderID', 'orderNumber')
        db_table = 'pending_orders'
        managed=True
        


class BanSymbol(models.Model):
    symbol = models.CharField(max_length=12)
    class Meta:
        db_table = 'ban_symbol'
        managed=False
        verbose_name_plural = "BanSymbol"  


class FreezeQuantity(models.Model):
    symbol = models.CharField(max_length=12)
    quantity = models.BigIntegerField()
    class Meta:
        db_table = 'freeze_quantity'
        managed=False
        verbose_name_plural = "FreezeQuantity"  


class NetPositionTable(models.Model):
    clientCode = models.CharField(max_length=100)
    tokenID = models.CharField(max_length=100)
    exchange = models.CharField(max_length=50)
    segment = models.CharField(max_length=50)
    tickerCode = models.CharField(max_length=100)
    optionType = models.CharField(max_length=50)
    underlyingSymbol = models.CharField(max_length=50)
    underlyingToken = models.CharField(max_length=50)
    finalQuantity = models.BigIntegerField()
    expiry = models.BigIntegerField()
    netValue = models.BigIntegerField()
    bookedProfit=models.FloatField()

    class Meta:
        unique_together = ('clientCode', 'tokenID')
        db_table = 'net_position_client'
        managed=False
        #primary_key = ('clientCode', 'tokenID')

class NseFnoSymbol(models.Model):
    underlying_name = models.CharField(max_length=100, primary_key=True)
    exchange = models.CharField(max_length=50)
    segment = models.CharField(max_length=50)
    class Meta:
        db_table = 'nse_fno_symbol'
        managed=False

class ClientTable(models.Model):
    clientCode = models.CharField(max_length=100, primary_key=True)
    panCode = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    emailID = models.CharField(max_length=100)
    phoneNumber = models.BigIntegerField()
    squareOff = models.BooleanField()
    banned = models.BooleanField()
    proClientIndicator = models.BigIntegerField()
    class Meta:
        db_table = 'client_table'
        managed=False


class ClientUnderlyingSymbol(models.Model):
    client = models.ForeignKey(ClientTable, on_delete=models.CASCADE)
    underlying_name = models.ForeignKey(NseFnoSymbol, on_delete=models.CASCADE)
    class Meta:
        db_table = 'client_underlying_banned_symbol'
        unique_together = ('client', 'underlying_name')
        managed=False


class LPPRange(models.Model):
    InstrumentName = models.CharField(max_length=100)
    token   = models.BigIntegerField(default=0)
    upperPriceRange   = models.FloatField(default=0.0)
    lowerPriceRange = models.FloatField(default=0.0)
    ltp = models.FloatField(default=0.0)
    bid1Price = models.FloatField(default=0.0)
    bid1Quantity = models.FloatField(default=0.0)
    ask1Price = models.FloatField(default=0.0)
    ask1Quantity = models.FloatField(default=0.0)


    class Meta:
        db_table = 'lpp_range'
        managed=True
        verbose_name_plural = "LPPRange"  


class StrategyManager(models.Model):
    strategyName = models.CharField(max_length=100, unique=True, primary_key=True)
    fileName   = models.CharField(default=0,max_length=100)
    algoID = algoID = models.BigIntegerField(null=True, blank=True)  
    description   = models.TextField(default=0,max_length=1000)
    class Meta:
        db_table = 'strategy_manager'
        managed=False
        verbose_name_plural = "StrategyManager"
    def __str__(self):
        return self.strategyName 


class ClientStrategyManager(models.Model):
        
    strategyID = models.ForeignKey(
        "StrategyManager", 
        on_delete=models.CASCADE,
   
        
    )
    
    clientID = models.ForeignKey(
        'Client_Model', 
         
        on_delete=models.CASCADE,
        unique=True
    )
    
    algoID = models.BigIntegerField(null=True, blank=True, editable=False)  
    class Meta:
        db_table = 'client_strategy_manager' 
        #managed=False
        verbose_name_plural = "ClientStrategyManager" 
    def save(self, *args, **kwargs):
        # Retrieve the current instance from the database
        try:
            
            self.algoID = self.strategyID.algoID
            self.strategyID= self.strategyID_id
            self.clientID=self.clientID_id
  
        except Exception as e:
            print("Exception ", str(e))
            pass
        super(ClientStrategyManager, self).save(*args, **kwargs)

class ClientStrategyOrderFiller(models.Model):
    id = models.AutoField(primary_key=True) 
    strategyID = models.CharField(max_length=100)
    clientID   = models.CharField(default=0,max_length=10)
    filler   = models.IntegerField(default=0)
    class Meta:
        db_table = 'client_strategy_order_filler'
        managed=False
        verbose_name_plural = "StrategyManagerOrderFiller"
    def __str__(self):
        return self.strategyID+str(self.filler)


class LogFile(models.Model):
    name = models.TextField(max_length=100, default='Log File', editable=False)
    startAdapter = models.BooleanField(default=False)
    stopAdapter =  models.BooleanField(default=False)
    clearAllOrders =  models.BooleanField(default=False)
    def clean(self):
        # Custom validation to prevent both fields from being True
        if self.startAdapter and self.stopAdapter:
            raise ValidationError('Both startAdapter and stopAdapter cannot be True at the same time.')


    @property
    def content(self):
        log_file = os.path.join("/home/admin/nseFOOMS", 'logs/output.log')
        if os.path.exists(log_file):
            with open(log_file, 'r') as file:
                return file.read()
        return "Log file not found."
    

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'logFile'
    
    def save(self, *args, **kwargs):
        # Retrieve the current instance from the database
        try:
            
            if self.startAdapter==True:
                try:
                    bashFile="/home/admin/nseFOOMS/runOMS.sh"
                    os.system(f'nohup bash {bashFile} > nohup.out 2>&1 &')

                    #process = subprocess.run([bashFile,], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    # Output the result
                    #print("Standard Output:", process.stdout)
                    #print("Standard Error:", process.stderr)
                    self.startAdapter=False
                except subprocess.CalledProcessError as e:
                    # Handle errors in case the script fails
                    print(f"An error occurred: {e}")
                    print(f"Error Output: {e.stderr}")
                    pass
            if self.stopAdapter==True:
                try:
                    bashFile="/home/admin/nseFOOMS/stopOMS.sh"
                    process = subprocess.run([bashFile], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    # Output the result
                    print("Standard Output:", process.stdout)
                    print("Standard Error:", process.stderr)
                    self.stopAdapter=False
                except subprocess.CalledProcessError as e:
                    # Handle errors in case the script fails
                    print(f"An error occurred: {e}")
                    print(f"Error Output: {e.stderr}")
                    pass
                pass
            if self.clearAllOrders==True:
                self.clearAllOrders=False
                PendingOrders.objects.all().delete()
                OrderBook.objects.all().delete()
                TradeBook.objects.all().delete()
                NetPositionTable.objects.all().delete()

  
        except Exception as e:
            print("Exception ", str(e))
            pass
        super(LogFile, self).save(*args, **kwargs)

class PriceHistory(models.Model):
    tokenNumber = models.IntegerField()  # Add unique constraint if required
    exchange = models.IntegerField()
    segment = models.IntegerField()
    ltp = models.IntegerField()
    ltq = models.IntegerField()
    ltt = models.IntegerField()
    lut = models.IntegerField()
    pc = models.IntegerField()
    openPrice = models.IntegerField()
    highPrice = models.IntegerField()
    lowPrice = models.IntegerField()
    closePrice = models.IntegerField()
    atp = models.IntegerField()
    atv = models.IntegerField()
    dayhigh = models.IntegerField()
    dayLow = models.IntegerField()
    oi = models.IntegerField()
    volume = models.FloatField()  # DOUBLE PRECISION equivalent
    bidPrice = ArrayField(models.IntegerField(), size=10)
    bidQuantity = ArrayField(models.IntegerField(), size=10)
    bidOrders = ArrayField(models.IntegerField(), size=10)
    askPrice = ArrayField(models.IntegerField(), size=10)
    askQuantity = ArrayField(models.IntegerField(), size=10)
    askOrders = ArrayField(models.IntegerField(), size=10)

    dayHighOI = models.IntegerField()
    dayLowOI = models.IntegerField()
    dprHigh = models.IntegerField()
    dprLow = models.IntegerField()

    class Meta:
        db_table = "priceHistory"  # To match the table name
        

    def __str__(self):
        return f"PriceHistory {self.tokenNumber}"

   
 
        


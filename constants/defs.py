API_KEY = "4b744941ebb5deb95e9aac3d73016757-bde4c4b3bc1cab3c95448a5691ccb0a7"
ACCOUNT_ID = "101-001-29478115-001"
OANDA_URL = "https://api-fxpractice.oanda.com/v3"

AV_API_KEY = "DQ3AX0TYP2H5CX8R"
AV_URL = "https://www.alphavantage.co/query?"
#above is alphavantage api key

SECURE_HEADER = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

SELL = -1
BUY = 1
NONE = 0

MONGO_CONN_STR = "mongodb+srv://dixunxi:Ihave4brothersand1sister!@atlascluster.ug8d2mk.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster"

INVESTING_COM_PAIRS = {
   "EUR_USD":{
      "pair":"EUR_USD",
      "pair_id":1
   },
   "GBP_USD":{
      "pair":"GBP_USD",
      "pair_id":2
   },
   "USD_JPY":{
      "pair":"USD_JPY",
      "pair_id":3
   },
   "USD_CHF":{
      "pair":"USD_CHF",
      "pair_id":4
   },
   "AUD_USD":{
      "pair":"AUD_USD",
      "pair_id":5
   },
   "EUR_GBP":{
      "pair":"EUR_GBP",
      "pair_id":6
   },
   "USD_CAD":{
      "pair":"USD_CAD",
      "pair_id":7
   },
   "NZD_USD":{
      "pair":"NZD_USD",
      "pair_id":8
   },
   "EUR_JPY":{
      "pair":"EUR_JPY",
      "pair_id":9
   },
   "EUR_CHF":{
      "pair":"EUR_CHF",
      "pair_id":10
   },
   "GBP_JPY":{
      "pair":"GBP_JPY",
      "pair_id":11
   },
   "GBP_CHF":{
      "pair":"GBP_CHF",
      "pair_id":12
   },
   "CHF_JPY":{
      "pair":"CHF_JPY",
      "pair_id":13
   },
   "CAD_CHF":{
      "pair":"CAD_CHF",
      "pair_id":14
   },
   "EUR_AUD":{
      "pair":"EUR_AUD",
      "pair_id":15
   },
   "EUR_CAD":{
      "pair":"EUR_CAD",
      "pair_id":16
   },
   "USD_ZAR":{
      "pair":"USD_ZAR",
      "pair_id":17
   },
   "USD_TRY":{
      "pair":"USD_TRY",
      "pair_id":18
   },
   "EUR_NOK":{
      "pair":"EUR_NOK",
      "pair_id":37
   },
   "BTC_NZD":{
      "pair":"BTC_NZD",
      "pair_id":38
   },
   "USD_MXN":{
      "pair":"USD_MXN",
      "pair_id":39
   },
   "USD_PLN":{
      "pair":"USD_PLN",
      "pair_id":40
   },
   "USD_SEK":{
      "pair":"USD_SEK",
      "pair_id":41
   },
   "USD_SGD":{
      "pair":"USD_SGD",
      "pair_id":42
   },
   "USD_DKK":{
      "pair":"USD_DKK",
      "pair_id":43
   },
   "EUR_DKK":{
      "pair":"EUR_DKK",
      "pair_id":44
   },
   "EUR_PLN":{
      "pair":"EUR_PLN",
      "pair_id":46
   },
   "AUD_CAD":{
      "pair":"AUD_CAD",
      "pair_id":47
   },
   "AUD_CHF":{
      "pair":"AUD_CHF",
      "pair_id":48
   },
   "AUD_JPY":{
      "pair":"AUD_JPY",
      "pair_id":49
   },
   "AUD_NZD":{
      "pair":"AUD_NZD",
      "pair_id":50
   },
   "CAD_JPY":{
      "pair":"CAD_JPY",
      "pair_id":51
   },
   "EUR_NZD":{
      "pair":"EUR_NZD",
      "pair_id":52
   },
   "GBP_AUD":{
      "pair":"GBP_AUD",
      "pair_id":53
   },
   "GBP_CAD":{
      "pair":"GBP_CAD",
      "pair_id":54
   },
   "GBP_NZD":{
      "pair":"GBP_NZD",
      "pair_id":55
   },
   "NZD_CAD":{
      "pair":"NZD_CAD",
      "pair_id":56
   },
   "NZD_CHF":{
      "pair":"NZD_CHF",
      "pair_id":57
   },
   "NZD_JPY":{
      "pair":"NZD_JPY",
      "pair_id":58
   },
   "USD_NOK":{
      "pair":"USD_NOK",
      "pair_id":59
   }
}

TFS = {
   "M5": 300,
   "M15": 900,
   "H1": 3600,
   "D": 86400
}

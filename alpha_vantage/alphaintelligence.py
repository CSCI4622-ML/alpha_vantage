from .alphavantage import AlphaVantage as av


class AlphaIntelligence(av):

    """This class implements all the api calls to alphaIntelligence
    """
    @av._output_format
    @av._call_api_on_func
    def get_news(self, symbol, **kwargs):
        """ Return intraday time series in two json objects as data and
        meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            interval:  time interval between two conscutive values,
                supported values are '1min', '5min', '15min', '30min', '60min'
                (default '15min')
            outputsize:  The size of the call, supported values are
                'compact' and 'full; the first returns the last 100 points in the
                data series, and 'full' returns the full-length intraday times
                series, commonly above 1MB (default 'compact')
        """
        _FUNCTION_KEY = f"NEWS_SENTIMENT&tickers={symbol}"
        for key, value in kwargs.items():
            _FUNCTION_KEY += f"&{key}={value}"
        return _FUNCTION_KEY, "feed", 'sentiment_score_definition'
#!/usr/bin/python
# -**- coding:utf8 -**-
import ccxt
import time
import click
import requests

sybmbol = 'BTC/JPY'
class Ticker():
    def __init__(self):
        self.ex_list = [ccxt.liquid(), "bitfyler" , ccxt.coincheck(), ccxt.bitbank(),ccxt.btcbox(),"GMO"]
        self.ex_name_list = ["liquid","bitfyler","coincheck", "bitbank","btcbox" ,"GMO"]

    def ticker(self):
        self.result_list = []
        click.clear()
        #  bitpoint  todo
        for exchange in self.ex_list:
            if type(exchange) is str and exchange == 'bitfyler':
                bitfyler = requests.get("https://api.bitflyer.jp/v1/ticker?coin=btc").json()
                bitfyler["bid"] = bitfyler["best_bid"]
                bitfyler["ask"] = bitfyler["best_ask"]
                self.result_list.append(bitfyler)
            elif type(exchange) is str and exchange == 'GMO':
                 r = requests.get("https://api.coin.z.com/public/v1/ticker?symbol=BTC").json()
                 self.result_list.append(r["data"][0])
            elif (exchange.has['fetchTicker']):
                r = exchange.fetch_ticker(sybmbol)
                self.result_list.append(r)
        max = 0
        min = 10000000000
        for r in self.result_list:
            bid = int(r["bid"])
            ask = int(r["ask"])
            if bid < min:
                min = bid
            if ask > max:
                max = ask

        click.echo(click.style("%-7s%5s%12s%10s%10s" % ("取引所名","買値","売値","スプレッド","24時間の取引高"), fg='white'),nl=True)
        for  index,r in enumerate(self.result_list):
            bid = int(r["bid"])
            ask = int(r["ask"])
            baseVolume = 0
            if 'baseVolume' in r.keys():
                baseVolume = int(r["baseVolume"])
            else:
                baseVolume = int(float(r["volume"]))
            # click.echo(click.style("%-10s%13s%10s%10s%15s" % (ex_name_list[index], str(ask) ,str(bid), str(ask - bid), str(baseVolume)), fg='white'),nl=False)
            click.echo(click.style("%-10s" % self.ex_name_list[index], fg='white'),nl=False)
            click.echo(click.style("%10s" % str(bid), fg='red', bold= (min == bid)),nl=False)
            click.echo(click.style("%13s" % str(ask), fg='green', bold= (max == ask) ),nl=False)
            click.echo(click.style("%10s" % str(ask - bid), fg='white'),nl=False)
            click.echo(click.style("%15s" % str(baseVolume), fg='white'),nl=True)
        click.echo(click.style("価格差:%s" % str(max - min),fg='white'),nl=True)


if __name__ == "__main__":

    t = Ticker()
    while True:
        try:
            t.ticker()
            time.sleep(2)
        except Exception as e:
            print(e)



    
    

    # gmo api https://api.coin.z.com/docs/#status
    # bitflyer https://api.bitflyer.jp//v1/ticker?coin=btc
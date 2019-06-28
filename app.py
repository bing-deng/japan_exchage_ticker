#!/usr/bin/python
# -**- coding:utf8 -**-
import ccxt
import time
import click

sybmbol = 'BTC/JPY'
class Ticker():
    def __init__(self):
        pass

    def ticker(self):
        click.clear()
        # bitFlyer bitpoint gmo 
        ex_list = [ccxt.coincheck(), ccxt.bitbank(),ccxt.btcbox(),ccxt.liquid()]
        ex_name_list = ["coincheck", "bitbank","btcbox" ,"liquid"]
        result_list =  []
        max = 0
        min = 10000000000
        for exchange in ex_list:
            if (exchange.has['fetchTicker']):
                r = exchange.fetch_ticker(sybmbol)
                result_list.append(r)
                bid = int(r["bid"])
                ask = int(r["ask"])
                if bid < min:
                    min = bid
                if ask > max:
                    max = ask
                    
        click.echo(click.style("%-7s%-9s%8s%10s%10s" % ("取引所名","買値","売値","スプレッド","24時間の取引高"), fg='white'),nl=True)
        
        for  index,r in enumerate(result_list):
            bid = int(r["bid"])
            ask = int(r["ask"])
            baseVolume = int(r["baseVolume"])
            # print(result)
            # print(bid, ask, ask - bid, baseVolume)
            # click.echo(click.style("%-10s%13s%10s%10s%15s" % (ex_name_list[index], str(ask) ,str(bid), str(ask - bid), str(baseVolume)), fg='white'),nl=False)
            click.echo(click.style("%-10s" % ex_name_list[index], fg='white'),nl=False)
           
            bid_bold = False
            if min == bid:
                bid_bold = True
            click.echo(click.style("%10s" % str(bid), fg='red', bold=bid_bold),nl=False)

            ask_bold = False
            if max == ask:
                ask_bold = True
            click.echo(click.style("%13s" % str(ask), fg='green', bold=ask_bold),nl=False)

            click.echo(click.style("%10s" % str(ask - bid), fg='white'),nl=False)
            click.echo(click.style("%15s" % str(baseVolume), fg='white'),nl=True)


if __name__ == "__main__":

    t = Ticker()
    while True:
        try:
                
            t.ticker()
            time.sleep(2)
        except Exception as e:
            print(e)



    
    
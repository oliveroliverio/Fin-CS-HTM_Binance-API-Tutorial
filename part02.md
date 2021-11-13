# Find some data
Use binance websockets.
- websockets are a way to stream market data in real time
- use command line tool like `wscat` 
- use JS to connect to websockets from webUI
- use python websocket client and respond to `websocket message strings`

## Binance API docs
[source](https://github.com/binance/binance-spot-api-docs)
[updated source](https://github.com/binance/binance-spot-api-docs/blob/26f40b60cddd3959daf29a7187ae82544dba944c/user-data-stream.md)

websockets: stream data in real time

current base endpoint: https://api.binance.com
websocket endpoint: wss://stream.binance.com:9443

### install wscat to view and subscribe to streams

```
npm install -g wscat
```

Connect to WSS server and append a particular stream
```
wscat -c wss://stream.binance.com:9443/ws/btcusdt@trade
```

output
```
< {"e":"trade","E":1636767569867,"s":"BTCUSDT","t":1143075105,"p":"64037.68000000","q":"0.00015000","b":8247713983,"a":8247713875,"T":1636767569866,"m":false,"M":true}
< {"e":"trade","E":1636767569872,"s":"BTCUSDT","t":1143075106,"p":"64037.68000000","q":"0.02203000","b":8247713985,"a":8247713875,"T":1636767569871,"m":false,"M":true}
```

In a websocket, you send it a message or subscription, and you get messages back from websockets in JSON format.

The "T" is unix time stamp.  Copy and paste into unixtimestamp.com
output:
```
Format	Milliseconds (1/1,000 second)
GMT	Sat Nov 13 2021 01:39:29 GMT+0000
Your Time Zone	Fri Nov 12 2021 17:39:29 GMT-0800 (Pacific Standard Time)
Relative	3 minutes ago
```
As a day trader, you're interested in 15min or hourly time frame.
Work with 5min time frame, see what it looks like

```
wscat -c wss://stream.binance.com:9443/ws/btcusdt@kline_5m
```

output: note, you won't see changes until 5min passes.  Also, prettify the json output.
```json
{
    "e": "kline",
    "E": 1636768019080,
    "s": "BTCUSDT",
    "k": {
        "t": 1636767900000,
        "T": 1636768199999,
        "s": "BTCUSDT",
        "i": "5m",
        "f": 1143078037,
        "L": 1143079057,
        "o": "64071.43000000",
        "c": "64059.67000000",
        "h": "64074.04000000",
        "l": "64011.31000000",
        "v": "21.52727000",
        "n": 1021,
        "x": false,
        "q": "1378579.12414530",
        "V": "11.27148000",
        "Q": "721833.95791820",
        "B": "0"
    }
}
```
Note, you can now see OHLC data

Instead of opening this in console, you want to save to a file for analysis later
Note: `tee` param prints to console but also saves to file.
```
wscat -c wss://stream.binance.com:9443/ws/btcusdt@kline_1m | tee dataset.txt
```
Be sure to `ctrl c` to quit once you've obtained enough data

Now how to connect to websocket from favorite programming language?  He uses JS

## Connecting to websockets via JS

create `index.html`

[JS has a websocket extension](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications)

example:
```
var exampleSocket = new WebSocket("wss://www.example.com/socketserver", "protocolOne");
```

Add the above to script tag in `index.html`

```html
<body>
  hello
  <script>
    var exampleSocket = new WebSocket("wss://stream.binance.com:9443/ws/btcusdt@trade");
    console.log(exampleSocket)
  </script>
</body>
```

So far this does nothing, need to add an onmessage function

```html
  <script>
    var binanceSocket = new WebSocket("wss://stream.binance.com:9443/ws/btcusdt@trade");

    binanceSocket.onmessage = function(event) {
      console.log(event.data)
    }
  </script>
```

now running this shows info in console window

Next go from console to `<div>`

```html
<body>
  <h2>Trades</h2>
  <div id="trades"></div>

  <script>
    var binanceSocket = new WebSocket("wss://stream.binance.com:9443/ws/btcusdt@trade");
    var tradeDiv = document.getElementById("trades")

    binanceSocket.onmessage = function(event) {
      console.log(event.data)

      var messageObject = JSON.parse(event.data)
      tradeDiv.append(messageObject.p)
    }
  </script>
</body>
```
# Lightweight charts library.

Recall in part 2 we just connected to websockets to stream incoming real time data.  but now want to parse that data into chart that updates in real time.

## Resources
- [tradingview - lightweight charts](https://www.tradingview.com/lightweight-charts/)
- [github - lightweight charts](https://github.com/tradingview/lightweight-charts)

## Installation
Install as a node package
```
npm install lightweight-charts
```

or install as CDN (include URL straight up).  Do this by adding src as script tag in header

```html
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Coinview</title>
  <script src='https://unpkg.com/lightweight-charts/dist/lightweight-charts.standalone.production.js'></script>
</head>
```

they provide an example of how to initialize the chart.
Copy and paste the following into chart.js

```js
const chart = LightweightCharts.createChart(document.body, { width: 400, height: 300 });
const lineSeries = chart.addLineSeries();
lineSeries.setData([
    { time: '2019-04-11', value: 80.01 },
    { time: '2019-04-12', value: 96.63 },
    { time: '2019-04-13', value: 76.64 },
    { time: '2019-04-14', value: 81.89 },
    { time: '2019-04-15', value: 74.43 },
    { time: '2019-04-16', value: 80.01 },
    { time: '2019-04-17', value: 96.63 },
    { time: '2019-04-18', value: 76.64 },
    { time: '2019-04-19', value: 81.89 },
    { time: '2019-04-20', value: 74.43 },
]);
```
note, when you do this the `document.body` part erases everything in index.html.  So make a div just for the chart

```html
<body>
  <h2>Trades</h2>
  <div id="chart"></div>
  <div id="trades"></div>
```

change `document.body` to `document.getElementById("chart")`
Now preview HTML to see if it renders correctly.  You can
Works, now change to candles instead of line
Click on [candlestick chart](https://jsfiddle.net/TradingView/eaod9Lq8/) for how to do this

structure looks like this
```js
var chart = LightweightCharts.createChart(document.body, {
	width: 600,
  height: 300,
	layout: {
		backgroundColor: '#000000',
		textColor: 'rgba(255, 255, 255, 0.9)',
	},
	grid: {
		vertLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
		horzLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
	},
	crosshair: {
		mode: LightweightCharts.CrosshairMode.Normal,
	},
	rightPriceScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	},
	timeScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	},
});

var candleSeries = chart.addCandlestickSeries({
  upColor: 'rgba(255, 144, 0, 1)',
  downColor: '#000',
  borderDownColor: 'rgba(255, 144, 0, 1)',
  borderUpColor: 'rgba(255, 144, 0, 1)',
  wickDownColor: 'rgba(255, 144, 0, 1)',
  wickUpColor: 'rgba(255, 144, 0, 1)',
});

candleSeries.setData([
	{ time: '2018-10-19', open: 180.34, high: 180.99, low: 178.57, close: 179.85 },
	{ time: '2018-10-22', open: 180.82, high: 181.40, low: 177.56, close: 178.75 },
	{ time: '2018-10-23', open: 175.77, high: 179.49, low: 175.44, close: 178.53 },
	{ time: '2018-10-24', open: 178.58, high: 182.37, low: 176.31, close: 176.97 },
	{ time: '2018-10-25', open: 177.52, high: 180.50, low: 176.83, close: 179.07 },
	{ time: '2018-10-26', open: 176.88, high: 177.34, low: 170.91, close: 172.23 },
	{ time: '2018-10-29', open: 173.74, high: 175.99, low: 170.95, close: 173.20 },
	{ time: '2018-10-30', open: 173.16, high: 176.43, low: 172.64, close: 176.24 },
	{ time: '2018-10-31', open: 177.98, high: 178.85, low: 175.59, close: 175.88 },
	{ time: '2018-11-01', open: 176.84, high: 180.86, low: 175.90, close: 180.46 },
	{ time: '2018-11-02', open: 182.47, high: 183.01, low: 177.39, close: 179.93 },
	{ time: '2018-11-05', open: 181.02, high: 182.41, low: 179.30, close: 182.19 },
	{ time: '2018-11-06', open: 181.93, high: 182.65, low: 180.05, close: 182.01 },
	{ time: '2018-11-07', open: 183.79, high: 187.68, low: 182.06, close: 187.23 },
	{ time: '2018-11-08', open: 187.13, high: 188.69, low: 185.72, close: 188.00 },
	{ time: '2018-11-09', open: 188.32, high: 188.48, low: 184.96, close: 185.99 },
```
you know what, just copy this whole example and replace chart.js.
Make sure to modify the `document.getElementsById('chart')`
Preview this in browser. Works.  make sure it's `getElementById` NOT `getElementsById`

## Adding user input (RSI indicator)
modify index.html
```html
<body>
  <h2>Trades</h2>
  <div id="chart"></div>
  <div id="trades"></div>
  <h3>Settings</h3>
  <div id="settings">
    <label>RSI</label>
    <div>
      <input type="text">
    </div>
  </div>
```

Go to tradingview to see how they do it.  They have an RSI oscillator below candlestick chart.  Goal is to do this now.
Be interested in the settings you can configure: "Length" and "source" (open, high, low, or close).  Add this to index.HTML

```html
<input type="text" id="rsi_strength" name="rsi_length" />
```
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
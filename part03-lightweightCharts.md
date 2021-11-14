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
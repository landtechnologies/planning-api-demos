# Land Insight Planning API demo(s)
Remember, to use the [Land Insight Planning API](http://www.landinsight.io/api) you will need to request an API key.   


If you just want some examples of how to make calls to the API in a specific programming language, check out the [Code Example Tool](http://docs.landinsight.apiary.io/#reference/planning-applications/list/get?console=1) in the apiary docs.  


Below we describe and explain how to setup the various demos in the repository.


## Pins on a Google Map in the browser

Anyone with web-development experience should find it fairly easy to plot planning data with Google Maps.  You don't even need to run a localhost server!   

The full code for this demo is in `googlemaps.html`; here we give a slightly simplified version.   

```
![screenshot of demo](googlemaps_screenshot.png)
```

We start with the [Add a Marker demo](https://developers.google.com/maps/documentation/javascript/adding-a-google-map) provided by Google, and then add in a little extra code for querying the Land Insight API.  Before going further, you will need to follow the instructions in that demo to get yourself an API key for the Google Maps service (this is obviously unrelated to your Land Insight API key).   

Right, now you have a Google API Key, ceate a blank `.html` file and copy in the code from the Google demo, setting your Google API key (as inidicated by the Google sample).  Then open the file in your browser and check it works - including panning/zooming of the map.

Next, simply replace the `initMap` function with the following:

```javascript
function initMap() {
  let theMap = new google.maps.Map(document.getElementById('map'), {
    zoom: 16,
    center: {lat: 51.5912874, lng: 0.1080217},
  });
  fetch('https://api.landinsight.io/v_beta/planning/planning-applications?radius=100&limit=15&location=1080217%2C51.5912874/',
        {headers: {'X-Api-Key': 'YOUR_LAND_INSIGHT_API_KEY_HERE'}})
  .then(resp => resp.json())
  .then(json => {
      let locations = json.map(x => ({
          lat: x.location.coordinates[1],
          lng: x.location.coordinates[0]
      }));
      locations.map(x => new google.maps.Marker({
        position: x,
        map: theMap
      }));
  });
}
```

Note that the above is written using nice modern JavaScript features (ES6), so it may not work in older browsers.

That's it!



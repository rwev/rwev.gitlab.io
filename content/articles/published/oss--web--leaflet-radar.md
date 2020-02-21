Title: The 4th Dimension: Animated Weather Radar for Leaflet
Category: oss/web
Tags: contribution,javascript
Status: published

The real-time interplay of terrain and weather is a force to be reckoned with while undertaking all sorts of outdoor activities in a wide variety of environments, whether far out at sea or high in mountains inland. Weather is a critical dimension in the understanding of one's surroundings, and a dimension that traditional maps fail to provide.

Furthermore, weather is infamously dynamic and unpredictable, rendering static projections in the form of frozen images or reductive quantifications insufficient.

But an animated radar embraces and displays this dynamism, allowing the viewer to form their own outlook from a higher-order visual information set that provides data along both space and time. If a picture is worth a thousand words, a video (animation) is worth orders of magnitudes more.

This is why I wrote a Leaflet plugin that adds animated satellite radar onto the map.

When activated, the last hour of radar images are fetched from a open and public data [source](https://mesonet.agron.iastate.edu) for the visible map area, and overlayed onto the map independently in a repeating loop. Playback can be paused and the displayed radar snapshot manually controlled with the slider.

<div style="height: 500px" id="radar-map"></div>

Code on [gitlab](https://gitlab.com/rwev/leaflet-radar).

I've contributed this custom control to main leaflet repository, and you can find it on the [leaflet plugins](https://www.leafletjs.com/plugins.html) page.

<script>

async function makeMaps() {

        loadStylesheet("/assets/javascript/dependencies/leaflet.css");
        loadStylesheet("/assets/javascript/dependencies/leaflet-radar.css");

        await loadScriptPromise("/assets/javascript/dependencies/leaflet.js");
        await loadScriptPromise("/assets/javascript/dependencies/leaflet-radar.js");

        const VIEW = [43.37, -116.12];
        const ZOOM = 6;

        let radarMap = L.map("radar-map").setView(VIEW, ZOOM);

        const osmBaseLayerF = () => L.tileLayer("https://tile-{s}.openstreetmap.fr/hot/{z}/{x}/{y}.png", {});

        osmBaseLayerF().addTo(radarMap);

        let radar = L.control.radar({});
        radar.addTo(map);
        radar.checkbox.checked = true;
        radar.toggle();
}
makeMaps();


</script>



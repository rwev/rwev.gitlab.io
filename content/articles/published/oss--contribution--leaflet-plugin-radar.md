Title: Leaflet Plugin: Radar
Category: oss/contribution
Tags: leaflet,javascript,mapping
Status: published

Weather is a critical dimension in the understanding one's immediate surroundings, especially on a real-time basis. Understanding the interplay of terrain and weather is crucial in all sorts of navigation. 

This plugin adds animated satellite radar onto the map. When activated, the last hour of radar images are fetched from a open and public data [source](https://mesonet.agron.iastate.edu) and overlayed loop onto the map in a repeating loop. 

<div style="height: 500px" id="radar-map"></div>

[github](https://github.com/rwev/leaflet-radar)

I've contributed this custom control to main leaflet repository, and you can find it on the [leaflet plugins](https://www.leafletjs.com/plugins.html) page.

<script>

async function makeMaps() {

        loadStylesheet("/assets/deps/leaflet.css");
        loadStylesheet("/assets/deps/leaflet-radar.css");

        await loadScriptPromise("/assets/deps/leaflet.js");
        await loadScriptPromise("/assets/deps/leaflet-radar.js");

        const VIEW = [43.37, -116.12];
        const ZOOM = 6;

        let radarMap = L.map("radar-map").setView(VIEW, ZOOM);
        
        const osmBaseLayerF = () => L.tileLayer("https://tile-{s}.openstreetmap.fr/hot/{z}/{x}/{y}.png", {});

        osmBaseLayerF().addTo(radarMap);
        
        L.control.radar({}).addTo(radarMap);
        
}
 makeMaps();


</script>



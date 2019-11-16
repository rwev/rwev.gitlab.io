Title: Leaflet Plugin: View Meta
Category: oss/contribution
Tags: leaflet,javascript,mapping
Status: published

Sharing a "location" is typically done by transmitting a single waypoint. This method tells the consumer of the information where to _center_ their focus  but doesn't convey any information regarding how that focus should be _bounded_.  What if one wants to share a _general area_ that they are looking at on their mapping application?

This plugin displays and persists meta-data about the map's view box (center and boundary coordinates) to the URL, which can be shared to precisely reconstruct the map view. 

<div style="height: 500px" id="view-meta-map"></div>

[github](https://github.com/rwev/leaflet-view-meta)

I've contributed this custom control to main leaflet repository, and you can find it on the [leaflet plugins](https://www.leafletjs.com/plugins.html) page.

<script>

async function makeMaps() {

        loadStylesheet("/assets/deps/leaflet.css");
        loadStylesheet("/assets/deps/leaflet-view-meta.css");

        await loadScriptPromise("/assets/deps/leaflet.js");
        await loadScriptPromise("/assets/deps/leaflet-view-meta.js");

        const VIEW = [43.37, -116.12];
        const ZOOM = 6;

        let viewMetaMap = L.map("view-meta-map").setView(VIEW, ZOOM);
        
        const osmBaseLayerF = () => L.tileLayer("https://tile-{s}.openstreetmap.fr/hot/{z}/{x}/{y}.png", {});

        osmBaseLayerF().addTo(viewMetaMap);
        
        L.control.viewMeta({}).addTo(viewMetaMap);
        
}
 makeMaps();


</script>



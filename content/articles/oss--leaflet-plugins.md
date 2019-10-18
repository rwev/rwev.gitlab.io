Title: Leaflet Plugin Contributions
Category: oss/leaflet
Tags: maps,projects,git,javascript

Maps are cool. It's easy to find myself in a daydream of sorts, gathering ideas for the next off-road motorcycle trip, scouting areas to hunt, or the next fishing expedition. The power of maps in increasing both awareness and depth of knowledge of surrounding geographical features is hard to beat. 

After playing around with [leaflet](https://www.leafletjs.com), the de facto open-source standard for interactive mapping in the browser, I decided to experimentally extend its functionality with a handful of plugins. 

I've contributed each of these custom control to main leaflet repository, and you can find them on the [leaflet plugins](https://www.leafletjs.com/plugins.html) page.

<!--
<script>

async function makeMaps() {

        loadStylesheet("/assets/deps/leaflet.css");
        loadStylesheet("/assets/deps/leaflet-radar.css");
        loadStylesheet("/assets/deps/leaflet-reticle.css");
        loadStylesheet("/assets/deps/leaflet-view-meta.css");

        await loadScriptPromise("/assets/deps/leaflet.js");
        await loadScriptPromise("/assets/deps/leaflet-radar.js");
        await loadScriptPromise("/assets/deps/leaflet-reticle.js");
        await loadScriptPromise("/assets/deps/leaflet-view-meta.js");

        const VIEW = [43.37, -116.12];
        const ZOOM = 6;

        let radarMap = L.map("radar-map").setView(VIEW, ZOOM);
        let reticleMap = L.map("reticle-map").setView(VIEW, ZOOM);
        let viewMetaMap = L.map("view-meta-map").setView(VIEW, ZOOM);
        
        const osmBaseLayerF = () => L.tileLayer("https://tile-{s}.openstreetmap.fr/hot/{z}/{x}/{y}.png", {});

        osmBaseLayerF().addTo(radarMap);
        osmBaseLayerF().addTo(reticleMap);
        osmBaseLayerF().addTo(viewMetaMap);
        
        L.control.radar({}).addTo(radarMap);
        L.control.reticle({mapId: "reticle-map"}).addTo(reticleMap);
        L.control.viewMeta({}).addTo(viewMetaMap);
        
}
makeMaps();

</script>

-->

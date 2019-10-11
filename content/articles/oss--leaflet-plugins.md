Title: Leaflet Plugin Contributions
Category: oss/leaflet
Tags: maps,projects,git,javascript
Status: published
Date: 01/01/01

Maps are cool. It's easy to find myself in a daydream of sorts, gathering ideas for the next off-road motorcycle trip, scouting areas to hunt, or the next fishing expedition. The power of maps in increasing both awareness and depth of knowledge of surrounding geographical features is hard to beat. 

After playing around with [leaflet](https://www.leafletjs.com), the de facto open-source standard for interactive mapping in the browser, I decided to experimentally extend its functionality with a handful of plugins. 

I've contributed each of these custom control to main leaflet repository, and you can find them on the [leaflet plugins](https://www.leafletjs.com/plugins.html) page.

# leaflet-radar 

[link](https://github.com/rwev/leaflet-radar)

Weather is a critical dimension in the understanding one's immediate surroundings, especially on a real-time basis. Understanding the interplay of terrain and weather is crucial in all sorts of navigation. 

This plugin adds animated satellite radar onto the map. When activated, the last hour of radar images are fetched from a open and public data [source](https://mesonet.agron.iastate.edu) and overlayed loop onto the map in a repeating loop. 

<div style="height: 500px" id="radar-map"></div>

# leaflet-reticle

[link](https://github.com/rwev/leaflet-reticle)

Map scales are a feature necessary to relate figures and lines and numbers on a map to usable distances and dimensions that one can physically reason with. 

Most maps, when on paper or within interactive interactions, put the map scale in the corner of the map. This leads to a few interrelated usability issues.

First, scales are (or should be) calculated based on a projection over the area in which the scale is placed. Second, scales are usually only given along one axis, normally longitude.  Problem is, the scale isn't the same everywhere on the two-dimensional map, due to the fact that the earth is a lumpy three-dimensional sphere. The result is incorrect estimation of distances within the map area, especially in the case of high level / low zoom, or when using the scale to make projections in the dimension normal / perpendicular to the dimension along which the scale is given.

Lastly, the user of a map, particularly interactive ones where the user can set the view box, are focused on the center of the map. Putting the scale along one of the edges forces the user to make a very crude eye-balled estimation, or maybe even with the assistance of another physical object such as a pen or finger. Once again, lots of room for error here. 

This plugin solves each of these issues: the distance projection is done _at map center_ for more accurate distance, scales are generated _independently_ along each axis, and the scales themselves are placed in center of map, (likely) closer to the _point of focus_.

<div class="quote">
        <p class="annotation">
                Reticle:
        </p>
        <p class="content">
                A grid or pattern placed in the eyepiece of an optical instrument, used to establish scale or position.
        </p>
</div>

<div style="height: 500px" id="reticle-map"></div>

# leaflet-view-meta

[link](https://github.com/rwev/leaflet-view-meta)

Sharing a "location" is typically done by transmitting a single waypoint. This method tells the consumer of the information where to _center_ their focus  but doesn't convey any information regarding how that focus should be _bounded_.  What if one wants to share a _general area_ that they are looking at on their mapping application?

This plugin displays and persists meta-data about the map's view box (center and boundary coordinates) to the URL, which can be shared to precisely reconstruct the map view. 

<div style="height: 500px" id="view-meta-map"></div>

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



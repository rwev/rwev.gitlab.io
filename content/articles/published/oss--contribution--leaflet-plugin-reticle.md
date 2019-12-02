Title: Leaflet Plugin: Reticle
Category: oss/web
Tags: contribution,javascript
Status: published

Map scales are a feature necessary to relate figures and lines and numbers on a map to usable distances and dimensions that one can physically reason with. 

Most maps, when on paper or within interactive interactions, put the map scale in the corner of the map. This leads to a few interrelated usability issues.

First, scales are (or should be) calculated based on a projection over the area in which the scale is placed. Second, scales are usually only given along one axis, normally longitude.  Problem is, the scale isn't the same everywhere on the two-dimensional map, due to the fact that the earth is a lumpy three-dimensional sphere. The result is incorrect estimation of distances within the map area, especially in the case of high level / low zoom, or when using the scale to make projections in the dimension normal / perpendicular to the dimension along which the scale is given.

Lastly, the user of a map, particularly interactive ones where the user can set the view box, are focused on the center of the map. Putting the scale along one of the edges forces the user to make a very crude eye-balled estimation, or maybe even with the assistance of another physical object such as a pen or finger. Once again, lots of room for error here. 

This plugin solves each of these issues: the distance projection is done _at map center_ for more accurate distance, scales are generated _independently_ along each axis, and the scales themselves are placed in center of map, (likely) closer to the _point of focus_.

> <strong>Reticle</strong>: A grid or pattern placed in the eyepiece of an optical instrument, used to establish scale or position.

<div style="height: 500px" id="reticle-map"></div>

[github](https://github.com/rwev/leaflet-reticle)

I've contributed this custom control to main leaflet repository, and you can find it on the [leaflet plugins](https://www.leafletjs.com/plugins.html) page.

<script>

async function makeMaps() {

        loadStylesheet("/assets/javascript/dependencies/leaflet.css");
        loadStylesheet("/assets/javascript/dependencies/leaflet-reticle.css");

        await loadScriptPromise("/assets/javascript/dependencies/leaflet.js");
        await loadScriptPromise("/assets/javascript/dependencies/leaflet-reticle.js");

        const VIEW = [43.37, -116.12];
        const ZOOM = 6;

        let reticleMap = L.map("reticle-map").setView(VIEW, ZOOM);
        
        const osmBaseLayerF = () => L.tileLayer("https://tile-{s}.openstreetmap.fr/hot/{z}/{x}/{y}.png", {});

        osmBaseLayerF().addTo(reticleMap);
        
        L.control.reticle({mapId: "reticle-map"}).addTo(reticleMap);
        
}
 makeMaps();


</script>



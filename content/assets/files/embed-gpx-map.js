function embedGpxMap(divId, gpxFile, loadScripts = false) {
        function make() {
                var map = L.map(divId).setView([43.37, -116.12], 13);

                var osmAttribution =
                        'Map data &copy; <a href="https://openstreetmap.org">OpenStreetMap</a> contributors';
                var leafletGpxAttribution =
                        '<a href="https://github.com/mpetazzoni/leaflet-gpx">GPX</a>';

                L.tileLayer(
                        "https://tile-{s}.openstreetmap.fr/hot/{z}/{x}/{y}.png",
                        {
                                attribution: [
                                        osmAttribution,
                                        leafletGpxAttribution
                                ].join(" | ")
                        }
                ).addTo(map);

                new L.GPX(gpxFile, {
                        async: true,
                        marker_options: {
                                startIconUrl:
                                        "https://raw.githubusercontent.com/mpetazzoni/leaflet-gpx/master/pin-icon-start.png",
                                endIconUrl:
                                        "https://raw.githubusercontent.com/mpetazzoni/leaflet-gpx/master/pin-icon-end.png",
                                shadowUrl:
                                        "https://raw.githubusercontent.com/mpetazzoni/leaflet-gpx/master/pin-shadow.png",
                                wptIconUrls: {
                                        "":
                                                "https://raw.githubusercontent.com/mpetazzoni/leaflet-gpx/master/pin-icon-wpt.png"
                                }
                        }
                })
                        .on("loaded", function(e) {
                                map.fitBounds(e.target.getBounds());
                        })
                        .addTo(map);
        }

        loadStylesheet("https://unpkg.com/leaflet@1.5.1/dist/leaflet.css");
        loadScript("https://unpkg.com/leaflet@1.5.1/dist/leaflet.js", () =>
                loadScript(
                        "https://cdnjs.cloudflare.com/ajax/libs/leaflet-gpx/1.4.0/gpx.min.js",
                        () => make()
                )
        );
}

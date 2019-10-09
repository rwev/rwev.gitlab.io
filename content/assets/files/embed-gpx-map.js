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

        loadStylesheet("assets/files/deps/leaflet.css");
        loadScript("assets/files/deps/leaflet.js", () =>
                loadScript(
                        "assets/files/leaflet-gpx.js",
                        () => make()
                )
        );
}

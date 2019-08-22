function embedGpxMap(divId, gpxFile) {

        function make() {

                var map = L.map(divId).setView([43.37, -116.12], 13);

                L.tileLayer(
                        "https://tile-{s}.openstreetmap.fr/hot/{z}/{x}/{y}.png"
                ).addTo(map);

                var gpx = "assets/files/" + gpxFile;

                new L.GPX(gpx, {
                        async: true,
                        marker_options: {
                                startIconUrl:
                                        "assets/dependencies/leaflet-gpx/pin-icon-start.png",
                                endIconUrl:
                                        "assets/dependencies/leaflet-gpx/pin-icon-end.png",
                                shadowUrl:
                                        "assets/dependencies/leaflet-gpx/pin-shadow.png",
                                wptIconUrls: {
                                        "":
                                                "assets/dependencies/leaflet-gpx/pin-icon-wpt.png"
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

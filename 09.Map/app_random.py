from flask import Flask, render_template
import folium
from folium.plugins import MarkerCluster
import random

app = Flask(__name__)


def generate_random_coordinates(num):
    coordinates = []
    for _ in range(num):
        lat = random.uniform(37.4, 37.7)
        lng = random.uniform(126.8, 127.1)
        coordinates.append([lat, lng])
    return coordinates


def create_map(num_points):
    seoul_center = [37.5665, 126.9780]
    map = folium.Map(location=seoul_center, zoom_start=12)

    # 좌표
    coordinates = generate_random_coordinates(num_points)

    maker_cluster = MarkerCluster().add_to(map)
    for coord in coordinates:
        folium.Marker(location=coord).add_to(maker_cluster)

    return map


@app.route("/map/<int:num_points>")
def map_points(num_points):
    mymap = mymap.create_map(num_points)
    map_html = mymap._repr_html_()
    return render_template("index.html", map_html=map_html)


if __name__ == "__main__":
    app.run(debug=True)

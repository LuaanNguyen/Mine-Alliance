"use client";

import { useEffect } from "react";
import L from "leaflet";
import { MapContainer, Marker, TileLayer, Popup, useMap } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import "leaflet-defaulticon-compatibility";
import "leaflet-defaulticon-compatibility/dist/leaflet-defaulticon-compatibility.css";
import { useGeneral } from "@/context/generalContext";

function ChangeMapView({ coords }: { coords: [number, number] }) {
  const map = useMap();
  useEffect(() => {
    map.setView(coords, 7);
  }, [coords, map]);
  return null;
}

export default function Map() {
  const { mineData, selectedMineID, toggleMineSelection } = useGeneral();

  function parseCoords(coords: string): [number, number] {
    const [lat, lng] = coords.split(",").map((coord) => parseFloat(coord));
    return [lat || 0, lng || 0];
  }

  const selectedMine = mineData.find((mine) => mine.id === selectedMineID);
  const defaultCenter: [number, number] = [34.0489, -111.0937];
  const center: [number, number] = selectedMine
    ? parseCoords(selectedMine.location_coords)
    : defaultCenter;

  return (
    <section className="grid col-span-2 h-[100%]">
      <MapContainer
        center={center}
        zoom={7}
        scrollWheelZoom={true}
        style={{ height: "100%", width: "100%" }}
      >
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url={`https://tiles.stadiamaps.com/tiles/outdoors/{z}/{x}/{y}{r}.png?api_key=${process.env.STADIA_MAPS_API_KEY}`}
        />
        {mineData.map((el) => (
          <Marker
            position={parseCoords(el.location_coords)}
            key={el.id}
            icon={el.id === selectedMineID ? highlightedIcon : defaultIcon}
            eventHandlers={{
              click: () => toggleMineSelection(el.id),
            }}
          >
            <Popup>{el.location}</Popup>
          </Marker>
        ))}
        <ChangeMapView coords={center} />
      </MapContainer>
    </section>
  );
}

const defaultIcon = new L.Icon({
  iconUrl: "https://unpkg.com/leaflet@1.7.1/dist/images/marker-icon.png",
  iconRetinaUrl:
    "https://unpkg.com/leaflet@1.7.1/dist/images/marker-icon-2x.png",
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowUrl: "https://unpkg.com/leaflet@1.7.1/dist/images/marker-shadow.png",
  shadowSize: [41, 41],
});

const highlightedIcon = new L.Icon({
  iconUrl:
    "https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png",
  shadowUrl:
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png",
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41],
});

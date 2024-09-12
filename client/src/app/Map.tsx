"use client";

import { MapContainer, Marker, TileLayer, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import "leaflet-defaulticon-compatibility";
import "leaflet-defaulticon-compatibility/dist/leaflet-defaulticon-compatibility.css";
import { useGeneral } from "@/context/generalContext";

export default function Map() {
  const { mineData } = useGeneral();

  function parseCoords(coords: string): [number, number] {
    const [lat, lng] = coords.split(",").map((coord) => parseFloat(coord));
    return [lat, lng];
  }

  return (
    <section className="grid col-span-2 h-[100%]">
      <MapContainer
        center={[34.0489, -111.0937]}
        zoom={7}
        scrollWheelZoom={false}
      >
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url={`https://tiles.stadiamaps.com/tiles/outdoors/{z}/{x}/{y}{r}.png?api_key=${process.env.STADIA_MAPS_API_KEY}`}
        />
        {mineData.map((el) => (
          <Marker position={parseCoords(el.location_coords)} key={el.id}>
            <Popup>{el.location}</Popup>
          </Marker>
        ))}
      </MapContainer>
    </section>
  );
}

import { MapContainer, Marker, TileLayer, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import "leaflet-defaulticon-compatibility";
import "leaflet-defaulticon-compatibility/dist/leaflet-defaulticon-compatibility.css";

export default function Map(props: any) {
  const { position, zoom } = props;

  return (
    <section className="grid col-span-2 h-[100%]">
      <MapContainer
        center={[34.0489, -111.0937]}
        zoom={7}
        scrollWheelZoom={false}
      >
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://tiles.stadiamaps.com/tiles/outdoors/{z}/{x}/{y}{r}.png"
        />
        <Marker position={[33.0551, -109.0645]}>
          <Popup>Morenci Mine</Popup>
        </Marker>
        <Marker position={[34.4125, -113.1925]}>
          <Popup>Bagdad Mine</Popup>
        </Marker>
        <Marker position={[33.466, -110.7264]}>
          <Popup>Ray Mine</Popup>
        </Marker>
        <Marker position={[31.9686, -110.3128]}>
          <Popup>Mission Complex</Popup>
        </Marker>
        <Marker position={[32.94, -110.8705]}>
          <Popup>Pinto Valley Mine</Popup>
        </Marker>
      </MapContainer>
    </section>
  );
}

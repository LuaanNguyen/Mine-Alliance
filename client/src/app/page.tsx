"use client";

import dynamic from "next/dynamic";

const Map = dynamic(() => import("./Map"), {
  ssr: false,
  loading: () => <MapLoadingSpinner />,
});

import Info from "./my-components/info";

import ChatBox from "./my-components/chatbox";

const MapLoadingSpinner = () => (
  <div className="col-span-2 flex items-center justify-center bg-gray-100">
    <div className="relative w-16 h-16 rounded-full animate-spin border-8 border-dashed border-[#88D66C] border-t-transparent"></div>
  </div>
);

export default function Home() {
  return (
    <>
      <div className="flex">
        <main className="grid grid-cols-4 h-[92vh]">
          <Info />
          <Map />
          <ChatBox />
        </main>
      </div>
    </>
  );
}

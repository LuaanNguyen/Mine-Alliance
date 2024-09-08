"use client";

import Map from "./Map";
import Info from "./my-components/info";

export default function Home() {
  return (
    <>
      <div className="flex">
        <main className="grid grid-cols-4 h-[100vh] overflow-hidden flex-grow">
          <Info />
          <Map />
          <div className="border-l-2 h-[100%]">4</div>
        </main>
      </div>
    </>
  );
}

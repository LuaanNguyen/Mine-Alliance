"use client";

import Map from "./Map";

export default function Home() {
  return (
    <main className="grid grid-cols-4 h-screen">
      <div className="border-r-2 h-[100%]">1</div>
      <Map />
      <div className="border-l-2 h-[100%]">4</div>
    </main>
  );
}

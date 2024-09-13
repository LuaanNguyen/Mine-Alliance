"use client";

import dynamic from "next/dynamic";

const Map = dynamic(() => import("./Map"), {
  ssr: false,
  loading: () => (
    <div className="relative  mx-auto my-auto inset-0 w-12 h-12 rounded-full animate-spin border-8 border-dashed border-[#6B8E23] border-t-transparent"></div>
  ),
});

import Info from "./my-components/info";
import { GeneralProvider } from "@/context/generalContext";
import ChatBox from "./my-components/chatbox";

export default function Home() {
  return (
    <>
      <GeneralProvider>
        <div className="flex">
          <main className="grid grid-cols-4 h-[92vh]">
            <Info />
            <Map />
            <ChatBox mineId="mine123" />
          </main>
        </div>
      </GeneralProvider>
    </>
  );
}

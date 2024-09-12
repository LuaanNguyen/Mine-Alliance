import React from "react";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Button } from "@/components/ui/button";
import { Factory, Navigation } from "lucide-react";
import { useGeneral } from "@/context/generalContext";

export default function Info() {
  return (
    <section className="border-r-2 h-[100%] flex flex-col justify-start">
      <div className="p-5 flex flex-col">
        <Profile />
        <ListOfMines />
      </div>
    </section>
  );
}

function Profile() {
  return (
    <div className="flex flex-col">
      {" "}
      <div className="flex items-center gap-5 my-1">
        <Avatar>
          <AvatarImage src="https://github.com/LuaanNguyen.png" />
          <AvatarFallback>Luan Nguyen</AvatarFallback>
        </Avatar>
        <div className="flex flex-col">
          {" "}
          <h4 className="text-xl">Welcome back! Luan Nguyen</h4>
          <p className="text-gray-400">Edit Profile</p>
        </div>
      </div>
      <div className="flex gap-5 justify-center">
        <Button variant="outline">Submit a issue 📝</Button>
        <Button variant="outline">Vote 🗳️</Button>
      </div>
      <hr className="h-[2px] bg-gray-200 my-4 w-[100%]"></hr>
    </div>
  );
}

function ListOfMines() {
  const { mineData } = useGeneral();

  return (
    <div className="flex flex-col">
      <h1 className="text-xl font-semibold">Nearby Active Mines</h1>
      <input
        type="text"
        placeholder={`Search...`}
        className="p-3 border-2 border-gray-200 rounded-2xl my-2"
      ></input>
      <div className="flex flex-row justify-between p-4">
        <div className="flex-row">
          <h1 className="text-3xl font-semibold">{mineData.length}</h1>
          <h4>Total</h4>
        </div>
        <div className="flex-row">
          <h1 className="text-3xl font-semibold">1</h1>
          <h4>Voted</h4>
        </div>
        <div className="flex-row">
          <h1 className="text-3xl font-semibold">1</h1>
          <h4>Resolved</h4>
        </div>
      </div>
      <section className="flex flex-col gap-2">
        {mineData.map((el) => (
          <div
            className="flex flex-row gap-2 items-center border-2 py-5 px-4 rounded-xl justify-between"
            key={el.id}
          >
            <Factory size={28} color="#fda668" />
            <div>
              {" "}
              <h1 className="text-xl font-semibold">{el.location}</h1>
              <p className="text-gray-400">{el.type_of_mining}</p>
            </div>
            <div>
              <Navigation size={28} color="#000000" />
            </div>
          </div>
        ))}
      </section>
    </div>
  );
}

import React from "react";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";

export default function Info() {
  return (
    <section className="border-r-2 h-[100%] flex flex-row justify-start">
      <div className="p-5 flex flex-row">
        <div className="flex flex-row items-center gap-2">
          {" "}
          <Profile />
          <h4 className="text-2xl font-semibold">Welcome back!</h4>
        </div>
      </div>
    </section>
  );
}

function Profile() {
  return (
    <Avatar>
      <AvatarImage src="https://github.com/LuaanNguyen.png" />
      <AvatarFallback>Luan Nguyen</AvatarFallback>
    </Avatar>
  );
}

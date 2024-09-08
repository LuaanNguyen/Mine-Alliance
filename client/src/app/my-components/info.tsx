import React from "react";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";

export default function Info() {
  return (
    <div className="border-r-2 h-[100%] flex flex-row justify-start">
      {/* <div className="p-5 flex flex-row">
        {" "}
        <Profile />
        <h4>Welcome back, Luan Nguyen</h4>
      </div> */}
    </div>
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

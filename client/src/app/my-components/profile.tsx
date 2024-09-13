import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Button } from "@/components/ui/button";

export default function Profile() {
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
      <hr className="h-[2px] bg-gray-200 my-2 w-[100%]"></hr>
    </div>
  );
}

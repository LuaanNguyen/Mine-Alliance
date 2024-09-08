import {
  House,
  CircleHelp,
  CircleAlert,
  Minus,
  Share2,
  Settings,
} from "lucide-react";

export default function Sidebar() {
  return (
    <aside className="p-4 border-r-4 w-[60px] flex flex-col gap-5">
      {/* Sidebar content goes here */}
      <House color="#fda668" />
      <Minus />
      <CircleHelp />
      <CircleAlert />
      <Share2 />
      <Settings />
    </aside>
  );
}

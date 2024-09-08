"use client";
import React, { useState, useEffect } from "react";
import { Pickaxe } from "lucide-react";
import { Clock, Sun, Thermometer, SunDim, Moon } from "lucide-react";
import { Button } from "@/components/ui/button";
import { useTheme } from "next-themes";
import { Toggle } from "@/components/ui/toggle";

import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuLabel,
  DropdownMenuRadioGroup,
  DropdownMenuRadioItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";

export default function Navigation() {
  const [time, setTime] = useState(getTime());
  const [position, setPosition] = React.useState("Community");
  const { theme, setTheme } = useTheme();
  console.log(theme);

  const toggleTheme = () => {
    setTheme(theme === "light" ? "dark" : "light");
  };

  useEffect(() => {
    const timer = setInterval(() => {
      setTime(getTime());
    }, 1000);

    return () => clearInterval(timer);
  }, []);

  function getTime() {
    const date = new Date();
    return date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds();
  }

  return (
    <nav className="w-[100%] flex justify-between border-b-2">
      <div className="flex gap-2 p-2 items-center">
        <Pickaxe size={44} strokeWidth={1.75} />
        <h1 className="text-2xl font-semibold">Sustainability</h1>
      </div>
      <section className="flex gap-5 p-4 items-center">
        <div className="flex gap-1">
          <Clock />
          {time}
        </div>
        <div className="flex gap-1">
          <Sun />
          Sunny
        </div>
        <div className="flex gap-1">
          <Thermometer />
          130°F
        </div>
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Button variant="outline">Login in as {position}</Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent className="w-56">
            <DropdownMenuLabel>Choose the Users to Login</DropdownMenuLabel>
            <DropdownMenuSeparator />
            <DropdownMenuRadioGroup
              value={position}
              onValueChange={setPosition}
            >
              <DropdownMenuRadioItem value="Community">
                Community
              </DropdownMenuRadioItem>
              <DropdownMenuRadioItem value="Government">
                Government
              </DropdownMenuRadioItem>
              <DropdownMenuRadioItem value="Factory">
                Factory
              </DropdownMenuRadioItem>
            </DropdownMenuRadioGroup>
          </DropdownMenuContent>
        </DropdownMenu>
        <Toggle onClick={toggleTheme}>
          {theme == "light" ? (
            <SunDim strokeWidth={1.75} />
          ) : (
            <Moon strokeWidth={1.75} />
          )}
        </Toggle>
      </section>
    </nav>
  );
}

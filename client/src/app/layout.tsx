import type { Metadata } from "next";
import { ThemeProvider } from "./my-components/theme-provider";
import "./globals.css";
import Navigation from "./my-components/navigation";
import {
  House,
  CircleHelp,
  CircleAlert,
  Minus,
  Share2,
  Settings,
} from "lucide-react";

export const metadata: Metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="flex">
        <ThemeProvider
          attribute="class"
          defaultTheme="system"
          enableSystem
          disableTransitionOnChange
        >
          <Sidebar />
          <div className="w-[100%]">
            <Navigation />
            {children}
          </div>
        </ThemeProvider>
      </body>
    </html>
  );
}

function Sidebar() {
  return (
    <aside className=" p-4 border-r-4 w-[60px] flex flex-col gap-5">
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
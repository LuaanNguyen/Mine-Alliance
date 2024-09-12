import type { Metadata } from "next";
import { ThemeProvider } from "./my-components/theme-provider";
import "./globals.css";
import Navigation from "./my-components/navigation";
import Sidebar from "./my-components/sidebar";

export const metadata: Metadata = {
  title: "Mine Alliance",
  description: "AZ Spark Challenge 2024",
  icons: {
    icon: "/favicon.svg", // Use .svg extension
  },
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

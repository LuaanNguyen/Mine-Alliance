"use client";
import {
  createContext,
  useContext,
  useState,
  ReactNode,
  useEffect,
} from "react";

interface Mine {
  affect_radius: number;
  air_quality: number;
  assessment: string;
  biodiversity: string;
  description: string;
  id: number;
  impact_scale: number | null;
  location: string;
  location_coords: string;
  socioeconomic_index: string;
  soil_quality: number;
  tenure: number;
  type_of_mining: string;
  water_quality: number;
}

interface MineState {
  mines: Mine[];
}

interface GeneralContextType {
  mine: MineState;
  setMine: React.Dispatch<React.SetStateAction<MineState>>;
}

const GeneralContext = createContext<GeneralContextType | undefined>(undefined);

const serverURL = "http://127.0.0.1:5000"; // This is a development URL, change as the VPS

const initialState: MineState = { mines: [] };

interface GeneralProviderProps {
  children: ReactNode;
}

function GeneralProvider({ children }: GeneralProviderProps) {
  const [mine, setMine] = useState<MineState>(initialState);

  useEffect(() => {
    async function fetchData() {
      try {
        const res = await fetch(`${serverURL}/mining_locations`);
        const data = await res.json();
        setMine(data);
      } catch {
        throw new Error("There was an error fetching data.");
      }
    }
    fetchData();
  }, []);

  return (
    <GeneralContext.Provider value={{ mine, setMine }}>
      {children}
    </GeneralContext.Provider>
  );
}

function useGeneral(): GeneralContextType {
  const context = useContext(GeneralContext);
  if (context === undefined) {
    throw new Error("GeneralContext was used outside the GeneralProvider");
  }
  return context;
}

export { GeneralProvider, useGeneral };

import React, { useState } from "react";
import { Factory, ChevronDown, ChevronUp } from "lucide-react";
import { useGeneral } from "@/context/generalContext";

export default function Info() {
  return (
    <section className="border-r-2 h-[100%] flex flex-col justify-start overflow-y-auto">
      <div className="p-5 flex flex-col overflow-scroll">
        {/* <Profile /> */}
        <ListOfMines />
      </div>
    </section>
  );
}

function ListOfMines() {
  const { mineData, selectedMineID, toggleMineSelection, numFeedback } =
    useGeneral();
  const [searchTerm, setSearchTerm] = useState("");

  const filteredMines = mineData.filter(
    (mine) =>
      mine.location.toLowerCase().includes(searchTerm.toLowerCase()) ||
      mine.type_of_mining.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="flex flex-col">
      <h1 className="text-xl font-semibold my-1">Nearby Active Mines</h1>
      <input
        type="text"
        placeholder={`Search...`}
        className="p-3 border-2 border-gray-200 bg-white rounded-2xl"
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />
      <div className="flex flex-row justify-between p-4">
        <div className="flex-row">
          <h1 className="text-3xl font-semibold">{filteredMines.length}</h1>
          <h4>Total</h4>
        </div>
        <div className="flex-row">
          <h1 className="text-3xl font-semibold text-center">{numFeedback}</h1>
          <h4>Issue Submitted</h4>
        </div>
        <div className="flex-row">
          <h1 className="text-3xl font-semibold">1</h1>
          <h4>Resolved</h4>
        </div>
      </div>
      <section className="flex flex-col gap-2 flex-1">
        {filteredMines.length > 0 ? (
          filteredMines.map((el) => (
            <div
              key={el.id}
              className={`flex flex-col border-2 rounded-xl transition-all duration-300 ease-in-out cursor-pointer
                        ${
                          selectedMineID === el.id
                            ? "ring-2 ring-[#87CEEB] shadow-lg"
                            : ""
                        }`}
              onClick={() => toggleMineSelection(el.id)}
            >
              <div className="flex flex-row items-center py-5 px-3 justify-between gap-4">
                <p className="text-gray-400">{el.id}</p>
                <Factory size={28} color="#fda668" />
                <div className="grow text-center">
                  <h1 className="text-lg font-semibold">{el.location}</h1>
                  <p className="text-gray-400">{el.type_of_mining}</p>
                </div>

                {selectedMineID === el.id ? (
                  <ChevronUp size={24} />
                ) : (
                  <ChevronDown size={24} />
                )}
              </div>
              {selectedMineID === el.id && (
                <div className="bg-gray-50 p-4 border-t text-sm">
                  <p>
                    <strong>Tenure:</strong> {el.tenure} years
                  </p>
                  <p>
                    <strong>Affect Radius:</strong> {el.affect_radius} km
                  </p>
                  <p>
                    <strong>Water Quality:</strong> {el.water_quality}
                  </p>
                  <p>
                    <strong>Air Quality:</strong> {el.air_quality}
                  </p>
                  <p>
                    <strong>Soil Quality:</strong> {el.soil_quality}
                  </p>
                  <p>
                    <strong>Biodiversity:</strong> {el.biodiversity}
                  </p>
                  <p>
                    <strong>Socioeconomic Index:</strong>{" "}
                    {el.socioeconomic_index}
                  </p>
                  <p>
                    <strong>Description:</strong> {el.description}
                  </p>
                </div>
              )}
            </div>
          ))
        ) : (
          <div className="text-center text-xl my-20">
            No matching mines found 🥲
          </div>
        )}
      </section>
    </div>
  );
}

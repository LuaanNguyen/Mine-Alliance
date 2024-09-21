import React, { useState } from "react";

const GenerateAssessment = ({
  locationId,
  selectedMineName,
}: {
  selectedMineName: undefined | string;
  locationId: number;
}) => {
  const [assessment, setAssessment] = useState(null);
  const [impactScale, setImpactScale] = useState(null);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleGenerateAssessment = async () => {
    setIsLoading(true);
    setError(null);

    try {
      const response = await fetch(`${process.env.BACKEND_URL}/assessment`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ location_id: locationId }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || "Failed to generate assessment");
      }

      const data = await response.json();
      setAssessment(data.assessment);
      setImpactScale(data.impact_scale);
    } catch (error) {
      console.error("Error:", error);
      setError(error instanceof Error ? error.message : String(error));
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="p-4 bg-white rounded-2xl mb-10 border-2 h-[400px] overflow-y-scroll ">
      <h2 className="text-lg mb-2">
        Generate LLM Assessment for your location{" "}
        <strong>{selectedMineName}📍</strong>
      </h2>
      <button
        onClick={handleGenerateAssessment}
        className="px-4 py-2 bg-[#88D66C] text-white rounded hover:bg-[#B4E380] focus:outline-none"
        disabled={isLoading}
      >
        {isLoading ? "Generating..." : "Generate Assessment"}
      </button>

      {isLoading ? <LoadingSpinner /> : null}

      {error && <p className="text-red-500 mt-2">{error}</p>}

      {assessment && (
        <div className="mt-4 rounded-2xl">
          <h3 className="font-semibold">Assessment:</h3>
          <p>{assessment}</p>
        </div>
      )}
    </div>
  );
};

const LoadingSpinner: React.FC = () => (
  <div className="flex justify-center items-center">
    <div className="relative mx-auto my-auto inset-0 w-12 h-12 rounded-full animate-spin border-8 border-dashed border-[#88D66C] border-t-transparent"></div>
  </div>
);

export default GenerateAssessment;

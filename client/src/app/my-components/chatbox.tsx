import React, { useState, useRef, useEffect } from "react";
import { Brain, Star } from "lucide-react";

interface ChatBoxProps {
  mineId: string;
}

const ChatBox: React.FC<ChatBoxProps> = ({ mineId }) => {
  const [message, setMessage] = useState("");
  const [chatHistory, setChatHistory] = useState<string[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [rating, setRating] = useState(0);
  const [feedback, setFeedback] = useState("");
  const chatEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chatHistory]);

  const handleRatingSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log(`Submitted rating: ${rating}, feedback: ${feedback}`);
    // Here you would typically send this data to your backend
    setRating(0);
    setFeedback("");
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!message.trim()) return;
    setError(null);
    setIsLoading(true);

    try {
      const response = await fetch(`${process.env.BACKEND_URL}/chatbot`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: message,
          mineId: mineId,
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || "Network response was not ok");
      }

      const data = await response.json();
      setChatHistory((prevHistory) => [
        ...prevHistory,
        `You: ${message}`,
        `Bot: ${data.response}`,
      ]);
      setMessage("");
    } catch (error) {
      console.error("Error:", error);
      setError(error instanceof Error ? error.message : String(error));
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex flex-col  border-l-2 border-gray-200 justify-start p-3 overflow-y-auto">
      <div className="flex flex-col h-[400px] border-2 rounded-2xl mb-4">
        <div className="p-4 rounded-t-2xl">
          <h2 className="text-xl text-[#88D66C] font-semibold flex items-center gap-2">
            <Brain />{" "}
            <span className="text-[#FDA668]">AI Assistant Connected</span>
          </h2>
        </div>
        <div className="flex-grow overflow-y-auto p-4 space-y-4">
          {chatHistory.map((msg, index) => (
            <div
              key={index}
              className={`flex ${
                msg.startsWith("You:") ? "justify-end" : "justify-start"
              }`}
            >
              <div
                className={`max-w-[70%] px-4 py-2 rounded-lg ${
                  msg.startsWith("You:")
                    ? "bg-[#FDA668] text-white"
                    : "bg-white text-gray-800 border border-gray-300"
                }`}
              >
                <p className="break-words">{msg}</p>
              </div>
            </div>
          ))}
          {error && <p className="text-red-500 text-center">{error}</p>}
          {isLoading && <LoadingSpinner />}
          <div ref={chatEndRef} />
        </div>
        <form onSubmit={handleSubmit} className="p-4 border-t border-gray-200">
          <div className="flex space-x-2">
            <input
              type="text"
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              placeholder="Ask about mining quality..."
              className="flex-grow bg-white  px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-[#FDA668]"
              disabled={isLoading}
            />
            <button
              type="submit"
              className="px-4 py-2 bg-[#88D66C] text-white rounded-lg hover:bg-[#B4E380] focus:outline-none focus:ring-2 focus:ring-[#FDA668] disabled:opacity-50"
              disabled={isLoading}
            >
              {isLoading ? "Sending..." : "Send"}
            </button>
          </div>
        </form>
      </div>

      <div className="flex flex-col">
        <form
          onSubmit={handleRatingSubmit}
          className="bg-white p-4 rounded-2xl "
        >
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2">
              Rate your experience at Moreci Mine:
            </label>
            <div className="flex">
              {[1, 2, 3, 4, 5].map((star) => (
                <Star
                  key={star}
                  size={24}
                  onClick={() => setRating(star)}
                  className={`cursor-pointer ${
                    star <= rating
                      ? "text-yellow-400 fill-current"
                      : "text-gray-300"
                  }`}
                />
              ))}
            </div>
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2">
              Your feedback:
            </label>
            <textarea
              value={feedback}
              onChange={(e) => setFeedback(e.target.value)}
              className="w-full px-3 py-2 bg-white text-gray-700 border rounded-lg focus:outline-none"
              rows={3}
              placeholder="Please share your thoughts..."
            ></textarea>
          </div>
          <button
            type="submit"
            className="bg-[#88D66C] text-white font-bold py-2 px-4 rounded hover:bg-[#B4E380] focus:outline-none focus:shadow-outline"
          >
            Submit Feedback
          </button>
        </form>
      </div>
    </div>
  );
};
export default ChatBox;

const LoadingSpinner: React.FC = () => (
  <div className="flex justify-center items-center">
    <div className="relative  mx-auto my-auto inset-0 w-12 h-12 rounded-full animate-spin border-8 border-dashed border-[#88D66C] border-t-transparent"></div>
  </div>
);

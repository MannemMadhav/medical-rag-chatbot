import { useEffect, useState } from "react";
import "./App.css";
import { streamQuestion } from "./api/chat";

import Sidebar from "./components/Sidebar";
import ChatHeader from "./components/ChatHeader";
import ChatInput from "./components/ChatInput";
import ChatMessages from "./components/ChatMessages";

function App() {

    const defaultMessages = [
        {
            sender: "bot",
            text: "👋 Hello! Ask me any medical question.",
            sources: [],
        },
    ];

    const [question, setQuestion] = useState("");
    const [loading, setLoading] = useState(false);

    const [messages, setMessages] = useState(() => {

        const saved = localStorage.getItem("medical_chat");

        if (saved) {
            return JSON.parse(saved);
        }

        return defaultMessages;

    });

    useEffect(() => {

        localStorage.setItem(
            "medical_chat",
            JSON.stringify(messages)
        );

    }, [messages]);

    const clearChat = () => {

        localStorage.removeItem("medical_chat");
        setMessages(defaultMessages);

    };

    const handleSend = async () => {

        if (!question.trim()) return;

        const currentQuestion = question;

        setMessages((prev) => [

            ...prev,

            {
                sender: "user",
                text: currentQuestion,
            },

            {
                sender: "bot",
                text: "",
                sources: [],
            },

        ]);

        setQuestion("");
        setLoading(true);

        try {

            const response = await streamQuestion(

                currentQuestion,

                (partialAnswer) => {

                    setMessages((prev) => {

                        const updated = [...prev];

                        updated[updated.length - 1] = {

                            ...updated[updated.length - 1],
                            text: partialAnswer,

                        };

                        return updated;

                    });

                }

            );

            setMessages((prev) => {

                const updated = [...prev];

                updated[updated.length - 1] = {

                    ...updated[updated.length - 1],
                    text: response.answer,
                    sources: response.sources,

                };

                return updated;

            });

        } catch {

            setMessages((prev) => {

                const updated = [...prev];

                updated[updated.length - 1] = {

                    sender: "bot",
                    text: "❌ Failed to contact backend.",
                    sources: [],

                };

                return updated;

            });

        } finally {

            setLoading(false);

        }

    };

    return (

        <div className="app">

            <Sidebar onClearChat={clearChat} />

            <div className="chat-container">

                <ChatHeader />

                <ChatMessages
                    messages={messages}
                    loading={loading}
                />

                <ChatInput
                    question={question}
                    setQuestion={setQuestion}
                    handleSend={handleSend}
                    loading={loading}
                />

            </div>

        </div>

    );

}

export default App;
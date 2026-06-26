import { useEffect, useRef } from "react";
import MessageBubble from "./MessageBubble";
import TypingIndicator from "./TypingIndicator";

function ChatMessages({ messages, loading }) {

    const messagesEndRef = useRef(null);

    useEffect(() => {
        messagesEndRef.current?.scrollIntoView({
            behavior: "smooth",
        });
    }, [messages, loading]);

    return (

        <div className="messages">

            {messages.map((message, index) => (

                <MessageBubble
                    key={index}
                    message={message}
                />

            ))}

            {loading && <TypingIndicator />}

            <div ref={messagesEndRef}></div>

        </div>

    );

}

export default ChatMessages;
function ChatInput({
    question,
    setQuestion,
    handleSend,
    loading,
}) {

    return (

        <div className="input-area">

            <input
                type="text"
                placeholder="Ask a medical question..."
                value={question}
                onChange={(e) =>
                    setQuestion(e.target.value)
                }
                onKeyDown={(e) => {

                    if (e.key === "Enter") {
                        handleSend();
                    }

                }}
                disabled={loading}
            />

            <button
                onClick={handleSend}
                disabled={loading}
            >
                {loading ? "Thinking..." : "Send"}
            </button>

        </div>

    );

}

export default ChatInput;
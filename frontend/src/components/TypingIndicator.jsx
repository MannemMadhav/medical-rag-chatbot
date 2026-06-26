function TypingIndicator() {
    return (
        <div className="bot-message">
            <div
                style={{
                    display: "flex",
                    alignItems: "center",
                    gap: "8px",
                    color: "#94A3B8",
                    fontStyle: "italic",
                }}
            >
                🤖 AI is thinking
                <span className="typing-dots">
                    <span>.</span>
                    <span>.</span>
                    <span>.</span>
                </span>
            </div>
        </div>
    );
}

export default TypingIndicator;
import { useState } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism";

function MessageBubble({ message }) {

    const [copied, setCopied] = useState(false);

    const copyToClipboard = async () => {

        try {

            await navigator.clipboard.writeText(message.text);

            setCopied(true);

            setTimeout(() => {
                setCopied(false);
            }, 2000);

        } catch (error) {

            console.error(error);

        }

    };

    return (

        <div
            className={
                message.sender === "user"
                    ? "user-message"
                    : "bot-message"
            }
        >

            {message.sender === "bot" && (

                <div
                    style={{
                        display: "flex",
                        justifyContent: "flex-end",
                        marginBottom: "10px",
                    }}
                >

                    <button
                        onClick={copyToClipboard}
                        style={{
                            border: "none",
                            background: "transparent",
                            cursor: "pointer",
                            color: "#60A5FA",
                            fontSize: "13px",
                            fontWeight: "600",
                        }}
                    >
                        {copied ? "✅ Copied" : "📋 Copy"}
                    </button>

                </div>

            )}

            <ReactMarkdown
                remarkPlugins={[remarkGfm]}
                components={{
                    code({
                        inline,
                        className,
                        children,
                        ...props
                    }) {

                        const match = /language-(\w+)/.exec(className || "");

                        return !inline && match ? (

                            <SyntaxHighlighter
                                style={oneDark}
                                language={match[1]}
                                PreTag="div"
                                {...props}
                            >
                                {String(children).replace(/\n$/, "")}
                            </SyntaxHighlighter>

                        ) : (

                            <code
                                className={className}
                                {...props}
                            >
                                {children}
                            </code>

                        );

                    },
                }}
            >
                {message.text}
            </ReactMarkdown>

            {message.sources &&
                message.sources.length > 0 && (

                    <div
                        style={{
                            marginTop: "18px",
                        }}
                    >

                        <div
                            style={{
                                fontWeight: "bold",
                                color: "#93C5FD",
                                marginBottom: "10px",
                            }}
                        >
                            📄 Sources
                        </div>

                        {message.sources.map((source, index) => (

                            <div
                                key={index}
                                style={{
                                    background: "#1E293B",
                                    border: "1px solid #334155",
                                    borderRadius: "10px",
                                    padding: "12px",
                                    marginBottom: "10px",
                                }}
                            >

                                <div
                                    style={{
                                        fontWeight: "600",
                                        color: "#F8FAFC",
                                    }}
                                >
                                    📄 {source}
                                </div>

                                <div
                                    style={{
                                        marginTop: "6px",
                                        fontSize: "12px",
                                        color: "#94A3B8",
                                    }}
                                >
                                    Trusted Medical Reference
                                </div>

                            </div>

                        ))}

                    </div>

                )}

        </div>

    );

}

export default MessageBubble;
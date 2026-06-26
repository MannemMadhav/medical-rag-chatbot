import { useEffect, useRef, useState } from "react";
import axios from "axios";

function Sidebar({ onClearChat }) {
    const fileInputRef = useRef(null);

    const [currentPdf, setCurrentPdf] = useState("");
    const [documents, setDocuments] = useState([]);

    const loadDocuments = async () => {
        try {
            const response = await axios.get(
                "http://127.0.0.1:8000/documents"
            );

            setDocuments(response.data.documents || []);
        } catch (error) {
            console.error("Failed to load documents", error);
        }
    };

    useEffect(() => {
        loadDocuments();
    }, []);

    const handleUploadClick = () => {
        fileInputRef.current.click();
    };

    const handleFileChange = async (event) => {
        const file = event.target.files[0];

        if (!file) return;

        const formData = new FormData();
        formData.append("file", file);

        try {
            await axios.post(
                "http://127.0.0.1:8000/upload",
                formData,
                {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    },
                }
            );

            setCurrentPdf(file.name);
            await loadDocuments();

            alert("✅ PDF uploaded successfully!");
        } catch (error) {
            console.error(error);
            alert("❌ Failed to upload PDF.");
        }
    };

    const handleDelete = async (filename) => {
        const confirmed = window.confirm(
            `Delete "${filename}"?`
        );

        if (!confirmed) return;

        try {
            await axios.delete(
                `http://127.0.0.1:8000/documents/${encodeURIComponent(filename)}`
            );

            if (currentPdf === filename) {
                setCurrentPdf("");
            }

            await loadDocuments();

            alert("✅ Document deleted.");
        } catch (error) {
            console.error(error);
            alert("❌ Failed to delete document.");
        }
    };

    return (
        <div className="sidebar">

            <h2>Medical AI</h2>

            <input
                type="file"
                accept=".pdf"
                ref={fileInputRef}
                onChange={handleFileChange}
                style={{ display: "none" }}
            />

            <button
                className="upload-btn"
                onClick={handleUploadClick}
            >
                📄 Upload PDF
            </button>

            {currentPdf && (
                <div
                    style={{
                        marginTop: "20px",
                        padding: "12px",
                        borderRadius: "10px",
                        background: "#1E293B",
                        border: "1px solid #334155",
                    }}
                >
                    <div
                        style={{
                            color: "#93C5FD",
                            fontWeight: "bold",
                            marginBottom: "8px",
                        }}
                    >
                        📚 Current Document
                    </div>

                    <div
                        style={{
                            color: "#F8FAFC",
                            fontSize: "14px",
                            wordBreak: "break-word",
                        }}
                        title={currentPdf}
                    >
                        ✅ {currentPdf}
                    </div>
                </div>
            )}

            <div
                style={{
                    marginTop: "20px",
                    padding: "12px",
                    borderRadius: "10px",
                    background: "#111827",
                    border: "1px solid #334155",
                }}
            >
                <div
                    style={{
                        color: "#93C5FD",
                        fontWeight: "bold",
                        marginBottom: "10px",
                    }}
                >
                    📚 Uploaded Documents
                </div>

                {documents.length === 0 ? (
                    <div
                        style={{
                            color: "#9CA3AF",
                            fontSize: "14px",
                        }}
                    >
                        No documents uploaded.
                    </div>
                ) : (
                    documents.map((doc) => (
                        <div
                            key={doc.name}
                            style={{
                                display: "flex",
                                justifyContent: "space-between",
                                alignItems: "center",
                                marginBottom: "8px",
                                gap: "8px",
                            }}
                        >
                            <span
                                title={doc.name}
                                style={{
                                    color: "#F8FAFC",
                                    fontSize: "14px",
                                    overflow: "hidden",
                                    textOverflow: "ellipsis",
                                    whiteSpace: "nowrap",
                                    flex: 1,
                                }}
                            >
                                📄 {doc.name}
                            </span>

                            <button
                                onClick={() => handleDelete(doc.name)}
                                style={{
                                    background: "transparent",
                                    border: "none",
                                    cursor: "pointer",
                                    color: "#EF4444",
                                    fontSize: "16px",
                                }}
                                title="Delete document"
                            >
                                🗑
                            </button>
                        </div>
                    ))
                )}
            </div>

            <button
                className="upload-btn"
                style={{
                    marginTop: "15px",
                    background: "#DC2626",
                }}
                onClick={onClearChat}
            >
                🗑 Clear Chat
            </button>

        </div>
    );
}

export default Sidebar;
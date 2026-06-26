import axios from "axios";
import config from "../config";

const API = axios.create({
    baseURL: config.API_URL,
});

export const askQuestion = async (question) => {

    const response = await API.post("/chat", {
        question,
    });

    return response.data;
};

export const streamQuestion = async (question, onChunk) => {

    const response = await fetch(
        `${config.API_URL}/chat/stream`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                question,
            }),
        }
    );

    if (!response.ok) {
        throw new Error("Streaming failed");
    }

    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    let answer = "";

    while (true) {

        const { done, value } = await reader.read();

        if (done) {
            break;
        }

        const chunk = decoder.decode(value);

        answer += chunk;

        onChunk(answer);
    }

    return {
        answer,
        sources: [],
    };
};
const express = require('express');
const cors = require('cors');
const { GoogleGenerativeAI } = require('@google/generative-ai');

const app = express();
const PORT = 3001;

const genAI = new GoogleGenerativeAI('enter_your_api_key ');
const model = genAI.getGenerativeModel({ model: 'gemini-1.5-flash' });

app.use(cors());
app.use(express.json());

app.post('/generateContent', async (req, res) => {
    const prompt = req.body.prompt;

    if (!prompt) {
        return res.status(400).json({ error: 'Prompt is required!' });
    }

    try {
        const result = await model.generateContent(prompt);

        res.json({
            response: result.response.text()
        });
    } catch (error) {
        console.error("Error generating content:", error);
        res.status(500).json({
            error: "Server Error!"
        });
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

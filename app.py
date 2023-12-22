// pages/index.js
import { useState } from 'react';

const API_URL = 'https://api.afforai.com/api/api_completion';

const Home = () => {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');

  const handleQuestionSubmit = async () => {
    try {
      const apiKey = 'fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e';
      const sessionID = '65489d7c9ad727940f2ab26f';

      const requestBody = {
        apiKey,
        sessionID,
        history: [{ role: 'user', content: question }],
        powerful: false,
        google: true,
      };

      const response = await fetch(API_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestBody),
      });

      const data = await response.json();

      // Assuming the API response structure includes an answer field
      if (data.answer) {
        setAnswer(data.answer);
      } else {
        setAnswer('No answer found.');
      }
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div>
      <h1>Guatemalan Law Q&A</h1>
      <div>
        <label>
          Enter your question:
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
          />
        </label>
        <button onClick={handleQuestionSubmit}>Submit</button>
      </div>
      <div>
        <h2>Answer:</h2>
        <p>{answer}</p>
      </div>
    </div>
  );
};

export default Home;

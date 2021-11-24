import React from 'react';
import './App.css';

const gretting = "gretting";
const displayEmojiName = event => alert(event.target.id);
const emojis = [
  {
    emoji: "😀",
    name: "grinning face"
  },
  {
    emoji: "🎉",
    name: "party popper"
  },
  {
    emoji: "💃",
    name: "woman dancing"
  }
];

function App() {
  const displayAction = true;
  return  (
  <div className="container">
    <h1 id={gretting}>Hello World</h1> 
    {displayAction && <p>I am writing JSX</p>}
    <ul>
      {
        emojis.map(emoji => (
          <li key={emoji.name}>
            <button
              onClick={displayEmojiName}>
              <span role="img" aria-label={emoji.name} id={emoji.name}>{emoji.emoji}</span>
            </button>
          </li>
        ))
      }
    </ul>
  </div>);
}

export default App;
import React from 'react';
import './App.css';

const App = () => {
  const buttons = [
    { text: 'Google', url: 'https://entypublic.github.io/xdmines/', image: '/images/11.png' },
    { text: 'YouTube', url: 'https://volneer.github.io/jea/', image: '/images/2.png' },
    { text: 'GitHub', url: 'https://volneer.github.io/avai/', image: '/images/33.png' },
    { text: 'Twitter', url: 'https://volneer.github.io/bb/', image: '/images/44.png' },
    { text: 'Facebook', url: 'https://volneer.github.io/raayl/', image: '/images/5.png' },
  ];

  return (
    <div className="app">

      <div className="button-container">
        {buttons.map((button, index) => (
          <a
            key={index}
            href={button.url}
            rel="noopener noreferrer"
            className="neon-button"
            style={{
              backgroundImage: `url(${button.image})`,
              backgroundSize: 'cover',
              backgroundPosition: 'center',
            }}
          >

          </a>
        ))}
      </div>
    </div>
  );
};

export default App;
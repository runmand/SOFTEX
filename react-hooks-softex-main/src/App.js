import './App.css';
import React, { useState } from 'react';


function App() {
  const [count, setCount] = useState(0)

  return(
    <div>
      <p>Voce clicou {count} vezes</p>
      <button onClick={() => setCount(count + 1)}>
        Clique Aqui
      </button>
    </div>
  )
}


export default App;

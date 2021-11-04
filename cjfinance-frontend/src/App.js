import Fin from "./components/Fin";
import "./App.css";
import { useState } from "react";
import axios from "axios";

function App() {
  const fin = [
    {
      id:1,
      title: "Receita de miojo",
      content:
        "Bata com um martelo antes de abrir o pacote. Misture o tempero, coloque em uma vasilha e aproveite seu snack :)",
    },
    {
      id: 2,
      title: "Sorvete de banana",
      content: "Coloque a banana no congelador e espere.",
    },
  ];
  axios
  .get("http://localhost:8000/api/notes/")
  .then((res) => console.log(res));

  return (
    <div className="App">
      {fin.map((fin) => (
          <Fin key={`fin__${fin.id}`} title={fin.title}>
            {fin.content}
          </Fin>
      ))}
    </div>
  );
}

export default App;
import React from "react";
import "./index.css";

export default function Fin(props) {
  return (   
  <div className="card">
      <h3 className="card-title">{props.title}</h3>
      <div className="card-content">{props.children}</div>
</div>
  )
}
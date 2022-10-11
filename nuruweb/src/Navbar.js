import React from "react";
import "./nav.css"
import pic from './Images/NuruLogo.png'

const navbar=()=> {

  return(
    <div>
      <div className="topnav" >
        <div className="navbar">   
          <a href="#home" class="active">Home</a>
          <a href="#news">About</a>
          <a href="#contact">Contact</a>        
          <button className="btn">Login</button>
        </div> 
        <div className="image">
          <img src={pic}></img>
        </div>
      </div>
    </div>
  );
}
export default navbar;


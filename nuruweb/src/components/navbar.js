import React from "react";
import "./nav.css"

 const Navbar=()=> {

    return(
        <>
        <div class="topnav" id="myTopnav">
        <a href="#home" class="active">Home</a>
        <a href="#news">About</a>
        <a href="#contact">Contact</a>
        <a href="javascript:void(0);" class="icon" onclick="myFunction()">
          <i class="fa fa-bars"></i>
        </a>
       
      </div>

      <div>
      <button>Login</button>

      </div>
    </>
);
}
export default Navbar;


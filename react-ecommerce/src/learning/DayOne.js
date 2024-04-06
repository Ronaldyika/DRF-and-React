import React,{useState} from "react";

const DayOne=()=>{
    return(
        <div>
            <form className="formComtainer">
                <div>
                    <label for='firstName'>First Name</label><br/>
                    <input type="text" placeholder="Enter first name" />
                </div>
                <div>
                    <label for='lastName'>Last Name</label><br/>
                    <input type="text" placeholder="Enter last name"/>
                </div>
                <div>
                    <label for='email'>Email</label><br/>
                    <input type="email" placeholder="Enter a valid email"/>
                </div>
                <div>
                    <label for='password'>Pasword</label><br/>
                    <input type="password" placeholder="Enter first name"/>
                </div>

                <button type="submint">Register</button>
            </form>
        </div>
    );
}

export default DayOne
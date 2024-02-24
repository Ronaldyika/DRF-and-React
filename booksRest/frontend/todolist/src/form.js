import React, {Component} from "react";

export function Form(){
    return(
        <div className="form-wrapper">
            <div className="form-title">
                <h2>User Submission Form</h2>
            </div>
            <div className="formcontent">
                <div className="username">
                    <label>Username</label>
                    <input className="formcontentitem" type="text" placeholder="enter username"/>
                </div>
                <div className="useremail">
                    <label>UserEmail</label>
                    <input type="email" placeholder="input email" className="formcontentitem"/>
                </div>
                <div className="primaryBtn">
                    <button>Submit</button>
                </div>
            </div>
            <div className="btnarea">
                <button >register</button>
                <button>forgot login</button>
            </div>
        </div>
    );
}

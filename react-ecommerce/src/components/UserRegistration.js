import React,{useState} from "react";

import api from '../service/api'

const UserRegistration =()=>{
    const [formData,setFormData] = useState({
        username:'',
        email:'',
        password1:'',
        password2:''
    });
    const handleInputChange=(e)=>{
        setFormData({formData,[e.target.name]:e.target.value});
    };

    const handleRegistration=async(e) =>{
        e.preventDefault();
        try{
            const response = await api.post('register/',formData);
            console.log('Registration succeess:',response);

            // redirect to loginpage
        }catch(error){
            console.error('Registration failed',error);

            //handle failure (show error message)
        }
    };

    return(
        <div>
            <h2>User Registration</h2>
            <form method="post" onSubmit={handleRegistration}>
                <input type="text" value={username} placeholder="enter a user name" required='true'></input>
                <input type="email" value={email} placeholder="enter an email" required='true'></input>
                <input type="password" value={password1} placeholder="enter a password" required='true'></input>
                <input type="password" value={password2} placeholder="password confirmation" required='true'></input>
                <button type="submit">Register</button>
            </form>
        </div>
    );
}


export default UserRegistration;
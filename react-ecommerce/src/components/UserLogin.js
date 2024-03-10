import React,{useState} from "react";
import api from '../services/api';

const UserLogin = ()=>{
    const [formData,setFormData]=useState({
        username: '',
        password: '',
    });

    const handleInputChange=(e)=>{
        setFormData({...formData,[e.target.name]: e.target.value});

    };

    const handleLogin = async(e)=>{
        e.preventDefault();
        try{
            const response = await api.post('login/',formData);
            console.log('login success', response);

            //set authentication token , redirect to dashboard
        }catch(error){
            console.error('login failed',error);

            // handle the failure 
        }
    };

    return( 
        <div>
            < h2>Login user</h2>
            <form onSubmit={handleLogin}>
                <input type="text" value={username} placeholder="enter a user name" required='true'></input>
                <input type="password" value={password} placeholder="enter a password" required='true'></input>
                <button type="submit">Login</button>
            </form>
        </div>
    );
}

export default UserLogin
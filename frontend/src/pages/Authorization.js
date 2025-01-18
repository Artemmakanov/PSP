import React, { useState } from "react"

export default function Authorization() {

    const [login, setLogin] = useState('');
    const [password, setPassword] = useState('');
    // const [Jwt, setJwt] = useState('');

 
    function handleLogin(event) {
        setLogin(event.target.value);
    };

    function handlePassword(event) {
        setPassword(event.target.value);
    };

    function handleSubmit(event) {
        fetch('http://0.0.0.0:5000/login',
            {
                method: 'post',
                headers: {'Content-Type':'application/json'},
                body: JSON.stringify({
                     "password": password,
                     "login": login 
                })
            }
        )
        .then((res) => res.json())
        .then(json => localStorage.setItem(
            'token', json.token) 
        );
        event.preventDefault();
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label>
                    login input: <input name="myLogin" onChange={e=>handleLogin(e)}/>
                </label>
                <label>
                    password input: <input name="myPassword" onChange={e=>handlePassword(e)}/>
                </label>
            <input type="submit" value="Login" />
            </form>
        </div>
    );
}
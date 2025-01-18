import React, { useState } from "react"

export default function Authorization() {

    const [login, setLogin] = useState('');
    const [password, setPassword] = useState('');
    const [name, setName] = useState('');
    const [surname, setSurname] = useState('');
    const [patronymic, setPatronymic] = useState('');

 
    function handleLogin(event) {
        setLogin(event.target.value);
    };

    function handlePassword(event) {
        setPassword(event.target.value);
    };

    function handleName(event) {
        setName(event.target.value);
    };

    function handleSurname(event) {
        setSurname(event.target.value);
    };
    
    function handlePatronymic(event) {
        setPatronymic(event.target.value);
    };

    function handleSubmit(event) {
        fetch('http://0.0.0.0:5000/register',
            {
                method: 'post',
                headers: {'Content-Type':'application/json'},
                body: JSON.stringify({
                     "password": password,
                     "login": login,
                     "name": name,
                     "surname": surname,
                     "patronymic": patronymic
                })
            }
        )
        event.preventDefault();
    };
    

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label>
                    name input: <input name="myName" onChange={e=>handleName(e)}/>
                </label>
                <label>
                    surname input: <input name="mySurname" onChange={e=>handleSurname(e)}/>
                </label>
                <label>
                    patronymic input: <input name="myPatronymic" onChange={e=>handlePatronymic(e)}/>
                </label>
                <label>
                    password input: <input name="myPassword" onChange={e=>handlePassword(e)}/>
                </label>
                <label>
                    login input: <input name="myLogin" onChange={e=>handleLogin(e)}/>
                </label>
            <input type="submit" value="Register" />
            </form>
        </div>
    );
}
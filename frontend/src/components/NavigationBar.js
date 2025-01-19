import React, { useContext } from "react"
import { useAuth } from "../provider/authProvider"


export default function NavigationBar ({ children }) {

    const { user } = useAuth();
    return (
        <div>
            <header>
                <a href="/authorization">authorization</a>
            </header>
            <header>
                <a href="/registration">registration</a>
            </header>
            <header>
                <a href="/search">search</a>
            </header>
            <header>
                <a href="/logout">logout</a>
            </header>
            <a>{user}</a>
            {children}
        </div>
     )
}
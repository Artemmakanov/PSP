import React, {useEffect} from "react"
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Authorization from "./routes/Authorization"
import Registration from "./routes/Registration"

export default function App() {

    return (
        <BrowserRouter>
            <Routes>
                <Route path="authorization" element={<Authorization/>}/>
                <Route path="registration" element={<Registration/>}/>
                {/* </Route>
                <Route path="/search">
                    <Search/>
                </Route>
                <Route path="/paper">
                    <Paper/>
                </Route>
                <Route path="/profile">
                    <Profile/>
                </Route> */} 
            </Routes>
        </BrowserRouter>
    )
}
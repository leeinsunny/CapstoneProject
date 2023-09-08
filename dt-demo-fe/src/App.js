import React from "react";
import Navbar from "./components/Navbar";
import {
    BrowserRouter as Router,
    Routes,
    Route,
    Navigate,
} from "react-router-dom";
import { Global } from "@emotion/react";
import { reset } from "./styles/reset";
import Home from "./pages/01_home";
import Filter from "./pages/02_filter";
import Converter from "./pages/03_converter";
import Statistics from "./pages/04_statistics";

function App() {
    return (
        <>
            <Global styles={reset} />
            <Router>
                <Navbar />
                <Routes>
                    <Route
                        exact
                        path="/"
                        element={<Navigate replace to="/home" />}
                    />
                    <Route path="/home" element={<Home />} />
                    <Route path="/filter" element={<Filter />} />
                    <Route path="/converter" element={<Converter />} />
                    <Route path="/statistics" element={<Statistics />} />
                </Routes>
            </Router>
        </>
    );
}

export default App;

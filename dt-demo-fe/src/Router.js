import Navbar from "./components/Navbar";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Home from "./pages/01_home";
import Filter from "./pages/02_filter";
import Converter from "./pages/03_converter";
import Statistics from "./pages/04_statistics";

const Router = () => {
    return (
        <BrowserRouter>
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
        </BrowserRouter>
    );
};

export default Router;

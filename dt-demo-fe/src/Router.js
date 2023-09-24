import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Navbar from "./components/navbar/index";
import Home from "./pages/01_home";
import Filter from "./pages/02_filter";
import Converter from "./pages/03_converter";
import Statistics from "./pages/04_statistics";
import DetectionContainer from "./pages/filtering/detectionReport";
import ConversionContainer from "./pages/filtering/conversionReport";
import FilterMain from "./pages/filtering";

const Router = () => {
    return (
        <BrowserRouter>
            <Navbar />
            <Routes>
                <Route path="/" element={<Navigate replace to="/home" />} />
                <Route path="/home" element={<Home />} />
                <Route path="/filter" element={<Filter />}>
                    <Route index element={<FilterMain />} />
                    <Route path="detection" element={<DetectionContainer />} />
                    <Route
                        path="conversion"
                        element={<ConversionContainer />}
                    />
                </Route>
                <Route path="/converter" element={<Converter />} />
                <Route path="/statistics" element={<Statistics />} />
            </Routes>
        </BrowserRouter>
    );
};

export default Router;

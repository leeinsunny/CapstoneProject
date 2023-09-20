import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Navbar from "./components/navbar/index";
import Home from "./pages/01_home";
import Filter from "./pages/02_filter";
import Converter from "./pages/03_converter";
import Statistics from "./pages/04_statistics";
import FileListContainer from "./pages/filtering/filelist";
import RulesContainer from "./pages/filtering/rules";
import ReportContainer from "./pages/filtering/report";

const Router = () => {
    return (
        <BrowserRouter>
            <Navbar />
            <Routes>
                <Route path="/" element={<Navigate replace to="/home" />} />
                <Route path="/home" element={<Home />} />
                <Route path="/filter" element={<Filter />}>
                    <Route path="filelist" element={<FileListContainer />} />
                    <Route path="rules" element={<RulesContainer />} />
                    <Route path="report" element={<ReportContainer />} />
                </Route>
                <Route path="/converter" element={<Converter />} />
                <Route path="/statistics" element={<Statistics />} />
            </Routes>
        </BrowserRouter>
    );
};

export default Router;

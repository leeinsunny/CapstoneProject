import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Navbar from "./components/navbar/index";
import Home from "./pages/01_home";
import Filter from "./pages/02_filter";
import Converter from "./pages/03_converter";
import Statistics from "./pages/04_statistics";
import DemoFileList from "./pages/demo/filelist";
import DemoRules from "./pages/demo/rules";
import DemoReport from "./pages/demo/report";
import DemoUpload from "./pages/demo/upload";

const Router = () => {
    return (
        <BrowserRouter>
            <Navbar />
            <Routes>
                <Route path="/" element={<Navigate replace to="/home" />} />
                <Route path="/home" element={<Home />} />
                <Route path="/filter" element={<Filter />}>
                    <Route index element={<DemoUpload />} />
                    <Route path="filelist" element={<DemoFileList />} />
                    <Route path="rules" element={<DemoRules />} />
                    <Route path="report" element={<DemoReport />} />
                </Route>
                <Route path="/converter" element={<Converter />} />
                <Route path="/statistics" element={<Statistics />} />
            </Routes>
        </BrowserRouter>
    );
};

export default Router;

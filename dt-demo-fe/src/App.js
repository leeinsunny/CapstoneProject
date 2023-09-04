// import logo from './logo.svg';
import React from 'react';
import './App.css';
import Navbar from './components/Navbar';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/01_home';
import Filter from './pages/02_filter';
import Converter from './pages/03_converter';
import Statistics from './pages/04_statistics';

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path='/home' element={<Home/>} />
        <Route path='/filter' element={<Filter/>} />
        <Route path='/converter' element={<Converter/>} />
        <Route path='/statistics' element={<Statistics/>} />
      </Routes>
  </Router>
  );
}

export default App;

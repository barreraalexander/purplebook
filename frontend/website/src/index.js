import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import './scss/main.scss';

//Pages
import Landing from './components/pages/Landing';
import About from './components/pages/About';
import Account from './components/pages/Account';
import Contact from './components/pages/Contact';
import Dashboard from './components/pages/Dashboard';

//Components
import MainHeader from './components/navbars/main-header.component';

//JS


ReactDOM.render(
    <Router>
    <MainHeader />
    <Routes>
    <Route
        path="/"
        element={<Landing/>}
        exact
        />
    <Route
        path="/about"
        element={<About/>}
        exact
        />
    <Route
        path="/contact"
        element={<Contact/>}
        exact
        />
    <Route
        path="/account"
        element={<Account/>}
        exact
        />
    <Route
        path="/dashboard"
        element={<Dashboard/>}
        exact
        />
    </Routes>
</Router>,
    document.getElementById('root')
  );
  
import React from 'react'
import { NavLink } from "react-router-dom";
import Dashboard from './../pages/Dashboard';


import { ReactComponent as HeaderImg } from '../../static/images/assets/header.svg'
import { ReactComponent as Logo } from '../../static/images/icons/logo.svg'


export default function MainHeader() {
    return (
        <section id="main_header_section">
                <HeaderImg className="header_img"/>
                <ul>
                    <NavLink
                        to="/"
                        activeClassName="is-active"
                        exact
                    >
                    Home
                    </NavLink>

                    <NavLink
                        to="/account"
                        activeClassName="is-active"
                        exact
                    >
                    Account
                    </NavLink>

                    <NavLink
                        to="/about"
                        activeClassName="is-active"
                        exact
                    >
                    About
                    </NavLink>
                    
                    <NavLink
                        to="/contact"
                        activeClassName="is-active"
                        exact
                    >
                    Contact
                    </NavLink>

                    <NavLink
                        to="/dashboard"
                        activeClassName="is-active"
                        exact
                    >
                    Dashboard
                    </NavLink>
                </ul>
        </section>
    )
}

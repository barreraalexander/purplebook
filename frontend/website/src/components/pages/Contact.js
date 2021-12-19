import React, {Component} from 'react';
import { render } from 'react-dom';


export default class Contact extends Component {
    constructor(props){
        super(props);
    }

    componentWillMount(){
        document.body.dataset.body_type = 'alt1'
    }

    render(){
        return (
        <section id="Contact">
            <h1>
                Contact
            </h1>
        </section>
        )
    }
};

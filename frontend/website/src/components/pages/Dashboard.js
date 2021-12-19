import React, {Component} from 'react';

export default class Dashboard extends Component {
    constructor(props){
        super(props);
    }

    componentWillMount(){
        document.body.dataset.body_type = 'alt1'
    }

    render(){
        return (
            <section id="Dashboard">
                <h1>
                    Dashboard
                </h1>
            </section>
        )
    }
} 

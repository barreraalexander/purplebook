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
            <div className="heading_ctnr">
                <p>
                    hello there
                </p>
                <h1>
                    Name
                </h1>
                <small>
                    emailme@gmail.com
                </small>
            </div>
            </section>
        )
    }
} 

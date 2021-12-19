import React, {Component} from 'react';

import AuthorizeForm from '../forms/authorize.component';

export default class Account extends Component {
    constructor(props){
        super(props);
    }

    componentWillMount(){
        document.body.dataset.body_type = 'alt3'
    }

    render(){
        return (
        <section id="Account">
            <div className="heading_ctnr">
                <p id="heading_ctnr1">
                    let's create
                </p>
                <h1 id="heading_ctnr2">
                    An Account
                </h1>
                <small>
                    fill out the form
                </small>
                <AuthorizeForm action_type='register'/>
            </div>

        </section>
        )
    }
}

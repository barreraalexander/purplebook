import React, {Component} from 'react';

import Explanation1 from './../sections/explanation1.component';
import Explanation2 from './../sections/explanation2.component';
import Explanation3 from './../sections/explanation3.component';
import CallToAction from './../sections/call_to_action.component';


export default class Landing extends Component {
    constructor(props){
        super(props);
    }

    componentWillMount(){
        document.body.dataset.body_type = 'alt1'
    }

    

    render(){
        return (
        <section id="Landing">
            <div className="heading_ctnr">
                <p>
                    welcome to
                </p>
                <h1>
                    Purple Buckets
                </h1>
                <small>
                    prettify the mayhem
                </small>
            </div>
            <Explanation1 />
            <Explanation2 />
            <Explanation3 />
            <CallToAction />
        </section>
        )
    }
}
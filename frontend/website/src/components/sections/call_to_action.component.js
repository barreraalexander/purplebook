import React, {Component} from 'react';

import { ReactComponent as Img1 } from '../../static/images/assets/ending_splash.svg'


export default class CallToAction extends Component{
    constructor(props){
        super(props);
    }
    render(){
        return (
            <section id="CallToAction">
                {/* <Img1 /> */}
                <div className="heading_ctnr">
                    <small>
                        Making sense of the world,
                    </small>
                    <h1>
                        one drop at a time
                    </h1>
                </div>
                <div className="cta_ctnr">
                    <a href="/account">
                        <h2>
                            create a free
                        </h2>
                            <button type="button">
                                ACCOUNT
                            </button>
                        <small>
                            sign up and get started instantly
                        </small>
                    </a>
                </div>
            </section>
        )
    }

}
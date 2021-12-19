import React, {Component} from 'react';

export default class About extends Component {
    constructor(props){
        super(props);
    }

    componentWillMount(){
        document.body.dataset.body_type = 'alt2'
    }

    render(){
        return (
        <section id="About">
            <div className="heading_ctnr">
                <p>
                    about us and our app
                </p>
                <h1>
                    Purple Buckets
                </h1>
                <small>
                    A Note-Taking App
                </small>
            </div>
            <div className="general_text_ctnr">
                <p>
                    <span>
                        What is a bucket?
                    </span>
                A bucket is just a collection
                of data. It's meant to be
                    <span>
                        structureless       
                    </span>                
                        and
                    <span>
                        versatile,
                    </span>
                so that a bucket can be a
                novelists book in progress or a programmers
                project outline. 
                </p>
            </div>
            <div className='general_text_ctnr about_builder'>
                <p>
                    <span>
                        Who is the coder?
                    </span>
                Alexander Barrera. Frontend dev. Backend dev. Database manager.
                    <span>
                    Pretty much a coding coder.
                    </span>
                Here am I, in the flesh.
                </p>
            </div>
            <div className='general_text_ctnr about_builder'>
                <p>
                    <span>
                        Can we see the github?
                    </span>
                    Yes indeed! Please fork it and contribute :)
                </p>
            </div>
        </section>
        )
    }

}
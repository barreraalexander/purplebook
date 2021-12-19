import React, {Component} from 'react';
import { ReactComponent as Img1 } from '../../static/images/assets/create_a_bucket.svg'


export default class Explanation1 extends Component{

    render(){
        return (
            <section id="Explanation1">
                <p>
                <span>
                    What is a bucket?
                </span>
                A bucket is just a collection of data. It's meant to be
                <span>
                     structureless 
                </span>
                and
                <span>
                     versatile 
                </span>
                , so that a bucket can be a novelists book-in-progress or a programmers project outline.
                </p>
                <Img1 />
            </section>
        )
    }

}
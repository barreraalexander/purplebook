import React, {Component} from 'react';
import { ReactComponent as Img1 } from '../../static/images/assets/pouring_bucket.svg'


export default class Explanation2 extends Component{
    constructor(props){
        super(props);
    }
    render(){
        return (
            <section id="Explanation2">
                <div className="instruction_ctnr">
                    <p className="circled_number">
                        1
                    </p>
                    <div className="instruction">
                        <small>
                            CREATE BUCKET
                        </small>
                    </div>
                </div>
                <div className="instruction_ctnr">
                    <p className="circled_number">
                        2
                    </p>
                    <div className="instruction">
                        <small>
                            CREATE SECTION
                        </small>
                    </div>
                </div>
                <div className="instruction_ctnr">
                    <p className="circled_number">
                        3
                    </p>
                    <div className="instruction">
                        <small>
                            CREATE PAGE
                        </small>
                    </div>
                </div>
                <Img1 />
            </section>
        )
    }

}
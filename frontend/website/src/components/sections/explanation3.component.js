import React, {Component} from 'react';
import { ReactComponent as Img1 } from '../../static/images/assets/assign_variables.svg'


export default class Explanation2 extends Component{
    constructor(props){
        super(props);
    }
    render(){
        return (
            <section id="Explanation3">
                <div className="instruction">
                    <p>
                        project_name = Rise Up
                    </p>
                    <p>
                        protagonist = Alexander
                    </p>
                    <p>
                        " My name is [protagonist] and this project is called [project_name] "
                    </p>
                </div>
                <Img1 />
            </section>
        )
    }

}
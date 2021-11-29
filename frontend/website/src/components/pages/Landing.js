import React from "react";

import Explanation1 from './../sections/explanation1.component';
import Explanation2 from './../sections/explanation2.component';
import Explanation3 from './../sections/explanation3.component';
import CallToAction from './../sections/call_to_action.component';


let explanation1 = " hey this is it"

const Landing = () => (
    <section id="Landing">
        <div className="heading_ctnr">
            <p>
                Welcome To
            </p>
            <h1>
                Purple Buckets
            </h1>
            <small>
                Prettify the Mayhem
            </small>
        </div>
        <Explanation1 />
        <Explanation2 />
        <Explanation3 />
        <CallToAction />
    </section>
);

export default Landing;
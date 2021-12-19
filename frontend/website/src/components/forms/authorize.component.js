import React, {Component} from 'react';
import axios from 'axios'

export default class AuthorizeForm extends Component{
    constructor(props){
        super(props);
        this.onChangeName = this.onChangeName.bind(this)
        this.onChangeEmail = this.onChangeEmail.bind(this)
        this.onChangePassword = this.onChangePassword.bind(this)
        this.onChangeCheckPassword = this.onChangeCheckPassword.bind(this)
        this.onChangeAction = this.onChangeAction.bind(this)
        this.onSubmit = this.onSubmit.bind(this)
        
        this.state = {
            name : "",
            email : "",
            password : "",
            check_password : "",
            action_type : this.props.action_type,
            login_url : "/auth/login",
            register_url : "/auth/register",
        }
    }



    onChangeName(e){
        this.setState({
            name : e.target.value
        })
    }

    onChangeEmail(e){
        this.setState({
            email : e.target.value
        })
    }

    onChangePassword(e){
        this.setState({
            password : e.target.value
        })
    }

    onChangeCheckPassword(e){
        this.setState({
            check_password : e.target.value
        })
    }

    onChangeAction(e){

        // e.preventDefault()

        let anchor = document.querySelector('#action_change')
        let check_password_input = document.querySelector('#check_password_ctnr')
        let name_input = document.querySelector('#name_ctnr')

        let heading_ctnr1 = document.querySelector('#heading_ctnr1')
        let heading_ctnr2 = document.querySelector('#heading_ctnr2')
        

        if (this.state.action_type=='register'){
            anchor.innerHTML = 'Registering? click here'
            check_password_input.style.display = 'none'
            name_input.style.display = 'none'

            heading_ctnr1.innerHTML = "let's login to"
            heading_ctnr2.innerHTML = "Your Account"
            
            this.setState({
                action_type: 'login'
            })
            
        } else {
            check_password_input.style.display = 'block'
            name_input.style.display = 'block'
            anchor.innerHTML = "Logging in? click here"
            
            heading_ctnr1.innerHTML = "let's create"
            heading_ctnr2.innerHTML = "An Account"

            this.setState({
                action_type: 'register'
            })
        }
    }

    
    onSubmit(e){
        e.preventDefault()

        if (this.state.check_password != this.state.password){
            alert('check pass')
            return
        }


        const new_user = {
            email : this.state.email,
            password : this.state.password,
            
        }

        console.log(new_user)
        if (this.state.action_type==='login'){
            axios.post(this.state.login_url, new_user)
            .then(res => console.log(res.data));
            
        } else if (this.state.action_type==='register'){
            axios.post(this.state.register_url, new_user)
            .then(res => console.log(res.data));

        }

    }



    render(){
        return (
            <section id='authorize_form_section' onSubmit={this.onSubmit}>
                <form onSubmit={this.onSubmit}>
                    <div id='name_ctnr' className='form_group'>
                        <div className='label_ctnr'>
                            <p>
                                Name 
                            </p>
                            <p className='tiny_text'>
                                | what should we call you
                            </p>
                        </div>
                        <input
                            type='text'
                            name='name'
                            onChange={this.onChangeName}
                            value={this.state.name}
                            required
                        />
                    </div>
                    <div id='email_ctnr' className='form_group'>
                        <div className='label_ctnr'>
                            <p>
                                Email 
                            </p>
                            <p className='tiny_text'>
                                | something valid please
                            </p>
                        </div>
                        <input
                            type="text"
                            name="email"
                            onChange={this.onChangeEmail}
                            value={this.state.email}
                            required
                        />
                    </div>
                    <div className='form_group'>
                        <div className='label_ctnr'>
                            <p>
                                Password 
                            </p>
                            <p className='tiny_text'>
                                | shh don't tell anyone
                            </p>
                        </div>
                        <input
                            type="password"
                            name="password"
                            onChange={this.onChangePassword}
                            value={this.state.password}
                            required
                        />
                    </div>
                    <div id='check_password_ctnr' className='form_group'>
                        <div className='label_ctnr'>
                            <p>
                                Re-Type Password 
                            </p>
                            <p className='tiny_text'>
                                | just double checking
                            </p>
                        </div>
                        <input
                            id="check_password"
                            type="password"
                            name="check_password"
                            onChange={this.onChangeCheckPassword}
                            value={this.state.check_password}
                            required
                        />
                    </div>
                    <div id="error_message_ctnr">
                        <p>
                            
                        </p>
                    </div>
                    <div className='form_group'>
                        <input
                            type="submit"
                            name="auth_submt"
                            value="submit"
                        />
                    </div>
                    <a id="action_change" onClick={this.onChangeAction}>
                        Logging in? click here
                    </a>
                </form>
            </section>
        )
    }

}
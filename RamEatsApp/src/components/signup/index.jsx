import './index.scss'
import logo from '../../assets/RamEatsLogo.svg'

const Signup = () => {
    return (
        <>
            <div className='login-page'>
                <ul>
                    <img src={logo} alt='Logo' height={'50px'}/> 
                    <h1>RamEats</h1> 
                    <form> {/** action defines location to send data method describes http method to use */}
                        <label for='name'>Name</label> <br/>
                        <input type='name' id='name' name='name' required minLength={'1'} maxLength={'20'} /> <br/>
                        <label for='email'>Email</label> <br/>
                        <input type='email' name='email' id='email' required /> <br/>
                        <label for='password'>Password</label> <br/>
                        <input type='password' name='password' id='password' required /> <br/>
                        <label for='confirm_password'>Re-Enter Password</label> <br/>
                        <input type='password' name='confirm_password' id='confirm_password' required /> <br/>
                        <button className='login'>Sign Up</button>
                    </form>
                </ul>

                <p>Back to <a className='bottom-link'>login</a></p>
            </div>
        </>
    );
}

export default Signup
import './index.scss'
import logo from '../../assets/RamEatsLogo.svg'

const Login = () => {
    return (
        <>
            <div className='login-page'>
                <ul>
                    <img src={logo} alt='Logo' height={'50px'}/> 
                    <h1>RamEats</h1> 
                    <form> {/** action defines location to send data method describes http method to use */}
                        <label for='email'>Email</label> <br/>
                        <input type='email' name='email' id='email' required /> <br/>
                        <label for='password'>Password</label> <br/>
                        <input type='password' name='password' id='password' required /> <br/>
                        <button className='login'>Login</button>
                        <a className='newPass'>Forgot password?</a>
                    </form>
                </ul>

                <p>Don't have an account? <a className='signUp'>Sign Up</a></p>
            </div>
        </>
    );
}

export default Login
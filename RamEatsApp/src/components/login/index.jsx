import './index.scss'
import logo from '../../assets/RamEatsLogo.svg'

const Login = () => {
    return (
        <>
            <img src={logo} alt='Logo' height={'50px'}/>
            <h1>RamEats</h1>
            <form> {/** action defines location to send data method describes http method to use */}
                <label for='email'>Email:</label>
                <input type='email' name='email' id='email' required />
                <label for='password'>Password:</label>
                <input type='password' name='password' id='password' required />
                <input type='submit' value='Login'/>
            </form>
        </>
    );
}

export default Login
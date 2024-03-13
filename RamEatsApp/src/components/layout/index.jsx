import { Outlet } from 'react-router-dom'
import './index.scss'
import Navbar from '../navbar'

const Layout = () => {
    return (
        <div className='App'>
            <Outlet />
            <Navbar />
        </div>
    )
}

export default Layout
import './App.scss'
import { Routes, Route } from 'react-router-dom'
import Login from './components/login'
import Layout from './components/layout'
import Home from './components/home'
import Signup from './components/signup'

function App() {
  

  return (
    <>
      <Routes>
        <Route path='/login' element={<Login />} />
        <Route path='/signup' element={<Signup />} />
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
        </Route>
      </Routes>
    </>
  )
}

export default App

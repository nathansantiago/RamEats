import './App.scss'
import { Routes, Route } from 'react-router-dom'

function App() {
  

  return (
    <>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
        </Route>
      </Routes>
    </>
  )
}

export default App

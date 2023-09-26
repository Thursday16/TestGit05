import Signin from './page/Signin';
import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Signup from './page/Signup';
import Home from './page/Home';
import Createproduct from './page/Createproduct';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path={'/signin'} element={<Signin />} />
        <Route path={'/signup'} element={<Signup />} />
        <Route path={'/home'} element={<Home />} />
        <Route path={'/createproduct'} element={<Createproduct />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;

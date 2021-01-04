import './App.css';
import Hero from './components/Hero';
import { BrowserRouter as Router, Link, Route } from 'react-router-dom';
import NewsDash from './components/NewsDash';
function App() {
  return (
    <Router>
      <div className="App">
        <Link to="/" style={{textDecoration:'none'}} >
        <div className="navbar">
          <div className="logo">
          <img src="./images/icon.png" alt="" width="20%"/>
                    <h5>BugsBee</h5>
          </div>
        </div>
        </Link>
        <Route path="/" exact component={Hero} />
        <Route path="/news" exact component={NewsDash} />
      </div>
    </Router>
  );
}

export default App;

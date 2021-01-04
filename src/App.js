import './App.css';
import Hero from './components/Hero';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import NewsDash from './components/NewsDash';
function App() {
  return (
    <Router>
      <div className="App">
        <Route path="/" exact component={Hero} />
        <Route path="/news" exact component={NewsDash} />
      </div>
    </Router>
  );
}

export default App;

import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import UserRegistration from './components/UserRegistration';
import UserLogin from './components/UserLogin';
import AdminLogin from './components/AdminLogin';
import Cart from './components/Cart';
import MessageSection from './components/MessageSection';
import AdminDashboard from './components/AdminDashboard';
import ProductList from './components/ProductList';

const App = () => {
  return (
    <Router>
      <div>
        <Switch>
          <Route path="/register" component={UserRegistration} />
          <Route path="/login" component={UserLogin} />
          <Route path="/adminlogin" component={AdminLogin} />
          <Route path="/cart" component={Cart} />
          <Route path="/ProductList" component={ProductList} />
          <Route path="/messages" component={MessageSection} />
          <Route path="/admindashboard" component={AdminDashboard} />
        </Switch>
      </div>
    </Router>
  );
};

export default App;

import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import UserRegistration from './components/UserRegistration';
import UserLogin from './components/UserLogin';
import AdminLogin from './components/AdminLogin';
import Cart from './components/Cart';
import MessageSection from './components/MessageSection';
import AdminDashboard from './components/AdminDashboard';

const App = () => {
  return (
    <Router>
      <div>
        <Switch>
          <Route path="/register" component={UserRegistration} />
          <Route path="/login" component={UserLogin} />
          <Route path="/admin-login" component={AdminLogin} />
          <Route path="/cart" component={Cart} />
          <Route path="/messages" component={MessageSection} />
          <Route path="/admin-dashboard" component={AdminDashboard} />
        </Switch>
      </div>
    </Router>
  );
};

export default App;

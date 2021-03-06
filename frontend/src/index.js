import React from 'react';
import ReactDOM from 'react-dom';

/* Added by JIMMY */ 
import createHistory from 'history/createBrowserHistory'
import { ConnectedRouter } from 'react-router-redux'
import { Provider } from 'react-redux'
/* Added by JIMMY */ 

import './index.css';
import 'bootstrap/dist/css/bootstrap.css'; 	// Added By Jimmy
import App from './App';
import registerServiceWorker from './registerServiceWorker';

import configureStore from './store'	// Added By Jimmy

import {Route, Switch} from 'react-router'
import Login from './containers/Login';
import PrivateRoute from './containers/PrivateRoute';

//ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();

const history = createHistory()
const store = configureStore(history)
ReactDOM.render((
  <Provider store={store}>
    <ConnectedRouter history={history}>
      <Switch>
        <Route exact path="/login/" component={Login} />
        <PrivateRoute path="/" component={App}/>
      </Switch>
    </ConnectedRouter>
  </Provider>
), document.getElementById('root'));
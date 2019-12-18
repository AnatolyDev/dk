import React from 'react';
import { Route, Switch } from 'react-router-dom';

import Home from '../Home';
import SignIn from '../../containers/SignIn';
import Dashboard from '../../containers/Dashboard';
import NotFound from '../NotFound';

const Main = () => {
    return (
        <>
            <Switch>
                <Route path='/' exact component={Home} />
                <Route path='/signin' component={SignIn} />
                <Route path='/dashboard' component={Dashboard} />
                <Route component={NotFound} />
            </Switch>
        </>
    )
}

export default Main;
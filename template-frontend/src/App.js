import React, { Component } from 'react';

import { BrowserRouter as Router, Route } from "react-router-dom";

import Book from "./Components/Book/index";

class App extends Component {
  render() {
    return (
      <Router>
        <Route path="/" exact component={Book} />
      </Router>
    );
  }
}

export default App;

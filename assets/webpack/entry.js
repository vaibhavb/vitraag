import React, { Component } from 'react';
import {render} from 'react-dom';
import FileReader from './FileReader'

class App extends Component {
  render() {
    return (<FileReader/>)
  }
}
render(<App />, document.getElementById('react'));
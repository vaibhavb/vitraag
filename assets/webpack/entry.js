import React, { Component } from 'react';
import {render} from 'react-dom';
import Transactions from './Transactions';

var transaction_data = [{
  "Date": "2/12/2021", 
  "Description": "CODAME, LLC",
  "Original Description": "CODAME, LLC",
  "Amount": "30.00",
  "Transaction Type": "debit",
  "Category": "Restaurants",
  "Account Name": "CREDIT CARD",
  "Labels": "",
  "Notes": ""
}];

class App extends Component {
  render() {
    this.state = {}
    this.state.data = transaction_data;
    return (<Transactions title="List of Transactions" data={this.state.data}/>)
  }
}
render(<App />, document.getElementById('react'));
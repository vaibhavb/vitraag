import React, {Component} from 'react';
import Transactions from './Transactions';
import Papa from 'papaparse';

class FileReader extends React.Component {
  constructor(props){
    super();
    this.state = {
      csvfile: undefined,
      data: []
    };
    this.updateData = this.updateData.bind(this);
  };

  handleChange = () => {
    this.setState({
      csvfile: event.target.files[0]
    });
  };

  importCSV = () => {
    const { csvfile } = this.state;
    Papa.parse(csvfile, {
      complete: this.updateData,
      header: true
    });
  };

  updateData(result) {
    var data = result.data;
    this.setState({data: data});
    console.log(data[0]);
  }

  render() {
    return (
      <div className="App">
        <br/>
        <div className="container">
        <div className="hero is-info">React App is working!</div>
        <h2>Import CSV File!</h2>
        <input
          className="csv-input"
          type="file"
          ref={input => {
            this.filesInput = input;
          }}
          name="file"
          placeholder={null}
          onChange={this.handleChange}
        />
        <p />
        <button onClick={this.importCSV}> Upload now!</button>
      </div>
      <br/>
        <Transactions title="List of Transactions" data={this.state.data}/>
      </div>
    );
  }
}
  
export default FileReader;
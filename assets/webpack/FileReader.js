import React, {Component} from 'react';

class FileReader extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      counter: 1
    };
  };
  handleChange = () => {
    console.log("File is being uploaded");
    this.setState((prevState) => ({  counter: prevState.counter + 1 }));
  };
  render() {
    return (
      <div className="App">
        <div class="container">
        <div class="hero is-info">React App is working!</div>
        <h2>Import CSV File - {this.state.counter} !</h2>
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
      </div>
    );
  }
}
  
  export default FileReader;
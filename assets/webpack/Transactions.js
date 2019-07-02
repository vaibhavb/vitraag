import React, {Component} from 'react';

class Transactions extends React.Component{
    render(){
        return(
        <div>
            <div>{this.props.title}</div>
            {this.props.data ? (<p>{this.props.data[0]}</p>): (<span></span>)}
        </div>
        )
    }
}

export default Transactions;
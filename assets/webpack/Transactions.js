import React, {Component} from 'react';

class Transactions extends React.Component{
    render(){
        return(
        <div class="column">
            <div class="title is-6">{this.props.title}</div>
            {this.props.data ? (<p><span>{this.props.data[0].Date}</span> 
                <span>: {this.props.data[0].Description}</span>
                <span>: ${this.props.data[0].Amount}</span>
                <span>: {this.props.data[0]['Account Name']}</span>
            </p>): (<span></span>)}
        </div>
        )
    }
}

export default Transactions;
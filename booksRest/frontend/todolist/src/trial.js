import React,{Component} from "react";

class TrialComponents extends Component{
    constructor(props){
        super(props)
        this.state=({
            message:'empty'
        })
    }
    Handler =(event)=>{
        this.setState({
            message:'this is the best'
        })
    }

    render(){
        return(
            <div>

            </div>
        )
    }
}
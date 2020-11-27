import React from "react";
import {withStyles} from "@material-ui/core/styles";
import fetchWebsites from "../api/fetchWebsites";


const styles = () => ({
    screen: {
        width: "15%",
        height: "250px"
    },
    secondButton: {
        margin: '10px',
        padding: '20px',
        alignItems: 'center',
        backgroundColor: 'lightblue'
    }
});

class NewComp extends React.Component {
    constructor(props) {
        super(props);
        this.state = {dataIsReturned: false, websites: []};
    }

    componentDidMount() {
        fetch('http://celery-manager-content-aggregator.192.168.5.60.nip.io/website_names/', {
            method: 'GET', // *GET, POST, PUT, DELETE, etc.
            mode: 'cors', // no-cors, *cors, same-origin
            headers: {
                'Content-Type': 'application/json'
                // 'Content-Type': 'application/x-www-form-urlencoded',
            },}).then(async (data) => {
                this.setState({dataIsReturned: true, websites: await data.json()})})
                    .catch(err => console.error(err));
}

render()
{
    return (this.state.dataIsReturned ? this.state.websites.map((website) =><h1>{website}</h1>)
        : <h1> Loading </h1>)
}
}
export default withStyles(styles)(NewComp);
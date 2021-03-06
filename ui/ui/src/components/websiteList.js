import React from "react";
import {withStyles} from "@material-ui/core/styles";
import ListItemIcon from "@material-ui/core/ListItemIcon";
import HttpIcon from "@material-ui/icons/Http";
import ListItemText from "@material-ui/core/ListItemText";
import ListItem from "@material-ui/core/ListItem";


const styles = () => ({
});

class WebsiteList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {dataIsReturned: false, websites: []};
    }

    componentDidMount() {
        fetch(process.env.CELERY+'website_names/', {
            method: 'GET',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
            },}).then(async (data) => {
                this.setState({dataIsReturned: true, websites: await data.json()})})
                    .catch(err => console.error(err));
}

render()
{
    return (this.state.dataIsReturned ? this.state.websites.map((website) =><ListItem button>
            <ListItemIcon>
                <HttpIcon/>
            </ListItemIcon>
            <ListItemText primary={website}/>
        </ListItem>)
        : <h1> Loading </h1>)
}
}
export default withStyles(styles)(WebsiteList);
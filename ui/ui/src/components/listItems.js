import React from 'react';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import HttpIcon from '@material-ui/icons/Http';
import fetchWebsites from "../api/fetchWebsites";
import { withStyles } from "@material-ui/core/styles";

const styles = () => ({
    screen: {
        width: "15%",
        height:"250px"
    },
    secondButton:{
        margin:'10px',
        padding:'20px',
        alignItems:'center',
        backgroundColor:'lightblue'
    }
});


class mainListItems extends React.Component {
    constructor(props) {
        super(props);
        this.state = {value: ''};
    }

    render() {
        return (<div>
            <ListItem button>
                <ListItemIcon>
                    <HttpIcon/>
                </ListItemIcon>
                <ListItemText Dashboard/>
            </ListItem>
            <ListItem button>
                <ListItemIcon>
                    <HttpIcon/>
                </ListItemIcon>
                <ListItemText Orders/>
            </ListItem>
        </div>)
    }
}

export default withStyles(styles)(mainListItems);
import React from 'react';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import HttpIcon from '@material-ui/icons/Http';

async function postData(url = '', data = {}) {
    return await fetch('http://celery-manager-content-aggregator.192.168.5.60.nip.io/website_names')
        .then(response => response.json())
        .then(data => console.log(data));
}
export const mainListItems = (
    <div>
        <ListItem button>
            <ListItemIcon>
                <HttpIcon />
            </ListItemIcon>
            <ListItemText primary="Dashboard" />
        </ListItem>
        <ListItem button>
            <ListItemIcon>
                <HttpIcon />
            </ListItemIcon>
            <ListItemText primary="Orders" />
        </ListItem>
        <h1>{postData()}</h1>
    </div>

);
import React from 'react';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import HttpIcon from '@material-ui/icons/Http';

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
    </div>
);
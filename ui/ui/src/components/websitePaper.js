import {withStyles} from "@material-ui/core/styles";
import React from "react";
import Paper from '@material-ui/core/Paper';
import clsx from "clsx";

const styles = (theme) => ({
    fixedHeight: {
        height: 240,
    },
    paper: {
        padding: theme.spacing(2),
        display: 'flex',
        overflow: 'auto',
        flexDirection: 'column',
    },
});

class WebsitePaper extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            dataIsReturned: false,
            website: {
                websiteName: '',
                mainHeadline: {
                    text: '',
                    url: ''
                },
                minorHeadlines: []
            }
        };
    }

    componentDidMount() {
        fetch(process.env.CELERY+'/website/'
            +this.props.websiteName, {
            method: 'GET',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
            },
        }).then(async (data) => {
            const websiteData = await data.json()
            this.setState({
                dataIsReturned: true,
                website: {
                    websiteName: websiteData['website'],
                    mainHeadline:{
                        text:websiteData['main_headline']['text'],
                        url:websiteData['main_headline']['url']
                    },
                    minorHeadlines: websiteData['minor_headlines']
                }
            })
        })
            .catch(err => console.error(err));
    }

    render() {
        const {classes} = this.props;
        const fixedHeightPaper = clsx(classes.paper, classes.fixedHeight);
        return (this.state.dataIsReturned ? <Paper className={fixedHeightPaper}>
                <b>Website:</b> {this.state.website.websiteName}
                <b>Major Headline:</b>
                <a href={this.state.website.mainHeadline.url}>{this.state.website.mainHeadline.text}</a>
                <b>Minor Headlines:</b>{this.state.website.minorHeadlines.map((data) => <h2>{data}</h2>)}

        </Paper>
            : <h1> Loading </h1>)
    }
}

export default withStyles(styles)(WebsitePaper);
import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

const bull = (
    <Box
        component="span"
        sx={{ display: 'inline-block', mx: '2px', transform: 'scale(0.8)' }}
    >
        •
    </Box>
);


export default function OutlinedCard(props) {
    return (
        <Box sx={{ minWidth: 275, p: 2 }} >

            <Card variant="outlined">
                <React.Fragment>
                    <CardContent>
                        <Typography gutterBottom variant="h5" component="div">
                            {props.title}
                        </Typography>
                        <Typography gutterBottom variant="h5" component="div">
                            Slug:  {props.slug}
                        </Typography>
                        <Typography gutterBottom variant="h5" component="div">
                            Company : {props.company_name}
                        </Typography>
                        <Typography gutterBottom variant="h5" component="div">
                            Location : {props.location}
                        </Typography>
                        <Typography variant="body2" color="text.secondary">
                            Location : {props.location}
                        </Typography>
                        <Typography variant="body2" color="text.secondary">
                            {props.description}
                        </Typography>


                    </CardContent>
                    <CardActions>
                        {props.description ? (
                            <Button size="small" onClick={props.onClick} >Back</Button>

                        ) : (
                            <Button size="small" onClick={props.onClick} id={props.id}>More Details</Button>

                        )

                        }
                        <Button size="small">Apply </Button>
                    </CardActions>
                </React.Fragment>
            </Card>
        </Box>
    );
}

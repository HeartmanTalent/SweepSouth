import React, { useEffect, useState } from 'react';
import { styled, alpha } from '@mui/material/styles';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import InputBase from '@mui/material/InputBase';
import SearchIcon from '@mui/icons-material/Search';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import axios from 'axios';
import OutlinedCard from './OutlinedCard';
import CssBaseline from '@mui/material/CssBaseline';
import Container from '@mui/material/Container';

const Search = styled('div')(({ theme }) => ({
    position: 'relative',
    borderRadius: theme.shape.borderRadius,
    backgroundColor: alpha(theme.palette.common.white, 0.15),
    '&:hover': {
        backgroundColor: alpha(theme.palette.common.white, 0.25),
    },
    marginLeft: 0,
    width: '100%',
    [theme.breakpoints.up('sm')]: {
        marginLeft: theme.spacing(1),
        width: 'auto',
    },
}));

const SearchIconWrapper = styled('div')(({ theme }) => ({
    padding: theme.spacing(0, 2),
    height: '100%',
    position: 'absolute',
    pointerEvents: 'none',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
}));

const StyledInputBase = styled(InputBase)(({ theme }) => ({
    color: 'inherit',
    '& .MuiInputBase-input': {
        padding: theme.spacing(1, 1, 1, 0),
        // vertical padding + font size from searchIcon
        paddingLeft: `calc(1em + ${theme.spacing(4)})`,
        transition: theme.transitions.create('width'),
        width: '100%',
        [theme.breakpoints.up('sm')]: {
            width: '12ch',
            '&:focus': {
                width: '20ch',
            },
        },
    },
}));

export default function Home() {
    const [parameter, setParameter] = React.useState('');
    const [query, setQuery] = React.useState('');
    const [jobs, setJobs] = React.useState([])
    const [job, setJob] = React.useState({})
    const [single, setSingle] = React.useState(false)
    const [loading, setLoading] = useState(true);

    const handleParameterChange = (event) => {
        const param = event.target.value
        if (param && query) {
            axios.get('/api/jobs/?' + param + '=' + query, { "Access-Control-Allow-Origin": "*" })
                .then((response) => {
                    setJobs(response.data);
                    setParameter(param);
                }, [])
                .catch((error) => {
                    console.error(error.message);

                })
        } else {
            axios.get('/api/jobs/', { "Access-Control-Allow-Origin": "*" })
                .then((response) => {
                    setJobs(response.data);
                    setSingle(false);
                    setParameter(param);
                }, [])
                .catch((error) => {
                    console.error(error.message);

                })
        }

    };

    const handleQueryChange = (event) => {
        const qry = event.target.value
        if (qry) {
            axios.get('/api/jobs/?' + parameter + '=' + qry, { "Access-Control-Allow-Origin": "*" })
                .then((response) => {
                    setJobs(response.data);
                    setQuery(qry);
                }, [])
                .catch((error) => {
                    console.error(error.message);

                })
        } else {
            axios.get('/api/jobs/', { "Access-Control-Allow-Origin": "*" })
                .then((response) => {
                    setJobs(response.data);
                    setSingle(false);
                    setQuery(qry);
                }, [])
                .catch((error) => {
                    console.error(error.message);

                })
        }

    };

    const handleJobChange = (event) => {
        const id = event.currentTarget.getAttribute("id")
        axios.get('/api/jobs/' + id, { "Access-Control-Allow-Origin": "*" })
            .then((response) => {
                setJob(response.data);
                setSingle(true);
            }, [])
            .catch((error) => {
                console.error(error.message);

            })
    };

    const cancelJobChange = (event) => {
        setSingle(false);
        setJob({});
    };
    useEffect(() => {
        const fetchData = async () => {
            setLoading(true);
            try {
                const { data: response } = await axios.get('/api/jobs',
                    { "Access-Control-Allow-Origin": "*" });
                setJobs(response);
            } catch (error) {
                console.error(error.message);
            }
            setLoading(false);
        }

        fetchData();
    }, []);

    return (
        <>
            <Box sx={{ flexGrow: 1 }}>
                <AppBar position="static">
                    <Toolbar sx={{ pt: 2, pb: 2 }}>
                        <Box sx={{ minWidth: 120 }}>
                            <FormControl fullWidth >
                                <InputLabel id="demo-simple-select-label" sx={{ color: 'white'}}>Parameter</InputLabel>
                                <Select
                                    sx={{ color: 'white' }}
                                    labelId="demo-simple-select-label"
                                    id="demo-simple-select"
                                    value={parameter}
                                    label="Parameter"
                                    onChange={handleParameterChange}
                                >
                                    <MenuItem value={"type"}>Type</MenuItem>
                                    <MenuItem value={"tag"}>Tag</MenuItem>
                                    <MenuItem value={"title"}>Title</MenuItem>
                                    <MenuItem value={"location"}>Location</MenuItem>
                                    <MenuItem value={"company"}>Company</MenuItem>
                                </Select>
                            </FormControl>
                        </Box>
                        <Search>
                            <SearchIconWrapper>
                                <SearchIcon />
                            </SearchIconWrapper>
                            <StyledInputBase
                                placeholder="Search…"
                                inputProps={{ 'aria-label': 'search' }}
                                value={query}
                                onChange={handleQueryChange}
                            />
                        </Search>
                        {/* <Typography
                        variant="h6"
                        noWrap
                        component="div"
                        sx={{ flexGrow: 1, display: { xs: 'none', sm: 'block' } }}
                    >
                        Jobs
                    </Typography> */}

                    </Toolbar>
                </AppBar>
            </Box>
            <React.Fragment>
                <CssBaseline />
                <Container fixed>
                    {loading && <div>Loading</div>}
                    {(!loading && !single) && (
                        <div >
                            <h2>Jobs ({Object.keys(jobs).length}) </h2>
                            {jobs.map(item => (
                                <OutlinedCard key={item.id}
                                    onClick={handleJobChange}
                                    id={item.id}
                                    title={item.title}
                                    slug={item.slug}
                                    company_name={item.company_name}
                                    location={item.location}
                                    url={item.url} />
                            ))}
                        </div>
                    )}
                    {(job && single) && (
                        <OutlinedCard key={job.id}
                            title={job.title}
                            description={job.description}
                            slug={job.slug}
                            company_name={job.company_name}
                            location={job.location}
                            url={job.url}
                            onClick={cancelJobChange}

                        />
                    )}

                </Container>
            </React.Fragment>
        </>
    );
}


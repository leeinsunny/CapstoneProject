import React, { useState, useEffect } from "react";
import axios from "axios";
import styled from "styled-components";
import { Outlet } from "react-router-dom";

const Container = styled.div`
    display: flex;
    justify-content: start;
    flex-direction: column;
    align-items: center;
    height: 100vh;
`;

const Filter = () => {
    const [data, setData] = useState(null);

    useEffect(() => {
        // TODO: Match backend connection structure
        const apiUrl = "/filter";

        axios
            .get(apiUrl)
            .then((response) => {
                setData(response.data);
                console.log("Fetched data from backend server:", response.data);
            })
            .catch((error) => {
                console.error("Cannot fetch data from backend server", error);
            });
    }, []);

    return (
        <Container>
            <Outlet />
        </Container>
    );
};

export default Filter;

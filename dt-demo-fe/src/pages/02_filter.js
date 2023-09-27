import React from "react";
import { Outlet } from "react-router-dom";
import styled from "styled-components";

const MainContainer = styled.div`
    display: flex;
    height: 100vh;
    align-items: start;
    justify-content: center;
    margin-top: 40px;
`;

const Filter = () => {
    return (
        <MainContainer>
            <Outlet />
        </MainContainer>
    );
};

export default Filter;

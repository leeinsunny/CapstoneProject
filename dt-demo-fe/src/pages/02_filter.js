import React from "react";
import { Outlet } from "react-router-dom";
import styled from "styled-components";

const MainContainer = styled.div`
    display: flex;
    width: 100vw;
    height: 100vh;
    align-items: center;
    justify-content: center;
`;

const Filter = () => {
    return (
        <MainContainer>
            <Outlet />
        </MainContainer>
    );
};

export default Filter;

import React from "react";
import styled from "styled-components";
import FileListContainer from "./filtering/filelist";
import RulesContainer from "./filtering/rules";

const Container = styled.div`
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    height: 100vh;
    width: 100%;
`;

const Filter = () => {
    return (
        <Container>
            <FileListContainer />
            <RulesContainer />
        </Container>
    );
};

export default Filter;

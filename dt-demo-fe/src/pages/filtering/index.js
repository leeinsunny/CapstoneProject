import React from "react";
import styled from "styled-components";
import FileListContainer from "./filelist";
import RulesContainer from "./rules";

const Container = styled.div`
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
`;

const FilterMain = () => {
    return (
        <Container>
            <FileListContainer />
            <RulesContainer />
        </Container>
    );
};

export default FilterMain;

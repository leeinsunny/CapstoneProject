import React from "react";
import { Button } from "antd";
import styled from "styled-components";
import { useNavigate } from "react-router-dom";

const Container = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
`;

const RulesBox = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border: 1px solid black;
    height: 300px;
    width: 400px;
    margin-top: 50px;
`;

const DemoRules = () => {
    const navigate = useNavigate();

    return (
        <Container>
            <RulesBox>
                <div>check box for rule settings will be implemented</div>
            </RulesBox>
            <Button
                style={{
                    backgroundColor: "#212653",
                    color: "white",
                    marginTop: "30px",
                }}
                onClick={() => {
                    navigate("/filter/report");
                }}
            >
                Start Filtering
            </Button>
        </Container>
    );
};

export default DemoRules;

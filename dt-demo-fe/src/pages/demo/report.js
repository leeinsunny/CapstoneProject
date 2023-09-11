import React from "react";
import styled from "styled-components";
import { Button } from "antd";

const Container = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
`;

const ReportBox = styled.div`
    display: flex;
    flex-direction: column;
    border: 1px solid black;
    padding: 20px;
`;

const DemoReport = () => {
    const handleExportButton = () => {
        console.log("export button clicked");
        alert("export button clicked");
    };

    return (
        <Container>
            <ReportBox>this is DemoReport</ReportBox>
            <Button
                style={{
                    marginTop: "30px",
                    backgroundColor: "#212653",
                    color: "white",
                }}
                onClick={handleExportButton}
            >
                Export
            </Button>
        </Container>
    );
};

export default DemoReport;

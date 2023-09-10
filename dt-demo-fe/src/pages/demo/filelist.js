import React, { useState } from "react";
import styled from "styled-components";
import { useNavigate } from "react-router-dom";
import { List, Button } from "antd";

const Container = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 600px;
    width: 100vw;
`;

const FileListWrapper = styled.div`
    display: flex;
    flex-direction: column;
    width: 500px;
    border: 1px solid black;
`;

const DemoFileList = () => {
    const navigate = useNavigate();
    const files = ["file1", "file2", "file3", "file4", "file5"];
    const [fileList, setFileList] = useState(files);

    return (
        <Container>
            <FileListWrapper>
                <List
                    header={<div>Uploaded File List</div>}
                    // footer={<div>Footer</div>}
                    bordered
                    dataSource={fileList}
                    renderItem={(item) => <List.Item>{item}</List.Item>}
                />
            </FileListWrapper>
            <Button
                style={{
                    backgroundColor: "#212653",
                    color: "white",
                    marginTop: "20px",
                    width: "100px",
                }}
                onClick={() => {
                    navigate("/filter/rules");
                }}
            >
                Set Filter
            </Button>
        </Container>
    );
};

export default DemoFileList;

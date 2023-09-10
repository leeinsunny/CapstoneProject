import styled from "styled-components";
import { Button } from "antd";
import { useNavigate } from "react-router-dom";

const Wrapper = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 500px;
    width: 100vw;
    .uploadBtn {
        width: 100px;
        height: 50px;
        cursor: pointer;
    }
`;

const DemoUpload = () => {
    const navigate = useNavigate();

    return (
        <Wrapper>
            <Button
                style={{ backgroundColor: "#212653", color: "white" }}
                onClick={() => {
                    navigate("/filter/filelist");
                }}
            >
                Upload
            </Button>
        </Wrapper>
    );
};

export default DemoUpload;

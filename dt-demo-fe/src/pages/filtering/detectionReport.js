import React, { useEffect, useState } from "react";
import styled from "styled-components";
import { Button } from "antd";
import { useNavigate } from "react-router-dom";
import useApi from "../../hooks/api/axiosInterceptor";
import jsPDF from "jspdf";
import MakePdf from "../../components/report/makePdf";

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
    width: 500px;
    height: 500px;
`;

const BottomContainer = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
`;

const RadioGroup = styled.div`
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    margin-top: 30px;
    width: 500px;
`;

const DetectionContainer = () => {
    const [radioSelected, setRadioSelected] = useState("");
    const navigate = useNavigate();

    const onChange = (e) => {
        setRadioSelected(e.target.value);
    };

    const handleFilteringButton = async (e) => {
        e.preventDefault();

        if (radioSelected === "") {
            alert("필터링 방식을 선택해주세요.");
            return;
        }

        try {
            await useApi.post("/filter/detection/type", {
                type: radioSelected,
            });
            console.log("detection type", radioSelected, " sent successfully");
            navigate("/filter/conversion");
        } catch (err) {
            console.log(err.response);
        }
    };

    useEffect(() => {}, [radioSelected]);

    return (
        <Container>
            <ReportBox>report container</ReportBox>
            <BottomContainer>
                <RadioGroup>
                    <input
                        type="radio"
                        id="word"
                        name="radioOption"
                        value="word"
                        checked={radioSelected === "word"}
                        onChange={onChange}
                    />
                    <label htmlFor="word">단어 변환</label>
                    <input
                        type="radio"
                        id="sent"
                        name="sent"
                        value="sent"
                        checked={radioSelected === "sent"}
                        onChange={onChange}
                    />
                    <label htmlFor="sent">단어가 포함된 문장 전체 제거</label>
                </RadioGroup>
                <Button
                    style={{
                        marginTop: "30px",
                        backgroundColor: "#212653",
                        color: "white",
                    }}
                    onClick={handleFilteringButton}
                >
                    Filter
                </Button>
            </BottomContainer>
        </Container>
    );
};

export default DetectionContainer;

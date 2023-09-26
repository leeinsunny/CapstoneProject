import React, { useEffect, useRef } from "react";
import styled from "styled-components";
import { Button } from "antd";
import useApi from "../../hooks/api/axiosInterceptor";
import html2canvas from "html2canvas";
import jsPDF from "jspdf";

const Container = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
`;

const ReportBox = styled.div`
    display: flex;
    flex-direction: column;
    padding: 10px;
    width: 800px;
    height: 500px;
    border: 1px solid black;
`;

const BottomContainer = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
`;

const ConversionContainer = () => {
    const pdfRef = useRef();


    const handleExportButton = async (e) => {
        console.log("handleExportButton clikced");

        e.preventDefault();
    };

    const htmlStringToPdf = async (htmlString, pdfRef) => {
        let iframe = document.createElement("iframe");
        iframe.style.visibility = "hidden";
        document.body.appendChild(iframe);
        let iframedoc = iframe.contentDocument || iframe.contentWindow.document;
        iframedoc.body.innerHTML = htmlString;

        let canvas = await html2canvas(iframedoc.body, {
            windowWidth: 800,
        });
        let imgData = canvas.toDataURL("image/png");

        const doc = new jsPDF({
            format: "a4",
            unit: "mm",
        });

        const pageWidth = doc.internal.pageSize.getWidth();
        const pageHeight = doc.internal.pageSize.getHeight();

        const widthRatio = pageWidth / canvas.width;
        const customHeight = canvas.height * widthRatio;

        doc.addImage(imgData, "png", 0, 0, pageWidth, customHeight);

        let heightLeft = customHeight;
        let heightAdd = -pageHeight;

        // over 1 page
        while (heightLeft >= pageHeight) {
            doc.addPage();
            doc.addImage(imgData, "png", 0, heightAdd, pageWidth, customHeight);
            heightLeft -= pageHeight;
            heightAdd -= pageHeight;
        }

        let pdfBlob = doc.output("blob");
        pdfRef.current.src = URL.createObjectURL(pdfBlob);
    };

    useEffect(() => {
        async function fetchData() {
            try {
                const response = await useApi.get("/filter/convreport");
                const html = response.data;

                htmlStringToPdf(html, pdfRef);
            } catch (error) {
                console.error("Error fetching data", error);
            }
        }
        fetchData();
    }, []);

    return (
        <Container>
            <ReportBox>
                <iframe
                    ref={pdfRef}
                    style={{ width: "100%", height: "100%" }}
                    title="Detection Report Viewer"
                />
            </ReportBox>
            <BottomContainer>
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
            </BottomContainer>
        </Container>
    );
};

export default ConversionContainer;

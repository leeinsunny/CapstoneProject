import React, { useEffect, useRef, useState } from "react";
import { Button } from "antd";
import useApi from "../../hooks/api/axiosInterceptor";

const UploadBtn = () => {
    const [selectedFile, setSelectedFile] = useState(null);
    const [form, setForm] = useState({
        name: "",
        uploadedDate: "",
        status: "",
        filteredDate: "",
    });
    const fileInputRef = useRef();
    const date = new Date();
    const uploadedDate = date.toISOString().slice(0, 10);

    const handleButtonClick = () => {
        fileInputRef.current.click();
    };

    const handleFileUpload = async (e) => {
        e.preventDefault();
        setSelectedFile(e.target.files[0]);

        if (selectedFile === null) {
            console.log("file selection cancelled");
            return;
        }

        var newFormState = {
            ...form,
            file: e.target.files[0],
            name: e.target.files[0]["name"],
            uploadedDate: uploadedDate,
            status: "uploaded",
        };

        console.log("file information was transmitted to server");

        try {
            await useApi.post("/filter/upload", {
                form: newFormState,
            });

            alert("파일 업로드가 완료되었습니다.");
        } catch (err) {
            console.log(err);
        }
    };

    useEffect(() => {
        setSelectedFile((currentValue) => fileInputRef.current.files[0]);

        console.log("selected in useEffect", selectedFile);
    }, [selectedFile]);

    return (
        <>
            <input
                type="file"
                accept=".txt"
                name="file"
                id="file"
                ref={fileInputRef}
                onChange={handleFileUpload}
                style={{ display: "none" }}
            />
            <Button
                style={{ backgroundColor: "#212653", color: "white" }}
                onClick={handleButtonClick}
            >
                Upload
            </Button>
        </>
    );
};

export default UploadBtn;

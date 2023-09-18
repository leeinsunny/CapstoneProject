import React, { useRef, useState } from "react";
import { Button } from "antd";
import useApi from "../../hooks/api/axiosInterceptor";

const UploadBtn = ({ onFileSelect }) => {
    const [selectedFile, setSelectedFile] = useState(null);
    const fileInputRef = useRef(); // Create a reference to the hidden file input element

    var newFormState = {
        name: "",
        uploadedDate: "",
        status: "",
        filteredDate: "",
    };

    const handleButtonClick = () => {
        fileInputRef.current.click();
    };

    const handleFileChange = (event) => {
        setSelectedFile(event.target.files[0]);
        onFileSelect(event.target.files[0]);
    };

    const onSubmit = async () => {
        // TODO: Handle file upload
        try {
            await useApi.post("/api/filter/filelist", {
                form: newFormState,
            });
        } catch (err) {
            console.log(err);
        }
    };

    return (
        <>
            <input
                type="file"
                accept=".txt"
                name="file"
                id="file"
                ref={fileInputRef}
                onChange={onSubmit}
                style={{ display: "none" }}
                multiple
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

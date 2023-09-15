import axios from "axios";

const useApi = axios.create({
    headers: {
        "Content-Type": "application/json;charset=UTF-8",
        "Access-Control-Allow-Origin": "http://localhost:5001",
        "Access-Control-Allow-Credentials": "true",
    },
});

useApi.interceptors.response.use((response) => response);

export default useApi;

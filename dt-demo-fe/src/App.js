import React from "react";
import { Global } from "@emotion/react";
import { reset } from "./styles/reset";
import Router from "./Router";

function App() {
    return (
        <>
            <Global styles={reset} />
            <Router />
        </>
    );
}

export default App;

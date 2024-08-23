import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import ScrollToTop from "./component/scrollToTop";
import { BackendURL } from "./component/backendURL";

import { Home } from "./pages/home";
import { Demo } from "./pages/demo";
import { Single } from "./pages/single";
import { ProviderProfile } from "./pages/providerProfile";
// import { ProviderPlantTypes } from "./pages/providerPlantTypes";
import { ProviderMapPage } from "./pages/providerMapPage";
import injectContext from "./store/appContext";
import { ProviderSignUp } from "./pages/providerSignUp";
import { Navbar } from "./component/navbar";
import { Footer } from "./component/footer";
import { ProviderServices } from "./pages/providerServices";



//create your first component
const Layout = () => {
    //the basename is used when your project is published in a subdirectory and not in the root of the domain
    // you can set the basename on the .env file located at the root of this project, E.g: BASENAME=/react-hello-webapp/
    const basename = process.env.BASENAME || "";

    if(!process.env.BACKEND_URL || process.env.BACKEND_URL == "") return <BackendURL/ >;

    return (
        <div>
            <BrowserRouter basename={basename}>
                <ScrollToTop>
                    <Navbar />
                    <Routes>
                        <Route element={<Home />} path="/" />
                        <Route element={<Demo />} path="/demo" />
                        <Route element={<Single />} path="/single/:theid" />
                        <Route element={<ProviderServices />} path="/provider-services" />
                        <Route element={<ProviderProfile />} path="/provider-profile" />
                        {/* <Route element={<ProviderPlantTypes />} path="/plant-types" /> */}
                        <Route element={<ProviderMapPage />} path="/provider-map" />
                        <Route element={<ProviderSignUp />} path="/provider-signup" />
                        <Route element={<h1>Not found!</h1>} />
                    </Routes>
                    <Footer />
                </ScrollToTop>
            </BrowserRouter>
        </div>
    );
};

export default injectContext(Layout);

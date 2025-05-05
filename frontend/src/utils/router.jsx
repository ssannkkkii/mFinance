import { Routes, Route } from "react-router-dom";
import MainPage from "../pages/MainPage/MainPage";
import AboutUs from "../pages/About/AboutUs";

const AppRouter = () => {
  return (
    <Routes>
      <Route path="/" element={<MainPage />} />
      <Route path="/about" element={<AboutUs />} />
    </Routes>
  );
};

export default AppRouter;

import { Routes, Route } from "react-router-dom";
import MainPage from "../pages/MainPage/MainPage";
import AboutUs from "../pages/About/AboutUs";
import CompleteProfile from "../pages/test/CompleteProfile";
import Profile from "../pages/test/ProfilePage";
import BankCard from "../pages/test/BankCard";
import Transactions from "../pages/test/Transictions";
import Login from "../pages/test/Login";

const AppRouter = () => {
  return (
    <Routes>
      <Route path="/" element={<MainPage />} />
      <Route path="/about" element={<AboutUs />} />
      <Route path="/login" element={<Login></Login>} />
      <Route path="/complete-profile" element={<CompleteProfile />} />
      <Route path="/profile" element={<Profile />} />
      <Route path="/bank-card" element={<BankCard />} />
      <Route path="/transactions" element={<Transactions />} />
    </Routes>
  );
};

export default AppRouter;

import { useState } from "react";
import api from "../../utils/api";

export default function Login() {
  const [phone, setPhone] = useState("");
  const [code, setCode] = useState("");
  const [step, setStep] = useState(1);

  const sendOTP = async () => {
    await api.post("/users/send-otp/", { phone });
    setStep(2);
  };

  const verifyOTP = async () => {
    await api.post("/users/verify-otp/", { phone, code });
    window.location.href = "/profile";
  };

  return (
    <div>
      <h2>Login</h2>
      {step === 1 ? (
        <>
          <input value={phone} onChange={(e) => setPhone(e.target.value)} placeholder="Phone" />
          <button onClick={sendOTP}>Send OTP</button>
        </>
      ) : (
        <>
          <input value={code} onChange={(e) => setCode(e.target.value)} placeholder="Enter OTP" />
          <button onClick={verifyOTP}>Verify OTP</button>
        </>
      )}
    </div>
  );
}

import { useState } from "react";
import api from "../../utils/api";

export default function CompleteProfile() {
  const [first, setFirst] = useState("");
  const [last, setLast] = useState("");

  const complete = async () => {
    const res = await api.post("/users/complete-profile/", { first_name: first, last_name: last });
    alert(res.data.message);
    window.location.href = "/profile";
  };

  return (
    <div>
      <h2>Complete Profile</h2>
      <input value={first} onChange={(e) => setFirst(e.target.value)} placeholder="First Name" />
      <input value={last} onChange={(e) => setLast(e.target.value)} placeholder="Last Name" />
      <button onClick={complete}>Submit</button>
    </div>
  );
}

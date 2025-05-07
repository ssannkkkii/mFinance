import { useEffect, useState } from "react";
import api from "../../utils/api";

export default function Profile() {
  const [data, setData] = useState(null);

  useEffect(() => {
    api.get("/users/profile/")
      .then(res => setData(res.data))
      .catch(() => window.location.href = "/login");
  }, []);

  if (!data) return <div>Loading...</div>;

  return (
    <div>
      <h2>Welcome, {data.first_name} {data.last_name}</h2>
      <p>Phone: {data.phone}</p>
      <p>Profile Completed: {data.is_profile_completed ? "Yes" : "No"}</p>
    </div>
  );
}

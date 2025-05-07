import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000/api", // або інший бекенд URL
  withCredentials: true,
});

export default api;
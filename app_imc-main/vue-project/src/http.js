import axios from "axios";

const http = axios.create({
    baseURL: import.meta.env.VITE_API_URL,
    headers: {
      "Access-Control-Allow-Origin": "*"
    }
  });

export default http;
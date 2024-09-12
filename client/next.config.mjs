/** @type {import('next').NextConfig} */
const nextConfig = {
  env: {
    STADIA_MAPS_API_KEY: process.env.STADIA_MAPS_API_KEY,
    BACKEND_URL: process.env.BACKEND_URL,
  },
};

export default nextConfig;

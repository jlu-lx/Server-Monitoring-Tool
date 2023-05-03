import axios from 'axios';

const API_URL = 'http://localhost:8080/api'; // 替换为后端Spring Boot应用程序的实际URL

const getServerStats = async () => {
  try {
    const response = await axios.get(`${API_URL}/server-stats`);
    return response.data;
  } catch (error) {
    console.error('Error fetching server stats:', error);
    return null;
  }
};

export default {
  getServerStats,
};

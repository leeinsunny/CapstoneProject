import React, { useState, useEffect } from 'react';
import axios from 'axios';
  
const Filter = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    const apiUrl = '/filter';

    axios.get(apiUrl)
    .then(response => {
      setData(response.data);
      console.log("Fetched data from backend server:", response.data );
    })
    .catch(error => {
      console.error('Cannot fetch data from backend server', error);
    });
  }, []);

  return (
    <div
      style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'stretch',
        height: '100vh'
      }}
    >
      <div>Hi this is 02_filter.js</div>
    </div>
  );
};

export default Filter;
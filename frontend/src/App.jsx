import React, { useEffect, useState } from 'react'
import axios from 'axios'

const App = () => {
  const [logs, setLogs] = useState([])

  useEffect(() => {
    axios.get('/api/logs')
      .then(res => setLogs(res.data))
      .catch(err => console.error('API error:', err))
  }, [])

  return (
    <div style={{ padding: '2rem' }}>
      <h1>SIEMLite - Log Viewer</h1>
      <table border="1" cellPadding="8">
        <thead>
          <tr>
            <th>Zaman</th>
            <th>IP</th>
            <th>Olay Türü</th>
            <th>Öncelik</th>
            <th>Mesaj</th>
          </tr>
        </thead>
        <tbody>
          {logs.map((log, i) => (
            <tr key={i}>
              <td>{log.timestamp}</td>
              <td>{log.source_ip}</td>
              <td>{log.event_type}</td>
              <td>{log.severity}</td>
              <td>{log.message}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default App

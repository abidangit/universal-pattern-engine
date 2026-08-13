import React, {useState} from 'react'
import axios from 'axios'

export default function App(){
  const [input, setInput] = useState('1,2,3,4')
  const [result, setResult] = useState(null)

  async function analyze(){
    try{
      const seq = input.split(',').map(s=>parseFloat(s.trim()))
      const r = await axios.post('/api/analyze', { sequence: seq })
      setResult(r.data)
    }catch(e){
      setResult({error: e.message})
    }
  }

  return (
    <div style={{padding:20,fontFamily:'Arial, sans-serif'}}>
      <h1>Universal Pattern Engine</h1>
      <p>Enter comma-separated numbers:</p>
      <input value={input} onChange={e=>setInput(e.target.value)} style={{width:'60%'}} />
      <button onClick={analyze} style={{marginLeft:10}}>Analyze</button>
      <pre style={{marginTop:20}}>{JSON.stringify(result, null, 2)}</pre>
    </div>
  )
}

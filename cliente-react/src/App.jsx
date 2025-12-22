import { useState, useEffect } from 'react';
import { getMarcas, getModelos, getAnos, getVeiculo } from './api';

function App() {
  const [marcas, setMarcas] = useState([]);
  const [modelos, setModelos] = useState([]);
  const [anos, setAnos] = useState([]);

  const [marcaId, setMarcaId] = useState('');
  const [modeloId, setModeloId] = useState('');
  const [anoId, setAnoId] = useState('');

  const [resultado, setResultado] = useState(null);

  useEffect(() => {
    getMarcas().then(dados => setMarcas(dados));
  }, []);

  async function selecionarMarca(e) {
    const id = e.target.value;
    setMarcaId(id);
    setModelos([]); 
    setAnos([]);
    setResultado(null);
    if(id) {
      const dados = await getModelos(id);
      setModelos(dados.modelos);
    }
  }

  async function selecionarModelo(e) {
    const id = e.target.value;
    setModeloId(id);
    setAnos([]);
    setResultado(null);
    if(id) {
      const dados = await getAnos(marcaId, id);
      setAnos(dados);
    }
  }

  async function consultar(e) {
    e.preventDefault();
    if (marcaId && modeloId && anoId) {
      const dados = await getVeiculo(marcaId, modeloId, anoId);
      setResultado(dados);
    }
  }

  return (
    <div className="container mx-auto py-10 px-4">
      <h1 className="text-3xl font-bold text-center text-blue-600 mb-8">Tabela Fipe (React)</h1>
      
      <div className="bg-white shadow-md rounded-lg p-6 max-w-md mx-auto">
        <form onSubmit={consultar} className="space-y-4">
          
          <select className="w-full border p-2 rounded" onChange={selecionarMarca} value={marcaId}>
            <option value="">Selecione a Marca</option>
            {marcas.map(m => <option key={m.codigo} value={m.codigo}>{m.nome}</option>)}
          </select>

          <select className="w-full border p-2 rounded" onChange={selecionarModelo} value={modeloId} disabled={!marcaId}>
            <option value="">Selecione o Modelo</option>
            {modelos.map(m => <option key={m.codigo} value={m.codigo}>{m.nome}</option>)}
          </select>

          <select className="w-full border p-2 rounded" onChange={e => setAnoId(e.target.value)} value={anoId} disabled={!modeloId}>
            <option value="">Selecione o Ano</option>
            {anos.map(a => <option key={a.codigo} value={a.codigo}>{a.nome}</option>)}
          </select>

          <button type="submit" className="w-full bg-blue-600 text-white font-bold py-2 rounded hover:bg-blue-700">
            Consultar Preço
          </button>
        </form>

        {resultado && (
          <div className="mt-6 p-4 bg-gray-50 rounded border">
            <h2 className="text-xl font-bold">{resultado.Modelo}</h2>
            <p>Ano: {resultado.AnoModelo}</p>
            <p className="text-2xl text-green-600 font-bold mt-2">{resultado.Valor}</p>
            <p className="text-sm text-gray-500">Combustível: {resultado.Combustivel}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
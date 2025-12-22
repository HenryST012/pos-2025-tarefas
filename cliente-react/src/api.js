const API_BASE = "https://parallelum.com.br/fipe/api/v1/carros";

export async function getMarcas() {
  const res = await fetch(`${API_BASE}/marcas`);
  return res.json();
}

export async function getModelos(marcaId) {
  const res = await fetch(`${API_BASE}/marcas/${marcaId}/modelos`);
  return res.json();
}

export async function getAnos(marcaId, modeloId) {
  const res = await fetch(`${API_BASE}/marcas/${marcaId}/modelos/${modeloId}/anos`);
  return res.json();
}

export async function getVeiculo(marcaId, modeloId, anoId) {
  const res = await fetch(`${API_BASE}/marcas/${marcaId}/modelos/${modeloId}/anos/${anoId}`);
  return res.json();
}
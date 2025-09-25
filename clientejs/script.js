const API_BASE = 'https://parallelum.com.br/fipe/api/v1/carros';

const selectMarcas = document.getElementById('marcas');
const selectModelos = document.getElementById('modelos');
const selectAnos = document.getElementById('anos');
const divResultado = document.getElementById('resultado');

function resetSelect(select, placeholder) {
    select.innerHTML = `<option value="">${placeholder}</option>`;
    select.disabled = true;
}

function popularSelect(select, items, valueKey, nameKey) {
    items.forEach(item => {
        const option = document.createElement('option');
        option.value = item[valueKey];
        option.textContent = item[nameKey];
        select.appendChild(option);
    });
    select.disabled = false;
}

async function carregarMarcas() {
    try {
        const response = await fetch(`${API_BASE}/marcas`);
        if (!response.ok) throw new Error('Erro ao buscar marcas.');
        
        const marcas = await response.json();
        
        selectMarcas.innerHTML = '<option value="">Selecione a marca</option>'; // Limpa o "carregando"
        popularSelect(selectMarcas, marcas, 'codigo', 'nome');

    } catch (error) {
        console.error("Falha ao carregar marcas:", error);
        selectMarcas.innerHTML = '<option value="">Erro ao carregar</option>';
    }
}

async function carregarModelos() {
    const idMarca = selectMarcas.value;
    
    resetSelect(selectModelos, 'Selecione uma marca primeiro');
    resetSelect(selectAnos, 'Selecione um modelo primeiro');
    divResultado.style.display = 'none';

    if (!idMarca) return;

    resetSelect(selectModelos, 'Carregando modelos...');

    try {
        const response = await fetch(`${API_BASE}/marcas/${idMarca}/modelos`);
        if (!response.ok) throw new Error('Erro ao buscar modelos.');

        const data = await response.json();
        resetSelect(selectModelos, 'Selecione o modelo');
        popularSelect(selectModelos, data.modelos, 'codigo', 'nome');

    } catch (error) {
        console.error("Falha ao carregar modelos:", error);
        resetSelect(selectModelos, 'Erro ao carregar');
    }
}

async function carregarAnos() {
    const idMarca = selectMarcas.value;
    const idModelo = selectModelos.value;

    resetSelect(selectAnos, 'Selecione um modelo primeiro');
    divResultado.style.display = 'none';

    if (!idModelo) return;

    resetSelect(selectAnos, 'Carregando anos...');

    try {
        const response = await fetch(`${API_BASE}/marcas/${idMarca}/modelos/${idModelo}/anos`);
        if (!response.ok) throw new Error('Erro ao buscar anos.');
        
        const anos = await response.json();
        resetSelect(selectAnos, 'Selecione o ano');
        popularSelect(selectAnos, anos, 'codigo', 'nome');

    } catch (error) {
        console.error("Falha ao carregar anos:", error);
        resetSelect(selectAnos, 'Erro ao carregar');
    }
}

async function exibirResultado() {
    const idMarca = selectMarcas.value;
    const idModelo = selectModelos.value;
    const idAno = selectAnos.value;

    divResultado.style.display = 'none';
    
    if (!idAno) return;

    try {
        const response = await fetch(`${API_BASE}/marcas/${idMarca}/modelos/${idModelo}/anos/${idAno}`);
        if (!response.ok) throw new Error('Erro ao buscar detalhes do veículo.');

        const veiculo = await response.json();

        divResultado.innerHTML = `
            <p><strong>Valor:</strong> ${veiculo.Valor}</p>
            <p><strong>Marca:</strong> ${veiculo.Marca}</p>
            <p><strong>Modelo:</strong> ${veiculo.Modelo}</p>
            <p><strong>Ano do Modelo:</strong> ${veiculo.AnoModelo}</p>
            <p><strong>Combustível:</strong> ${veiculo.Combustivel}</p>
            <p><strong>Código FIPE:</strong> ${veiculo.CodigoFipe}</p>
            <p><strong>Mês de Referência:</strong> ${veiculo.MesReferencia}</p>
        `;
        divResultado.style.display = 'block';

    } catch (error) {
        console.error("Falha ao exibir resultado:", error);
        divResultado.innerHTML = '<p>Não foi possível carregar os detalhes do veículo.</p>';
        divResultado.style.display = 'block';
    }
}

document.addEventListener('DOMContentLoaded', carregarMarcas);
selectMarcas.addEventListener('change', carregarModelos);
selectModelos.addEventListener('change', carregarAnos);
selectAnos.addEventListener('change', exibirResultado);
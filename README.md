# Problema do Caixeiro Viajante (TSP) - Sul Fluminense

Este repositório implementa uma solução **exata (força bruta)** para o **Problema do Caixeiro Viajante (TSP)** aplicada a seis municípios da região Sul Fluminense do Estado do Rio de Janeiro.  
O objetivo é determinar o ciclo Hamiltoniano de menor distância total, partindo e retornando a **Volta Redonda**.

📂 Repositório: [tsp_sf](https://github.com/vitor-souza-ime/tsp_sf)

---

## 📌 Descrição

O **Problema do Caixeiro Viajante (TSP)** consiste em encontrar o caminho mais curto que passa exatamente uma vez por todas as cidades e retorna ao ponto de partida.  
Este problema é **NP-difícil** e, neste projeto, foi resolvido por **força bruta**, avaliando todas as permutações possíveis.

### Cidades consideradas:
- Volta Redonda (origem)
- Barra Mansa
- Pinheiral
- Quatis
- Piraí
- Valença

As distâncias foram coletadas no **Google Maps** utilizando rotas rodoviárias mais diretas.

---

## ⚙️ Funcionalidades

- Modelagem do problema como grafo completo não-direcionado (usando **NetworkX**).
- Cálculo exaustivo de todas as rotas possíveis (fixando Volta Redonda como ponto inicial).
- Determinação do **melhor ciclo Hamiltoniano**.
- Visualização do grafo:
  - Todas as conexões entre cidades com suas distâncias (arestas).
  - Melhor caminho destacado em **verde**.
  - Cidade de origem (**Volta Redonda**) destacada em **vermelho**.

---

## 🚀 Como executar

### 1. Clone o repositório
```bash
git clone https://github.com/vitor-souza-ime/tsp_sf.git
cd tsp_sf
````

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o programa

```bash
python main.py
```

---

## 📊 Exemplo de saída

```text
Melhor caminho (ciclo Hamiltoniano): ['Volta Redonda', 'Pinheiral', 'Piraí', 'Valença', 'Barra Mansa', 'Quatis', 'Volta Redonda']
Menor distância total (km): 214.9
Tempo de cálculo (s): 0.0051
```

E a execução gera o seguinte grafo com o caminho ótimo destacado:

![Exemplo de Grafo](docs/exemplo_saida.png)

---

## 📈 Complexidade

O algoritmo possui **complexidade temporal O(n!)**, onde `n` é o número de cidades.
No caso deste estudo (6 cidades), foram avaliadas **(6-1)! = 120 permutações**.
Embora seja viável para instâncias pequenas, este método torna-se inviável para conjuntos maiores de cidades.

---

## 📚 Dependências

* [Python 3.9+](https://www.python.org/)
* [NetworkX](https://networkx.org/)
* [Matplotlib](https://matplotlib.org/)

Instale tudo com:

```bash
pip install networkx matplotlib
```

---



Você quer que eu também monte o **`requirements.txt`** correspondente para o repositório (`networkx` e `matplotlib` com versões sugeridas)?
```

# Trabalho Prático 3 — Problema do Carteiro Chinês

## 📌 Disciplina

Resolução de Problemas com Grafos
Orientador: Prof. Me Ricardo Carubbi

---

## 🎯 Objetivo

O objetivo deste trabalho é aplicar conceitos de grafos direcionados ponderados no contexto do Problema do Carteiro Chinês, realizando:

* Identificação de vértices desbalanceados;
* Eulerização manual do grafo;
* Implementação do algoritmo de Hierholzer para encontrar um circuito euleriano;
* Cálculo do custo total do percurso.

---

## 📊 Modelagem do Problema

O grafo fornecido foi interpretado como um dígrafo ponderado, onde:

* Vértices representam pontos do grafo;
* Arestas representam conexões direcionadas com custo associado.

---

## ⚖️ Análise dos Graus

Foram calculados os graus de entrada e saída de cada vértice:

* Vértices com excesso de saída: **a, b**
* Vértices com excesso de entrada: **e, f**

---

## 🔧 Eulerização do Grafo

Para balancear o grafo, foram adicionadas arestas repetidas com base em caminhos já existentes, conectando vértices desbalanceados.

### Arestas adicionadas:

* e → a (12)
* f → c (22)
* c → a (20)
* a → b (10)

Essas adições garantem que todos os vértices tenham:

> grau de entrada = grau de saída

Tornando o grafo **euleriano**.

---

## 💻 Implementação

A solução foi implementada em Python, utilizando uma estrutura modular baseada no padrão algs4:

* `DirectedEdge.py`: representação de arestas ponderadas
* `Digraph.py`: estrutura do dígrafo
* `DirectedEulerianCycle.py`: implementação do algoritmo de Hierholzer
* `main.py`: leitura da entrada, execução e saída

---

## 🔁 Algoritmo de Hierholzer

O algoritmo de Hierholzer foi utilizado para encontrar um circuito euleriano no grafo eulerizado.

Ele funciona percorrendo o grafo e garantindo que todas as arestas sejam visitadas exatamente uma vez.

---

## ▶️ Execução do Programa

1. Acesse a pasta `src`:

```bash
cd src
```

2. Execute o programa:

```bash
python main.py
```

---

## 📤 Saída Esperada

O programa exibe:

* Graus de entrada e saída dos vértices;
* Verificação de balanceamento;
* Circuito euleriano encontrado;
* Custo total do percurso.

Exemplo:

```
Grafo balanceado! Executando Hierholzer...

Circuito Euleriano:
a -> b -> d -> f -> c -> a -> ...

Custo total: 259
```

---

## ✅ Conclusão

Após a eulerização manual, o grafo tornou-se balanceado, permitindo a aplicação do algoritmo de Hierholzer.

O circuito euleriano encontrado percorre todas as arestas exatamente uma vez, e o custo total reflete tanto as arestas originais quanto as adicionadas.


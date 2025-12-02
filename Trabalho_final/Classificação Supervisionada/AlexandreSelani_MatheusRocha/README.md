# Detecção de Invasão em Redes com OPF (Optimum-Path Forest)

Este diretório contém os arquivos do trabalho final da disciplina de Inteligência Artificial, referente à sessão de Classificação Supervisionada. O projeto foca na implementação e análise do classificador Optimum-Path Forest (OPF) aplicado à detecção de intrusão em redes de computadores em comparação com outros modelos e trabalhos anteriores.

## Autores
* Alexandre Luis Frata Selani
* Matheus Rocha de Almeida

## Conteúdo

A entrega consiste nas seguintes pastas e arquivos:

* **Pasta Artigo**
  * **AlexandreSelani_MatheusRocha-ClassificacaoSupervisionada (.pdf)**: Documentação completa abordando a teoria, metodologia, experimentos e a análise dos resultados obtidos.
  * **AlexandreSelani_MatheusRocha-ClassificacaoSupervisionada_apresentacao (.pdf)**: Arquivo utilizado para apresentação do trabalho.
* **Pasta Código**
  * **OPF_IDS (.ipynb)**: Implementação em Python (Jupyter Notebook) utilizada para os experimentos, contendo o pré-processamento dos dados e a execução do classificador OPF.
  * **opf_ids (.py)**: Mesma aplicação acima mas já formatada para python.
* **Pasta Resultados**
  * **Pastas KDDCUP-X**: Pastas com os resultados gerados pelos nossos testes em cada uma das variações dos datasets, tanto as matrizes de confusão quanto os dados em .csv produzidos.

## Sobre o trabalho

O objetivo principal foi validar a eficiência do OPF em um cenário de segurança de redes e compará-lo com os modelos SVM-RBF e KNN. O fluxo de trabalho implementado inclui:

1.  Carregamento e pré processamento de datasets de tráfego de rede.
2.  Treinamento dos modelos OPF, SVM-RBF e KNN
4.  Avaliação de métricas de desempenho (Acurácia no estilo OPF, Acurácia padrão, F1-Score e tempo).

## Como Executar

Necessário ter o **Python 3.x** e o **Jupyter** instalados. As principais dependências incluem `numpy`, `pandas`, `sklearn` e a bilbioteca do OPF `OPFython`.

Para abrir o notebook:

```bash
jupyter notebook OPF_IDS.ipynb

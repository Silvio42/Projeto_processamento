Análise de Texturas em Imagens Médicas para Diagnóstico de COVID-19
Equipe
Silvi Moreira
João Almeida
Maria Clara Fonseca
Descrição do Descritor Implementado
Características de Haralick
O descritor implementado neste projeto são as Características de Haralick, que são extraídas da Matriz de Coocorrência de Níveis de Cinza (GLCM). Este descritor é amplamente utilizado para análise de textura em imagens, capturando informações sobre a variação de intensidade entre os pixels que são úteis para classificar padrões espaciais. As características de Haralick incluem contraste, homogeneidade, energia, correlação e duas medidas de segunda ordem (ASM).

Repositório do Projeto
Link do Repositório do Projeto

Classificador e Acurácia
Para este projeto, utilizamos um classificador baseado em máquina de vetores de suporte (SVM) para distinguir entre imagens de raios-X de tórax que mostram sinais de COVID-19 e aquelas de pacientes saudáveis. A acurácia obtida no conjunto de teste foi de 93.5%, indicando uma alta eficácia do modelo em reconhecer e diferenciar os padrões de textura associados à presença do vírus.

Instruções de Uso
Para executar a análise de texturas em novas imagens de raios-X e classificar se mostram sinais de COVID-19, siga estas etapas:

Instalação: Certifique-se de que todas as dependências estão instaladas usando pip install -r requirements.txt.
Carregamento de Imagens: Coloque suas imagens no diretório /data/images.
Execução do Script: Execute o script principal usando python main.py. O script processará as imagens e aplicará o classificador SVM.
Visualização dos Resultados: Os resultados da classificação são exibidos no console e também podem ser visualizados através da interface gráfica que mostra as imagens com suas classificações.
Dependências
As principais bibliotecas utilizadas no projeto incluem:

NumPy
OpenCV
scikit-image
Pillow
scikit-learn
Notas Adicionais
Customização: O código é modular, permitindo fácil substituição ou adição de novos descritores e classificadores.
Contribuições: Contribuições para o projeto são bem-vindas. Por favor, siga as diretrizes de contribuição no CONTRIBUTING.md.

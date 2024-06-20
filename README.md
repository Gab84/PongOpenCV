# PROJETO PONG VISION

<img src="https://cdn.discordapp.com/attachments/856567980363874325/1253171289837928448/PONG_VISION.png?ex=6674e236&is=667390b6&hm=d26c10e272a0e5f13bb77c7e8eb2ca689a2ae1751c952ff56796cc9fee5a1f8c&" />

## **HISTÓRIA (DE ONDE SAIU A INSPIRAÇÃO)**

A história do projeto foi pensada no intuito de trazer temas sobre o avanço tecnológico de forma divertida e didática, pensando nisso, nós nos inspiramos no jogo antigo “PONG”, que foi produzido pela Atari, em 1972. O antigo jogo se baseava em um árcade de tênis de mesa, com gráficos bidimensionais. A inspiração foi colocada apenas para tornar o jogo mais moderno, prático e atrativo ao público, sendo que, sua forma de utilizar-se e o seu modelo já existiam, mas com a inovação e a tecnologia que usufruímos hoje, ele foi revolucionado, para ampliar nossos ares em busca de facilitar e introduzir a programação em todos os âmbitos.

> **Nosso projeto tem como base a visão computacional, reconhecimento de imagens, tratamento de imagens e o aprendizado de máquina.**
> 

## **COMO FUNCIONA?**

O reconhecimento de imagem tem o intuito principal de reconhecer qual mão está na tela e a quantidade que estão aparecendo, se distinguindo da direita e esquerda, através do aprendizado de máquina que a biblioteca Mediapipe disponibiliza para nós.

Para o feito, utilizamos 100% da programação de ***Python*** a partir de bibliotecas previamente já criadas por outros desenvolvedores que auxiliaram na nossa produção, entre elas são: Opencv, Mediapipe e um pacote chamado Cvzone, os quais o compilava e deixava de forma mais prática pelas funções utilizadas no código.

Assim que colocamos a mão em frente à câmera e ela é reconhecida, dá início ao processo de visão computacional, responsável por fazer o trabalho de reconhecimento da imagem aparente na tela, frame por frame, sendo capturadas infinitas vezes, realizando a identificação que o usuário possa controlar a função desejada, e em seguida, o tratamento de imagens “desenha” para nós de forma didática todos os pontos de sombras na nossa mão, ou seja, reconhece todas as juntas dos nossos dedos e classifica em pontos simétricos,  tornando o controle e manuseio das funções do nosso código mais evidente. Esses pontos em completa identificação passa a fazer o uso do aprendizado de maquina e da visão computacional e o tratamento de imagens novamente, em um looping.

Funcionando nessa maneira, a máquina reconhece as mãos (se é a direita ou esquerda) e atribui esse valor na memória dela, e em questão de milésimos, calcula a posição da mão em relação aos pixels da câmera, e com base nisso, de forma instantânea, faz do usuário um “Jogador” ou como preferimos chamar, *controlador*. Diante disso, nesse momento o controlador comanda uma das duas bordas do “jogo” e de forma reconhecível, a máquina determina em qual lado irá controlar.

Em seguida, junto da posição da mão em cada frame gerado pela visão computacional, ajustada o reconhecimento pelos pixels com a posição da borda do “jogo” que o indivíduo irá controlar. O mesmo vale para a mão esquerda, há opção de jogar sozinho ou em dupla (que pode ser mais legal! :D )

Essas bibliotecas contam com inúmeras funções de extrema importância para a tecnologia, sua previsão é que a melhore para cada tipo de especialidade, sendo a visão computacional, o aprendizado de máquina e o tratamento de imagens, que estão presentes em quase tudo em sua volta atualmente.

## **INFORMAÇÕES GERAIS.**

Se você possui um celular que tenha reconhecimento facial, saiba que é utilizável para o aprendizado da máquina, a visão computacional, reconhecimento de imagens e seu tratamento, porém, um bom sistema possui um reconhecimento com uma alta capacidade de processamento e níveis de pontos superiores ao que trouxemos aqui.

Um ponto importante, é a tecnologia se tornou fundamental para o nosso avanço e modernização, é a nossa era. Porém, até as coisas mais cotidianas podem ser feitas de forma independente, seja para fins lucrativos, fins pessoais, diversão, controles ou diversos outros motivos existentes... Nesse projeto, tivemos o intuito de trazer de forma mais presente aos jovens dessa geração e veem jogos sendo lançados com realidade aumentada e afins, viemos mostrar, no mundo atual, que com a base de informática e força de vontade, é possível fazer coisas incríveis e grandiosas.

E com base nesse projeto, utilizando tudo que foi utilizado, é possível criar um sistema que reconheça lotação de um tanque, seja de líquido, ou em grãos, reconhecendo os produtos que estejam em uma prateleira, uma inspeção de trânsito, utilizando a visão computacional para reconhecimento de placas de carros, altura dos carros e etc...

# **A ACESSIBILIDADE QUE PODE SER USUFRUIDA.**

> Afinal, como o projeto teria acessibilidade ao público?
> 

No projeto PONG, podemos considerar como a tecnologia de visão computacional e aprendizado de máquina pode ser adaptada para ajudar pessoas com diferentes tipos de deficiência. A seguir estão algumas maneiras de fazer isso.

### **Controle de Interfaces por Movimento:**

> O projeto PONG pode ser adaptado para permitir que pessoas com mobilidade reduzida ou sem uso dos membros superiores controlem interfaces de computador ou dispositivos móveis. Por exemplo:
> 
- **Rastreamento Ocular:** Em vez de usar as mãos, o sistema pode ser adaptado para rastrear movimentos oculares, permitindo que pessoas com paralisia ou limitações motoras interajam com o computador.
- **Movimentos Faciais:** O reconhecimento facial pode ser usado para detectar expressões faciais ou pequenos movimentos da cabeça como forma de controle.

### **Educação Inclusiva:**

> Da forma que estamos mostrando a vocês, a adaptações no projeto PONG podem proporcionar experiências educacionais para crianças com deficiências físicas ou cognitivas:
> 
- **Jogos Educativos:** Utilizando a visão computacional para criar jogos educativos que são controlados por gestos, facilitando a interação de crianças com deficiências.
- **Interação Multissensorial:** Incorporando feedback tátil ou auditivo para auxiliar crianças com deficiência visual ou auditiva.

### **Reabilitação:**

> Tecnologias de reconhecimento de imagem e visão computacional podem ser usadas em programas de reabilitação:
> 
- **Terapias de Reabilitação Física:** Utilizando o controle por movimento para criar exercícios interativos para pacientes em recuperação de lesões ou cirurgias.
- **Monitoramento e Feedback:** Usar o sistema para monitorar movimentos e fornecer feedback em tempo real para garantir que os exercícios estejam sendo feitos corretamente.

### **Acessibilidade Digital:**

- **Navegação por Gestos:** Sistemas baseados em visão computacional que permitem a navegação em dispositivos móveis ou computadores através de gestos, sem a necessidade de interação física direta.
- **Leitura de Textos e Imagens:** O uso de aprendizado de máquina para reconhecer textos e imagens, fornecendo descrições auditivas para pessoas com deficiência visual.

### **Inclusão Social:**

> Garantindo que todas as pessoas possam participar de atividades sociais e recreativas:
> 
- **Jogos Inclusivos:** Adaptação do jogo PONG para ser controlado por diferentes tipos de movimentos, permitindo que pessoas com diferentes habilidades físicas possam jogar juntas.
- **Espaços Públicos Acessíveis:** Utilizando tecnologias similares para desenvolver sistemas de orientação e navegação em espaços públicos para pessoas com deficiência visual ou auditiva.

### **Adaptação do Ambiente:**

> Criando ambientes mais acessíveis através de tecnologias inteligentes:
> 
- **Casa Inteligente:** Implementação de controle por gestos para dispositivos domésticos, facilitando a vida de pessoas com deficiência motora.
- **Reconhecimento de Objetos:** Sistemas de visão computacional que ajudam a identificar e localizar objetos em casa, auxiliando pessoas com deficiência visual.

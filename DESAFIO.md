# 🍄 Mario Debug Challenge — Liga Acadêmica

Bem-vindo(a)! Vocês receberam uma versão **quebrada** do clássico Super Mario
Bros Liga Acadêmica - UFVJMusada apenas para fins educacionais. Alguém "sabotou" o código com **10
bugs** espalhados pelo jogo. Sua equipe tem **3h30 (210 minutos)** para
encontrar e corrigir o máximo de bugs possível.

## 🏰 A história

**🍄 O Reino Cogumelo está em perigo!**

Bowser invadiu o sistema que mantém o Reino Cogumelo funcionando e espalhou
bugs pelo código. Moedas deixaram de ser contabilizadas corretamente,
pontuações foram alteradas, blocos pararam de reagir e até os inimigos
começaram a se comportar de maneira inesperada.

Mario percebeu que não conseguiria resolver todos os problemas sozinho e
convocou os maiores heróis do reino para uma missão: restaurar o jogo antes
que Bowser consiga assumir o controle.

Cada equipe representa um personagem do universo Mario. Durante a
competição, os participantes deverão avançar pelo Reino Cogumelo, investigar
os problemas encontrados e corrigir os bugs escondidos no código.

A jornada começa com problemas simples e, conforme as equipes avançam, os
desafios se tornam mais complexos. No final, os participantes chegarão ao
Castelo de Bowser, onde estarão os últimos problemas do sistema.

## 👥 As equipes

Cada equipe poderá representar um personagem do universo Mario. A identidade
dos personagens é principalmente narrativa e visual: todas as equipes
enfrentam os mesmos desafios e possuem as mesmas condições.

| Equipe | Personagem |
|---|---|
| Equipe Mario | Mario |
| Equipe Luigi | Luigi |
| Equipe Peach | Peach |
| Equipe Yoshi | Yoshi |
| Equipe Toad | Toad |
| Equipe Daisy | Daisy |

## Como rodar o jogo

```bash
pip install pygame pytmx
python main.py
```

## 🎮 Controles

| Tecla | Ação |
|---|---|
| **Enter** | Começar o jogo (na tela inicial) |
| **→** / **←** | Andar para a direita / esquerda |
| **↑** | Pular (segure para pular mais alto; solte cedo para um pulo baixo) |
| **Shift esquerdo** | Correr. Com a flor de fogo, também atira bolas de fogo |

## Regras

1. Cada bug corrigido vale pontos, de acordo com a dificuldade (veja tabela).
2. Cada bug abaixo já vem com o **arquivo onde ele está** e uma **descrição
   do que deveria acontecer no jogo**. O trabalho de vocês é entender o
   código daquele arquivo, achar o trecho responsável por aquele
   comportamento, entender por que ele está errado, e corrigir. Em algumas
   missões, parte do código foi apagada: nesses casos, vocês vão precisar
   completá-lo.
3. **Não é permitido** simplesmente reescrever o jogo do zero ou copiar a
   versão original do GitHub — o objetivo é *debugar*, não substituir.
4. Cada correção deve alterar o **mínimo necessário** de código. Correções
   que quebram outra funcionalidade do jogo não pontuam.
5. Façam commits separados (ou marquem claramente) para cada bug corrigido.
6. Ao final, cada equipe faz uma demonstração rápida (2 min) mostrando os
   bugs corrigidos ao vivo para a comissão avaliadora.

## Os 10 desafios

> ⚠️ Dois arquivos (`Goombas.py` e `Player.py`) têm **dois bugs cada**.
> Não parem de procurar num arquivo só porque já acharam um problema nele.

---

### 🟢 Fáceis (10 pts cada)

**#1 — A gravidade está ao contrário** // Feito
📁 Arquivo: `Const.py`
Jogue o início da fase e preste atenção em como o Mario cai depois de
pular. O esperado é que ele suba, atinja o ponto mais alto e desça,
acelerando conforme cai — como qualquer objeto que você joga pra cima na
vida real. Tem algo puxando o Mario e os inimigos pro lado errado.

**#2 — Inimigo "tremendo" na parede**  // Feito
📁 Arquivo: `Entity.py`
Observe um Goomba ou Koopa andando até esbarrar numa parede ou bloco. O
esperado: ele deveria **virar de direção e continuar andando normalmente**,
como um "ricochete". Em vez disso, algo estranho acontece nesse momento —
o inimigo trava ou fica vibrando no lugar, sem seguir em frente.

**#3 — O cogumelo não sai do lugar** //Feito
📁 Arquivo: `Mushroom.py`
Quebre um bloco de interrogação que solta um cogumelo (power-up de
crescimento). Observe o que ele faz assim que "nasce". O comportamento
clássico do jogo é o cogumelo sair andando **na direção leste (direita)**
logo depois de sair do bloco — aqui ele fica parado, sem andar para
nenhum dos lados. O trecho de código que deveria colocar o cogumelo em
movimento está incompleto: vocês vão precisar escrevê-lo.

---

### 🟡 Médios (20 pts cada)

**#4 — Pisar no inimigo faz o oposto do esperado** // Não feito
📁 Arquivo: `Goombas.py`
No Super Mario clássico, pular em cima de um Goomba o esmaga (mata) e não
machuca o Mario. Encostar nele de lado, sem pular por cima, é que machuca o
Mario. Testem as duas situações neste jogo e comparem com o que
deveria acontecer.

**#5 — A animação do Goomba congela** // Feito
📁 Arquivo: `Goombas.py`
Deixe um Goomba andando livremente por 10-15 segundos, sem interagir com
ele, e observe o sprite (a imagem) dele bem de perto. O Goomba deveria
continuar animando as perninhas indefinidamente enquanto anda, mas depois
de um tempinho a imagem para de mudar, como se ele "travasse" visualmente
(mesmo continuando a se mover).

**#6 — Contador de moedas não soma** // Feito
📁 Arquivo: `Player.py`
Colete duas ou mais moedas seguidas e observe o número de moedas mostrado
no HUD (canto da tela). O esperado é que o contador **acumule** — 1, depois
2, depois 3... Aqui ele fica parado em 0, não importa quantas moedas o
Mario pegue. O trecho de código que deveria somar as moedas está
incompleto: vocês vão precisar escrevê-lo.

**#7 — Casco chutado não sai do lugar**  // Não foi feito
📁 Arquivo: `Koopa.py`
Pule em cima de um Koopa (tartaruga) até ele virar um casco parado, e
depois encoste nele de novo pra "chutá-lo". O casco deveria sair
deslizando **para longe do Mario** (na direção contrária de onde o Mario
está), pra ele poder usar o casco como arma contra outros inimigos sem se
machucar. Aqui, o casco continua parado depois do chute. O trecho de
código que deveria dar velocidade ao casco está incompleto: vocês vão
precisar escrevê-lo.

---

### 🔴 Difíceis (35 pts cada)

**#8 — O jogo nunca acaba quando o Mario perde todas as vidas**
📁 Arquivo: `Map.py`
O Mario começa com 3 vidas. Percam de propósito as 3 vidas seguidas (deixe
o Mario morrer 3 vezes) e observem o que acontece a cada morte. O esperado
é que o Mario faça a animação de morte (com o som) e, na terceira morte,
apareça uma tela de "Fim de Jogo" (Game Over). Isso não está acontecendo —
o Mario volta na hora para o começo da fase, como se nada tivesse
acontecido, e o contador de vidas continua descendo sem parar. O trecho de
código que deveria tratar a morte do Mario está incompleto: vocês vão
precisar escrevê-lo.

**#9 — A fase nunca termina de verdade**
📁 Arquivo: `Flag.py`
Cheguem até o fim da fase e toquem a bandeira. O esperado: a bandeira
desce até a base do mastro (uma animação rápida), e o Mario é levado pra
dentro do castelo, encerrando a fase com sucesso. Aqui, a bandeira começa a
descer... e nunca para: passa do pé do mastro, some pelo chão e o jogo fica
travado nessa animação para sempre. O trecho de código que deveria
encerrar a descida da bandeira está incompleto: vocês vão precisar
escrevê-lo.

**#10 — O Mario fica invencível para sempre depois do primeiro dano**
📁 Arquivo: `Player.py`
No jogo original, depois que o Mario perde um power-up (por exemplo, leva
um dano e vira "pequeno" de novo), ele fica **piscando e invencível por
alguns segundos** — proteção temporária pra ele conseguir se afastar do
perigo. Testem: tomem um dano de propósito e depois fiquem encostando em
inimigos repetidamente por bastante tempo (mais de 5-10 segundos) e vejam
se essa invencibilidade realmente acaba em algum momento, como deveria.

---

## Pontuação

| Dificuldade | Pontos por bug | Qtde | Subtotal |
|---|---|---|---|
| 🟢 Fácil | 10 pts | 3 | 30 |
| 🟡 Médio | 20 pts | 4 | 80 |
| 🔴 Difícil | 35 pts | 3 | 105 |

**Pontuação máxima: 215 pontos**

Critério de desempate: menor tempo total de submissão.

## Dicas de processo

- Comecem pelos fáceis para garantir pontos e se familiarizarem com a
  estrutura do código (uma classe por arquivo, nomes de métodos em
  português).
- Reproduzam o comportamento errado primeiro (consigam fazer o bug
  acontecer de propósito), só depois vão olhar o código — assim vocês
  sabem exatamente o que procurar.
- Nem todo comportamento "esquisito" é um dos 10 bugs listados — o jogo
  tem algumas simplificações propositais da versão original (não tem
  todos os inimigos/fases do jogo clássico). Foquem só no que está descrito
  acima.

Boa sorte, e que vença a melhor equipe de debugging! 🎮

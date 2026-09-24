# 🍄 Mario Debug Challenge — Liga Acadêmica

Bem-vindo(a)! Vocês receberam uma versão **quebrada** do clássico Super Mario
Bros (base original por [Liga Acadêmica - UFVJM](https://github.com/josuejuca/Super-Mario-Bros),
usada apenas para fins educacionais). Alguém "sabotou" o código com **10
bugs** espalhados pelo jogo. Sua equipe tem **3h30 (210 minutos)** para
encontrar e corrigir o máximo de bugs possível.

## Como rodar o jogo

```bash
pip install pygame pytmx
python main.py
```

Controles: Setas (mover), Cima (pular), Shift (correr / atirar fireball com power-up de fogo).

## Regras

1. Cada bug corrigido vale pontos, de acordo com a dificuldade (veja tabela).
2. Cada bug abaixo já vem com o **arquivo onde ele está** e uma **descrição
   do que deveria acontecer no jogo**. O trabalho de vocês é entender o
   código daquele arquivo, achar o trecho responsável por aquele
   comportamento, entender por que ele está errado, e corrigir.
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

**#1 — A gravidade está ao contrário**
📁 Arquivo: `Const.py`
Jogue o início da fase e preste atenção em como o Mario cai depois de
pular. O esperado é que ele suba, atinja o ponto mais alto e desça,
acelerando conforme cai — como qualquer objeto que você joga pra cima na
vida real. Tem algo puxando o Mario e os inimigos pro lado errado.

**#2 — Inimigo "tremendo" na parede**
📁 Arquivo: `Entity.py`
Observe um Goomba ou Koopa andando até esbarrar numa parede ou bloco. O
esperado: ele deveria **virar de direção e continuar andando normalmente**,
como um "ricochete". Em vez disso, algo estranho acontece nesse momento —
o inimigo trava ou fica vibrando no lugar, sem seguir em frente.

**#3 — Cogumelo anda para o lado errado**
📁 Arquivo: `Mushroom.py`
Quebre um bloco de interrogação que solta um cogumelo (power-up de
crescimento). Observe pra que lado ele começa a se mover assim que
"nasce". O comportamento clássico do jogo é o cogumelo sair andando **na
mesma direção geral que o Mario estava indo** quando o bloco foi
ativado — aqui ele está saindo para o lado oposto ao esperado.

---

### 🟡 Médios (20 pts cada)

**#4 — Pisar no inimigo faz o oposto do esperado**
📁 Arquivo: `Goombas.py`
No Super Mario clássico, pular em cima de um Goomba o esmaga (mata) e não
machuca o Mario. Encostar nele de lado, sem pular por cima, é que machuca o
Mario. Testem as duas situações neste jogo e comparem com o que
deveria acontecer.

**#5 — A animação do Goomba congela**
📁 Arquivo: `Goombas.py`
Deixe um Goomba andando livremente por 10-15 segundos, sem interagir com
ele, e observe o sprite (a imagem) dele bem de perto. O Goomba deveria
continuar animando as perninhas indefinidamente enquanto anda, mas depois
de um tempinho a imagem para de mudar, como se ele "travasse" visualmente
(mesmo continuando a se mover).

**#6 — Contador de moedas não soma**
📁 Arquivo: `Player.py`
Colete duas ou mais moedas seguidas e observe o número de moedas mostrado
no HUD (canto da tela). O esperado é que o contador **acumule** — 1, depois
2, depois 3... Mas o comportamento atual não é esse.

**#7 — Casco chutado vai contra o jogador**
📁 Arquivo: `Koopa.py`
Pule em cima de um Koopa (tartaruga) até ele virar um casco parado, e
depois encoste nele de novo pra "chutá-lo". O casco deveria sair
deslizando **para longe do Mario** (na direção contrária de onde o Mario
está), pra ele poder usar o casco como arma contra outros inimigos sem se
machucar. Aqui, o casco está indo na direção errada.

---

### 🔴 Difíceis (35 pts cada)

**#8 — O jogo nunca acaba quando o Mario perde todas as vidas**
📁 Arquivo: `Map.py`
O Mario começa com 3 vidas. Percam de propósito as 3 vidas seguidas (deixe
o Mario morrer 3 vezes) e observem o que acontece na terceira morte. O
esperado é que apareça uma tela de "Fim de Jogo" (Game Over). Isso não está
acontecendo — o jogo simplesmente continua reiniciando o Mario como se
nada tivesse acontecido. Dica de raciocínio: pensem em qual número exato
representa "não sobrou nenhuma vida" e comparem com o número que está
sendo checado no código.

**#9 — A fase nunca termina de verdade**
📁 Arquivo: `Flag.py`
Cheguem até o fim da fase e toquem a bandeira. O esperado: a bandeira
desce até a base do mastro (uma animação rápida), e o Mario é levado pra
dentro do castelo, encerrando a fase com sucesso. Aqui, a bandeira começa a
descer... e nunca chega a terminar essa descida, deixando o jogo travado
nessa animação para sempre. Dica de raciocínio: existe um valor que marca
"a bandeira já chegou ao final do mastro" — será que esse valor é
realmente alcançável, dado até onde a bandeira consegue descer?

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
